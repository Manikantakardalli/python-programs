# Cricket Scoreboard Simulator

team_name = input("Enter Team Name: ")
players = []

print("\nEnter Playing XI")
for i in range(11):
    player = input(f"Player {i+1}: ")
    players.append(player)

runs = 0
wickets = 0
balls = 0
extras = 0

batsman1 = players[0]
batsman2 = players[1]
next_batsman = 2

score = {}

for player in players:
    score[player] = {
        "Runs": 0,
        "Balls": 0,
        "Fours": 0,
        "Sixes": 0
    }

print("\n====== MATCH STARTED ======")

while wickets < 10 and balls < 120:

    print(f"\nScore : {runs}/{wickets}")
    print(f"Overs : {balls//6}.{balls%6}")
    print("Striker :", batsman1)
    print("Non-Striker :", batsman2)

    print("\nEnter Ball Result")
    print("0 1 2 3 4 6")
    print("W = Wicket")
    print("NB = No Ball")
    print("WD = Wide")

    ball = input("Result : ").upper()

    if ball in ["0", "1", "2", "3", "4", "6"]:

        run = int(ball)

        runs += run
        balls += 1

        score[batsman1]["Runs"] += run
        score[batsman1]["Balls"] += 1

        if run == 4:
            score[batsman1]["Fours"] += 1

        if run == 6:
            score[batsman1]["Sixes"] += 1

        if run % 2 == 1:
            batsman1, batsman2 = batsman2, batsman1

    elif ball == "W":

        balls += 1
        wickets += 1

        score[batsman1]["Balls"] += 1

        print(batsman1, "OUT!")

        if next_batsman < 11:
            batsman1 = players[next_batsman]
            next_batsman += 1
        else:
            break

    elif ball == "NB":

        runs += 1
        extras += 1
        print("No Ball")

    elif ball == "WD":

        runs += 1
        extras += 1
        print("Wide Ball")

    else:
        print("Invalid Input")

    if balls % 6 == 0:
        batsman1, batsman2 = batsman2, batsman1
        print("\n------ Over Completed ------")

print("\n=========== INNINGS OVER ===========")

print(f"\nFinal Score : {team_name} {runs}/{wickets}")
print(f"Overs : {balls//6}.{balls%6}")
print(f"Extras : {extras}")

print("\n========== SCORECARD ==========")

highest = ""
highest_runs = -1

for player in players:

    data = score[player]

    if data["Balls"] == 0:
        strike_rate = 0
    else:
        strike_rate = (data["Runs"] / data["Balls"]) * 100

    print("-" * 40)
    print("Player :", player)
    print("Runs :", data["Runs"])
    print("Balls :", data["Balls"])
    print("4s :", data["Fours"])
    print("6s :", data["Sixes"])
    print("Strike Rate : {:.2f}".format(strike_rate))

    if data["Runs"] > highest_runs:
        highest_runs = data["Runs"]
        highest = player

print("\n==============================")
print("Top Scorer :", highest)
print("Runs :", highest_runs)

run_rate = runs / (balls / 6)

print("Run Rate : {:.2f}".format(run_rate))

print("\nThanks for Playing!")