from dataclasses import dataclass, field

@dataclass
class Player:
    name : str
    classes : list[str] = field(default_factory=list)
    roles : list[str] = field(default_factory=list)
    rating : float = 0.0
    is_taken : bool = False

    def to_string(self):
        return "{0} - {1} - {2}".format(self.name, str(self.rating), ", ".join(self.roles))