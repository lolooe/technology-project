def on_forever():
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_icon(IconNames.HEART)
    basic.show_string("Technology")
basic.forever(on_forever)

def on_forever2():
    music.play_melody("C D E F E D C G ", 99)
basic.forever(on_forever2)
