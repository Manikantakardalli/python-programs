# Electronic Voting Machine (EVM)

votes = {
    "Rahul": 0,
    "Priya": 0,
    "Arjun": 0,
    "NOTA": 0
}

print("======WELCOME TO EVM =======")

while True:
    print("\nCandidates")
    print("1. Rahul")
    print("2. Priya")
    print("3. Arjun")
    print("4. NOTA")
    print("5. End Voting")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        votes["Rahul"] += 1
        print("Vote Cast Successfully!")
    elif choice == 2:
        votes["Priya"] += 1
        print("Vote Cast Successfully!")
    elif choice == 3:
        votes["Arjun"] += 1
        print("Vote Cast Successfully!")
    elif choice == 4:
        votes["NOTA"] += 1
        print("Vote Cast Successfully!")
    elif choice == 5:
        break
    else:
        print("Invalid Choice!")

print("\n:---RESULT---:")

for candidate, count in votes.items():
    print(candidate, ":", count)

max_votes = max(votes.values())
winners = []

for candidate, count in votes.items():
    if count == max_votes:
        winners.append(candidate)

if len(winners) == 1:
    print("\nWinner:", winners[0])
    print("Votes:", max_votes)
else:
    print("\nElection Tie Between:", winners)
    print("Votes:", max_votes)

print("\nThank You for Voting!")