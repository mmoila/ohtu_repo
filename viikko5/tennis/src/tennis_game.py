class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {"name": player1_name, "points": 0}
        self.player2 = {"name": player2_name, "points": 0}
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1["name"]:
            self.player1["points"] += 1
        else:
            self.player2["points"] += 1

    def get_tie_score(self):
        if self.player1["points"] > 3:
            return "Deuce"
        return self.scores[self.player1["points"]] + "-All"

    def get_leading_player_name(self):
        if self.player1["points"] > self.player2["points"]:
            return self.player1["name"]
        return self.player2["name"]

    def get_score_after_forty(self):
        difference = abs(self.player1["points"] - self.player2["points"])
        leader = self.get_leading_player_name()
        if difference > 1:
            return f"Win for {leader}"
        return f"Advantage {leader}"

    def get_score(self):
        player1_points = self.player1["points"]
        player2_points = self.player2["points"]

        if player1_points == player2_points:
            return self.get_tie_score()

        elif player1_points >= 4 or player2_points >= 4:
            return self.get_score_after_forty()

        else:
            return f"{self.scores[player1_points]}-{self.scores[player2_points]}"
