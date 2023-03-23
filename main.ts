radio.onReceivedValue(function (name, value) {
    if (name == "8") {
        basic.showString("" + (value))
        radio.sendValue("9", value)
    }
})
radio.setTransmitPower(7)
radio.setGroup(1)
basic.forever(function () {
	
})
