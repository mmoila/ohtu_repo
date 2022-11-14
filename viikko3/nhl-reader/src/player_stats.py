class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        return filter(lambda x: x.nationality == nationality,
                      all_players)
