import json 

class Score:
    def __init__(self, player, points):
        self.player = player
        self.points = points

    def __str__(self):
        return f"{self.player}: {self.point}"

class ScoreBoard:
    def __init__(self, target):
        if target <= 0:
            raise ValueError("target must be positive.")
        self.target = target
        self.scores = []

    def add(self, player, points):
        if points <= 0:
            raise ValueError("points must be positive.")
        self.scores.append(Score(player, points))

    def total(self):
        total = 0
        for s in self.scores:
            total = total + s.points
        return total

    def to_go(self):
        return self.target - self.total()

    def reached(self):
        return self.total() >= self.target

    def best(self):
        if not self.scores:
            return None
        return max(self.scores, key=lambda s: s.points)

    def at_least(self, target):
        for s in self.scores:
            if s.points >= target:
                yield s