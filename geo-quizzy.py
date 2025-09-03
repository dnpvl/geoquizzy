from prompt import qst
from prompt import awe
import time
import random

diff_list = ["easy", "normal", "hard"]
diff = input("Choose a difficulty between 'easy', 'normal' or 'hard': ")
if diff not in diff_list:
    diff = "normal"

if diff == "easy":
    t = 24
elif diff == "hard":
    t = 8
else:
    t = 16

scr = 0
for i in range(10):
    ask = random.randint(0, len(qst) - 1)
    print(qst[ask])
    begin = time.time()
    play = input("Enter answer (all lowercase): ")
    if play:
        play = play.lower()
        end = time.time()

    if end - begin > t:
        print("You did not answer quickly enough.")
        print(f"Your score is {scr} out of 10.")
    elif play in awe[ask]:
        scr += 1
        print("Good answer!")
        print(f"Your score is {scr} out of 10.")
    else:
        print("That is not a good answer.")
        print(f"Your score is {scr} out of 10.")


    print("")
    qst.remove(qst[ask])
    awe.remove(awe[ask])

print("")
if diff == "easy" or diff == "normal":
    if scr < 10:
        scr += 1
print(f"Your final score is {scr} out of 10.")
print("Press enter to exit.")
input("")

