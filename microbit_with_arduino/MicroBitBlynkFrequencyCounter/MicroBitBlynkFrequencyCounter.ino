/*************************************************************
  Blynk is a platform with iOS and Android apps to control
  Arduino, Raspberry Pi and the likes over the Internet.
  You can easily build graphic interfaces for all your
  projects by simply dragging and dropping widgets.

    Downloads, docs, tutorials: http://www.blynk.cc
    Sketch generator:           http://examples.blynk.cc
    Blynk community:            http://community.blynk.cc
    Social networks:            http://www.fb.com/blynkapp
                                http://twitter.com/blynk_app

  Blynk library is licensed under MIT license
  This example code is in public domain.

 *************************************************************

  This example shows how to use BBC Micro:Bit
  to connect your project to Blynk.

  Note: This requires nRF5 support package:
    https://github.com/sandeepmistry/arduino-nRF5

  And BLEPeripheral library
    from http://librarymanager/all#BLEPeripheral
    or https://github.com/sandeepmistry/arduino-BLEPeripheral

  1. Select: Tools -> SoftDevice -> S110
  2. Select: Tools -> Programmer -> CMSIS-DAP
  3. Select: Tools -> nRF5 Flash SoftDevice
  4. Read and Accept License
  5. Verify and Upload Sketch

  NOTE: BLE support is in beta!

 *************************************************************/

#define BLYNK_USE_DIRECT_CONNECT

#define BLYNK_PRINT Serial

#include <BlynkSimpleSerialBLE.h>
#include <BLEPeripheral.h>
#include "BLESerial.h"
#include <Adafruit_Microbit.h>

#include "Wire.h"
#include <SparkFun_MAG3110.h>

 
MAG3110 compass = MAG3110();  // The compass chip
int baseline = 0;          

Adafruit_Microbit_Matrix microbit;

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "Your secret token from Blynk app"; 


// Create ble serial instance, parameters are ignored for MicroBit
BLESerial SerialBLE(0, 0, 0);




/* The frequency at which polledFrequency is updated. */
/* (Default: 4Hz) */
#define DATA_UPDATE_FREQ 4

/*Application */
#define SPOKES 1
#define RADIUS 0.311
float velocity = 0.0;
/***************************************
 * Code starts here, modify with care! *
 ***************************************/
/* The latest measured frequency of magnetometer*/
int polledFrequency = -1;

/* Printing delay time */
unsigned long printTime = 0;

void setup() {
  Serial.begin(9600);

  SerialBLE.setLocalName("Blynk");
  SerialBLE.setDeviceName("Blynk");
  SerialBLE.setAppearance(0x0080);
  SerialBLE.begin();

  Blynk.begin(SerialBLE, auth);

  Serial.println("Waiting for connections...");
  microbit.begin();
  microbit.clear();
  
  compass.initialize();       // Initializes the compass chip
  compass.start();            // Puts the sensor in active mode
  baseline = readStrength();  // Take a baseline reading of magnetic strength
  delay(500);

  
}

/***********************************
 * Frequency counter functionality *
 ***********************************/

/* Timestamp of the last time polledFrequency was updated */
unsigned long dataUpdateTime = 0;
/* How many times the PIN_SENSOR has switched state to HIGH since dataUpdateTime */
int frequencyCounter = 0;
/* State of the counter for comparison */
bool lastBlocked = false;


void updateFrequencyCounter() {
  /* Read the sensor state */
  bool currentlyBlocked = false;
  if (abs(readStrength() - baseline) > 15000) {
    currentlyBlocked = true;
  }
  
  if (currentlyBlocked && !lastBlocked) {
    /* Add to the counter if the sensor just switched to HIGH */
    frequencyCounter++;
  }
  /* Update state for next time */
  lastBlocked = currentlyBlocked;

  if (millis() - dataUpdateTime > (1.0 / DATA_UPDATE_FREQ) * 1000) {
    /* Update polledFrequency at the frequency of DATA_UPDATE_FREQ */
    dataUpdateTime = millis();
    /* Hz = N * Hz */
    polledFrequency = frequencyCounter * DATA_UPDATE_FREQ;

  if (millis() - printTime > 1000.0 / DATA_UPDATE_FREQ) {
    velocity = 2 * 3.1416 * polledFrequency / SPOKES* RADIUS * 3.6;
    printTime = millis();
  }
    /* Reset the frequency counter so it starts counting up again */
    frequencyCounter = 0;
  }
}




int readStrength() {
  int x, y, z;
  while(!compass.dataReady()) {};   // Wait for data to become available to read
  compass.readMag(&x, &y, &z);      // Read data into variables
  // calculate the RMS power combining x, y and z readings
  int power = sqrt((sq(float(x)) + sq(float(y)) + sq(float(z))) / 3);
  return power;
}



void loop() {
  SerialBLE.poll();

  if (SerialBLE) {    // If BLE is connected...
    updateFrequencyCounter();
    Blynk.virtualWrite(V0, velocity);
    Blynk.run();
  }
}

