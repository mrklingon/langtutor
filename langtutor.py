from adafruit_circuitplayground import cp
import time
import random
from blinknum import *
from wise import *
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

lang = "mandoa"

langs = ["mandoa","klingon","romulan","vulcan"]
lnum = 0
kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)


def compthink(cycles):
    for i in range (10*cycles):
        freq = random.randrange(200,1200)
        dur = random.uniform(.02,.125)
        cp.play_tone(freq,dur)


def prt(text):
    if cp.switch:
        print(text)
    else:
        layout.write(text + "\n")
def getWD(fnm):
    len = file_len(fnm)
    line = wisdom(random.randrange(len),fnm)
    line = line.strip("\n");
    (key, val) = line.split("\", \"")
    val = val.strip('"') #remove terminal "
    val = val.strip(' "')#remove initial ' "'
    key = key.strip( '"')
    return (key+" : " +val     )
prt(" ")
compthink(3)

def vocab(w):
    for i in range(w):
       prt(getWD(lang))
    prt(" ")


Done = False
while not Done:
    val = 0

    if cp.touch_A3: #reset game
        lnum = lnum + 1
        if lnum > 3:
            lnum = 0
        lang = langs[lnum]
        prt(lang)
        time.sleep(.25)

    if cp.button_a:
        a = getWD(lang)
        prt(a)
        val = val+1

    if cp.button_b:
        vocab(5)
        val = val+2

    if val == 1:
        cp.pixels.fill(blue)
        compthink(1)
        time.sleep(.25)
        cp.pixels.fill(blank)

    if val == 2:
        cp.pixels.fill(green)

        compthink(1)
        cp.pixels.fill(blank)

    if val == 3:
        prt ("Qapla'!")
        Done = True
