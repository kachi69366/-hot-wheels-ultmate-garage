serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
serial.set_rx_buffer_size(32)
Math_question = Math.random_boolean()
music.play(music.string_playable("B A G A G F A C5 ", 120),
    music.PlaybackMode.UNTIL_DONE)
led.plot_bar_graph(9, 9)

def on_forever():
    pass
basic.forever(on_forever)
