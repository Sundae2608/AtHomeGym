from api import Exercise

x = Exercise("seven_minutes_abs/")
for i in range(4):
    x.add_exercise("Seated Abs Left", 60, 0)
    x.add_exercise("Seated Abs Right", 60, 0)
    x.add_exercise("Drunken Mountain Climbers", 60, 30)
    x.add_exercise("Marching Plank", 60, 0)
    x.add_exercise("Scissors", 60, 0)
    x.add_exercise("Starfish Crunch", 30, 0)
    x.add_exercise("Russian V Tuck Twists", 30, 0)
x.play_exercise()