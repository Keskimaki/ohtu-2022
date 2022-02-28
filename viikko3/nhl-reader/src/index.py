import requests
from datetime import datetime
from player import Player

def main():
    nationality = 'FIN'

    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print(f"Players from {nationality} {datetime.now()}\n")

    players = []

    for player_dict in response:
        if player_dict['nationality'] != nationality:
            continue

        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    players.sort(reverse=True, key=lambda player: player.goals + player.assists)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
