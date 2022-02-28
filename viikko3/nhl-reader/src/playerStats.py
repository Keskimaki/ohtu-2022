class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = list(filter(lambda player: player.nationality == nationality, self.players))

        players.sort(reverse=True, key=lambda player: player.goals + player.assists)

        return players
