def on_received_value(name, value):
    if name == "8":
        basic.show_string("" + str((value)))
        radio.send_value("9", value)
radio.on_received_value(on_received_value)

radio.set_transmit_power(7)
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
