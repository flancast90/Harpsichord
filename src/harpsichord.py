# STEPS: 
# read file line by line
# for each line, map sound to recognised symbols: +-%&*/;?"'!${}=_()[], which is played for the number of s of the line length/1000, *200

from pysine import sine 
import os, time, math
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# C, D, E, F, G, A, B
key = 0 

# octave num (1, 2, 3, 4, 5, 6, 7 not included for ease-of-programmability)
octave = 0

OCTAVEINT1 = 4
OCTAVEINT2 = 16
OCTAVEINT3 = 28
OCTAVEINT4 = 40
OCTAVEINT5 = 52
OCTAVEINT6 = 64
OCTAVEINT7 = 76
OCTAVEINT8 = 88

# major or minor
mm = ""

def main_menu():
    global key, mm, octave
    key = random_("key")
    mm = random_("mm")
    octave = random_("octave")
    print("\n\n"+bcolors.OKCYAN + "Your directory: "+os.getcwd()+ bcolors.ENDC)
    path = input("\nHarpsichord: A Pythonic Approach to Making Music with Code.\nEnter file path to begin: ")
    make_music(path)

def random_(arg):
    if arg == "key":
        # Choose a number between 1 and 7
        rand = randint(0, 6)+1
        # Map number to appropriate "letter"
        return rand
    elif arg == "mm":
        # Choose a number between 1 and 2
        rand_ = randint(0,1)+1
        if rand_ == 1:
            return "major"
        elif rand_ == 2:
            return "minor"
    elif arg == "octave":
        _rand_ = randint(0,5)+1
        return _rand_

def make_music(dir_):
    with open(dir_) as file_:
        for index, line in enumerate(file_):
            print("Line {}: {}".format(index, line.strip()))
            map_keys(line.strip())

def map_keys(code):
# Modified from https://stackabuse.com/read-a-file-line-by-line-in-python
    symbols = ['+', '-', '%', '&', '*', '/', ';', '?', '"', '\'', '!', '$', '{', '}', '=', '_', '(', ')', '[', ']', ',', '.', '#', '`', '\\']
    for item in symbols:
        if item in code:
            play_sound((len(code)/8000)*80)
        
    #print(bcolors.OKGREEN + code + key + mm + str(octave) + bcolors.ENDC)
def play_sound(length):
    # important numbers pertaining to note and octave frequency translations
    # C1 is 32.7032, C2 is 65.4064, highest is C8 (C1*2^7)
    # Each key up is 1.05946371509 times the lower
    # (32.7032*2^[octaveNum-1])*1.05946371509^surplus
    C1 = 32.7032
    note = pick_random_note("note")
    motion = pick_random_note("motion")
    if motion == "up":
        note_loc = (octave*12)+note+4
    elif motion == "down":  
        note_loc = (octave*12)-note+4
    OCTAVE = math.floor((note_loc+8)/12)
    SURPLUS = note_loc - globals()["OCTAVEINT"+str(OCTAVE)]
    #TESTING print("SURPLUS="+str(SURPLUS)+", OCTAVE="+str(OCTAVE)+", NOTE="+str(note_loc)+" , frequency="+str(C1*(2**(OCTAVE-1))*(1.05946371509**(SURPLUS)))+" , duration="+str(length))
    sine(frequency=(C1*(2**(OCTAVE-1))*(1.05946371509**(SURPLUS))), duration=length)

def pick_random_note(arg):
    if arg == "note":
        return randint(0, 7)+1
    elif arg == "motion":
        rand = randint(0,1)
        if rand == 0:
            motion = "down"
        elif rand == 1:
            motion = "up"
        return motion

main_menu()  
