import sys
import time
import pyautogui
import keyboard

mapping = {"1": (848, 500), "2": (887, 501), "3": (922, 499), "4": (961, 502), "5": (996, 498), "6": (1036, 501), "7": (1068, 500)}

songs = {
    1: {"name": "HymnToTheJoy", "pattern": "3.3.4.5.5.4.3.2.1.1.2.3.3..22..3.3.4.5.5.4.3.2.1.1.2.3.2..11", "delay": 0.1484},
    2: {"name": "FrereJacques", "pattern": "2..3..4..2..2..3..4..2...4..5..6....4..5..6....6.7.6.5.4...2...6.7.6.5.4..2..2..1..2...2..1..2", "delay": 0.0484},
    3: {"name": "AmazingGrace", "pattern": "1..3..3...5.4.3.5...4..3...2..1...1..3..3...5.4.3.5...4..6..6....4..6..6...5.4.3.5....4..3...2.1....1..3..3...5.4.3.5...4..3", "delay": 0.0484},
    4: {"name": "BrahmsLullaby", "pattern": "1.1.3...1.1.3...1.3.6..5..4.4..3...1.2.3..1..1.2.3...1.3.6.5.4..6..7", "delay": 0.0484},
    5: {"name": "HappyBirthdayToYou", "pattern": "1.12..1..3..2....1.12..1..4..3....1..1.6..5..4..3.2....5.54..2..3..2", "delay": 0.0484},
    6: {"name": "Greensleeves", "pattern": "3.4..5.6..76.5..4.3..23.4..3.3.23.4..2.1..3.4..5.6..76.5..4.2..34.5..43.2..12.3", "delay": 0.0484},
    7: {"name": "Geometry", "pattern": "3.5.3.1.3.5.3...3.5.3.5.765432.2.5.3.1.3.5.3..7.65.43.2.1", "delay": 0.0984},
    8: {"name": "Minuet", "pattern": "6.23456.2.2.7.34567.2.2.5.65434.54323.43212", "delay": 0.0484},
    9: {"name": "JoyToTheWorld", "pattern": "7.6.54..4.3.21..45..56..67..77654.44321357", "delay": 0.0484},
    10: {"name": "GodlyImagination", "pattern": "3.7.2.3.7.2.3.7.2.3.7.2..1.3.5..1.2.5..1.3.6.767676.5.2.3.4..6.7.5..4.3.2.323", "delay": 0.0484},
    11: {"name": "LaVieEnRose", "pattern": "6..54.32.65..43.21.54..32.12.54..3...7..65.43.65..43.21.54..32.12.54...3...6..54.32.65..43.21.54..32..1.55...6.6..56.6..56.6..52...6.6..56.6..56.6..57.4..6.1..5654.32.65.1..43.21.54.34.56", "delay": 0.0484}
}

print("\nAvailable Songs:")
for num, song in songs.items():
    print(f"{num}. {song['name']}")

while True:
    try:
        selection = int(input("\nEnter the number of the song you want to play (1-11): "))
        if 1 <= selection <= 11:
            break
        print("Please enter a number between 1 and 11")
    except ValueError:
        print("Please enter a valid number")

selected_song = songs[selection]
pattern = selected_song["pattern"]
delay = selected_song["delay"]

print(f"\nSelected: {selected_song['name']}")
print("Press 'S' to start the pattern. Press 'Q' to stop the program at any time.")

running = True
started = False

def stop_program():
    global running
    running = False
    print("\nProgram stopped by user!")

def start_pattern():
    global started
    started = True
    print("\nStarting pattern!")

keyboard.on_press_key('q', lambda _: stop_program())
keyboard.on_press_key('s', lambda _: start_pattern())

while not started and running:
    time.sleep(0.1)

if running:
    for note in pattern:
        if not running:
            break
        if note == ".":
            time.sleep(0.25)
        else:
            x, y = mapping[note]
            pyautogui.moveTo(x, y)
            pyautogui.press('w')
            time.sleep(delay)

keyboard.unhook_all()


