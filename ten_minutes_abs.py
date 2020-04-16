from api import Exercise

x = Exercise("ten_minutes_abs/")
for i in range(4):
    x.add_exercise("Jumping Jacks", 45, 15)
    x.add_exercise("Bicycle Crunch", 45, 15)
    x.add_exercise("High Knee Taps", 45, 15)
    x.add_exercise("Russian Twists", 45, 15)
    x.add_exercise("Mountain Climber", 45, 15)
    x.add_exercise("Leg Raises", 45, 15)
    x.add_exercise("In and Out, Open and Close", 45, 15)
    x.add_exercise("Plank, Side to Side", 45, 15)
    x.add_exercise("Star Crunch", 45, 15)
    x.add_exercise("High Knee Runs", 45, 30)
x.play_exercise()