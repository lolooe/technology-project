basic.forever(function () {
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showIcon(IconNames.Heart)
    basic.showString("Technology")
})
basic.forever(function () {
    music.playMelody("C D E F E D C G ", 90)
})
