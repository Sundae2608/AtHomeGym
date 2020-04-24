from api import Exercise

x = Exercise("pull_up_practice/")
for i in range(5):
    x.add_exercise("Dead hang", 30, 10)
    x.add_rep_exercise("Australian pull up wide", 10, 4, 20)
    x.add_rep_exercise("Australian pull up medium", 10, 4, 20)
    x.add_rep_exercise("Australian pull up narrow", 10, 4, 20)
    x.add_rep_exercise("Negative pull up", 10, 10, 20)
    x.add_rep_exercise("Assisted pull up", 10, 4, 10)