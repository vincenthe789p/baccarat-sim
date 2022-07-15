import baccarat as game

banker = 0
player = 0
ties = 0
total = 0
TRIALS = 1000000

for i in range(TRIALS):
    result = game.play()
    if result == "Player wins":
        player +=1
    elif result == "Banker wins":
        banker += 1
    elif result == "Tie":
        ties += 1
    else:
        exit("Invalid game result")
    total += 1


print("player: ", player/total)
print("banker: ", banker/total)
print("ties: ", ties/total)