class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return (f"{self.name:25}   {self.team} " +
                f"{self.goals:2} + {self.assists:2} = {self.points}")
