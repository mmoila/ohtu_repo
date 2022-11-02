from player_reader import PlayerReader


def sort_by(player, criteria):

    if criteria.name == "GOALS":
        return player.goals
    elif criteria.name == "ASSISTS":
        return player.assists
    elif criteria.name == "POINT":
        return player.points
    else:
        raise(Exception("Incorrect criteria"))


class Statistics:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()
        

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, criteria):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda p: sort_by(p, criteria)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
