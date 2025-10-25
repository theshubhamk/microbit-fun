def on_button_pressed_a():
    global F, A, C, E
    F = F / 2
    A = A / 2
    C = C / 2
    E = E / 2
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global F, A, C, E
    F = F * 2
    A = A * 2
    C = C * 2
    E = E * 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    music.play_tone(F, music.beat(BeatFraction.HALF))
    music.play_tone(A, music.beat(BeatFraction.HALF))
    music.play_tone(C, music.beat(BeatFraction.HALF))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

E = 0
C = 0
A = 0
F = 0
F = 349
A = 440
C = 523
E = 659