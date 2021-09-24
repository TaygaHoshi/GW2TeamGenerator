from dataclasses import dataclass, field

@dataclass
class Player:
    name : str
    roles : list[str] = field(default_factory=list)
    is_taken : bool = False
    rating : float = 0.0

    def to_string(self):
        return "{0} - {1} - {2}".format(self.name, str(self.rating), str(self.roles))