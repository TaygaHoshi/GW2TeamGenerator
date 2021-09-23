import random as rnd
from Player import Player
from Team import Team

def generate_teams(team_style : list[str], players : list[Player]):

    # get the player count per team
    team_size = len(team_style)

    # fill the gaps so player count is divisible
    while not len(players) % team_size == 0:
        players.append(Player("Empty Slot", [], False, 0.0))
    
    team_count = len(players) / len(team_size)

    # generate teams
    # first, fill the nonrandom roles
    for team_index in range(team_count): # generate a team object with a temporary name 
        temp_team = Team(team_index, [], 0.0)

        for role in team_style: # fill the roles for that team
            if not role == "random":
                possiblePlayers = []

                for p in players: # find possible players for that role and populate a list with them
                    if not p.is_taken and not p.name == "Empty Slot" and role in p.roles:
                        possiblePlayers.append(p)
                
                if not len(possiblePlayers) == 0: # there are possible players for the role
                    # BURDASIN BURDASIN BURDASIN
                    pass
                else: # there are no possible players for the role, add a free/wildcard spot
                    temp_team.add_member(Player("Empty Slot", 1200, role))

                



if __name__=="__main__":
    pass