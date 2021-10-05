from dataclasses import dataclass, field
from Player import Player

@dataclass
class Team:
    team_ID : int
    members : list[Player] = field(default_factory=list)
    average_rating : float = 0.0

    def add_member(self, p : Player):
        self.members.append(p)
        self.average_rating = self.average_rating + ((p.rating - self.average_rating) / (len(self.members) + 1))

    def new_average (self, p : Player):
        return self.average_rating + ((p.rating - self.average_rating) / (len(self.members) + 1))

    def to_string(self):
        result = "Team {0}, size: {1:.0f}, rating: {2}\n".format(self.team_ID, len(self.members), self.average_rating)

        for p in self.members:
            result += p.to_string() + "\n"

        return result