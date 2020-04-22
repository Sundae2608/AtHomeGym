from api import Exercise

x = Exercise("brutal_ladder_hiit/")
x.add_exercise("Single leg hip rotation", 30, 10)
x.add_exercise("Knee to elbow crunches", 30, 10)
x.add_exercise("Squat Reach Ups", 30, 10)
x.add_exercise("Skater Jump", 30, 10)
x.add_exercise("Mountain Climber", 30, 10)

x.add_exercise("Scissors", 50, 10)
x.add_exercise("High Stepping", 50, 10)
x.add_exercise("Modified Burpees", 50, 10)
x.add_exercise("Mountain Climber", 50, 10)

x.add_exercise("Scissors", 40, 10)
x.add_exercise("High Stepping", 40, 10)
x.add_exercise("Modified Burpees", 40, 10)
x.add_exercise("Squats", 40, 10)

x.add_exercise("Scissors", 30, 10)
x.add_exercise("High Stepping", 30, 10)
x.add_exercise("Modified Burpees", 30, 10)
x.add_exercise("Jumping Jacks", 30, 10)

x.add_exercise("Scissors", 20, 10)
x.add_exercise("High Stepping", 20, 10)
x.add_exercise("Modified Burpees", 20, 10)
x.add_exercise("Squats", 20, 10)

x.add_exercise("Scissors", 10, 10)
x.add_exercise("High Stepping", 10, 10)
x.add_exercise("Modified Burpees", 10, 10)
x.add_exercise("Jumping Jacks", 10, 10)
x.play_exercise()