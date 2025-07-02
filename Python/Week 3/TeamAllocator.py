import random

players = ["Kamari", "Max", "Braylen",
           "Ollie", "Xavier", "Avery",
           "Carl", "Walter", "Darren",
           "EJ", "Nahum", "Joaquin",
           "Marshawn", "Ja'Den", "Isaiah",
           "Kenlon", "Nishad", "Kauri",
           "Kris", "Joseph", "Semaj",
           "Tay", "Taqari", "Jarmauri"]


def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players) // 2]
    teamCaptain1 = team1[random.randrange(0, 13)]

    print("TEAM 1:")
    print("Team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player)

    team2 = players[len(players) // 2:]
    teamCaptain2 = team2[random.randrange(0,13)]

    print("\nTEAM 2")
    print("Team 2 Captain: " + teamCaptain2)
    for player in team2:
        print(player)

PickTeams(players)

