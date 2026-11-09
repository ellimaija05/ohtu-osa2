class StatisticsService:
    def __init__(self, reader):
        self._reader = reader
        self._players = self._reader.get_players()

    def search(self, name):
        for player in self._players:
            if player.name == name:
                return player
        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )
        return list(players_of_team)

    def top(self, how_many):
        sorted_players = sorted(
            self._players,
            key=lambda player: player.points,
            reverse=True
        )
        return sorted_players[:how_many]
