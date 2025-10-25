input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    F = F / 2
    A = A / 2
    C = C / 2
    E = E / 2
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    music.playTone(988, music.beat(BeatFraction.Whole))
    music.playTone(165, music.beat(BeatFraction.Whole))
    music.playTone(932, music.beat(BeatFraction.Whole))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    F = F * 2
    A = A * 2
    C = C * 2
    E = E * 2
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    music.playTone(F, music.beat(BeatFraction.Half))
    music.playTone(A, music.beat(BeatFraction.Half))
    music.playTone(C, music.beat(BeatFraction.Half))
})
let E = 0
let C = 0
let A = 0
let F = 0
F = 349
A = 440
C = 523
E = 659
