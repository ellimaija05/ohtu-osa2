from urllib.request import urlopen
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = urlopen(self._url)
        try:
            data = response.read().decode("utf-8")
            lines = data.splitlines()
            players = []
            for line in lines:
                parts = line.split(";")
                if len(parts) >= 4:
                    name = parts[0].strip()
                    team = parts[1].strip()
                    goals = int(parts[2].strip())
                    assists = int(parts[3].strip())
                    players.append(Player(name, team, goals, assists))
            return players
        except Exception:
            return []
