from dataclasses import dataclass, field
from Player import Player

@dataclass
class Team:
    team_ID : int
    members : list[Player] = field(default_factory=list)
    average_rating : float = 0.0

    def add_member(self, p : Player):
        self.members.append(p)

        self.average_rating = 0.0

        for player in self.members:
            self.average_rating += player.rating

        self.average_rating = self.average_rating / len(self.members)

    def new_average (self, p : Player):

        new_rating = p.rating

        for player in self.members:
            new_rating += player.rating

        return new_rating/(len(self.members) + 1)

    def to_string(self):
        result = "Team {0}, size: {1}, rating: {2:.2f}\n".format(self.team_ID+1, len(self.members), self.average_rating)

        id = 1
        for p in self.members:
            result += str(id) + ". " + p.to_string() + "\n"
            id += 1

        return result