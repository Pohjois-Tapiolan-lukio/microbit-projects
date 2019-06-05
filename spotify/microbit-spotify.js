var SerialPort = require("serialport");
const Readline = SerialPort.parsers.Readline;
var spotify = require('spotify-node-applescript');

var port = new SerialPort('/dev/tty.usbmodem1412', {
 baudRate: 115200,
 autoOpen: false
})
const parser = new Readline();
port.pipe(parser);

port.open(() => {
    console.log("Port open");
    parser.on('data', (data) => {
        console.log('Received Data: ' + data.toString());
        processData(data);
    });
})

function processData(data) {
    if (data.indexOf('NEXT') == 0) {
        // Handle NEXT received
        spotify.setShuffling(false);
        spotify.next(function () {
            // Playing the next song
        });

    } else if (data.indexOf('PREVIOUS') == 0) {
        // Handle PREVIOUS received
        spotify.setShuffling(false);
        spotify.previous(function () {
            // Playing the previous song
        });

    } else if (data.indexOf('SHUFFLE') == 0) {
        // Handle SHUFFLE received
        spotify.setShuffling(true);
        spotify.next(function () {
            // Playing the next song
        });
    }
}
