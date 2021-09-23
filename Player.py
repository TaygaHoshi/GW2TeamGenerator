from dataclasses import dataclass, field

@dataclass
class Player:
    name : str
    roles : list[str] = []
    is_taken : bool = False
    rating : float = 0.0

    def to_string(self):
        return "{0} - {1} - {2}".format(self.name, str(self.rating), str(self.roles))