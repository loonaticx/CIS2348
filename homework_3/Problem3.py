jerseyNumber2playerRating = dict()


# Part 1 + Part 3
def gimmieRoster():
    print("ROSTER")
    for jerseyNum in sorted(jerseyNumber2playerRating.keys()):
        print(f"Jersey number: {jerseyNum}, Rating: {jerseyNumber2playerRating[jerseyNum]}")


# Part 7: Get players above specific rating
def gimmiePlayersViaRating():
    rating = int(input("Enter a rating:"))
    print()
    print(f"ABOVE {rating}")
    for jerseyNum, playerRating in jerseyNumber2playerRating.items():
        if playerRating > rating:
            print(f"Jersey number: {jerseyNum}, Rating: {rating}")


# Part 1 + Part 4
def registerPlayer(amt):
    if amt == 1:
        jerseyNumber = int(input(f"Enter a new player's jersey number:"))
        print()
        playerRating = int(input(f"Enter the player's rating:"))
        print()
        jerseyNumber2playerRating[jerseyNumber] = playerRating
        print()
        return

    for i in range(1, amt + 1):
        jerseyNumber = int(input(f"Enter player {i}'s jersey number:"))
        print()
        playerRating = int(input(f"Enter player {i}'s rating:"))
        print()
        jerseyNumber2playerRating[jerseyNumber] = playerRating
        print()


# Part 5: Delete player
def unregisterPlayer():
    jerseyNumber = int(input("Enter a jersey number:"))
    print()
    del jerseyNumber2playerRating[jerseyNumber]


# Part 6: Update players
def updatePlayer():
    jerseyNumber = int(input("Enter a jersey number:"))
    print()
    newRating = int(input("Enter a new rating for player:"))
    print()
    jerseyNumber2playerRating[jerseyNumber] = newRating


# Part 2: Menu
def makeMenu():
    MENU = """MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
"""
    print(MENU)
    wannaExit = False
    while not wannaExit:
        option = input("Choose an option:\n")
        if option == "q":
            wannaExit = True
        # Part 3: Output Roster
        elif option == "o":
            gimmieRoster()
        # Part 4: Add player
        elif option == "a":
            registerPlayer(1)
        # Part 5: Delete player
        elif option == "d":
            unregisterPlayer()
        # Part 6: Update players
        elif option == "u":
            updatePlayer()
        # Part 7: Output players above a specific rating value
        elif option == "r":
            gimmiePlayersViaRating()
        else:
            print("Invalid choice >:(")


if __name__ == "__main__":
    def partOne():
        registerPlayer(5)
        gimmieRoster()
    partOne()
    print()
    makeMenu()
