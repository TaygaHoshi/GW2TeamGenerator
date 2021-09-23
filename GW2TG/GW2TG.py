import random as rnd
from Player import Player
from Team import Team
from utility import *

def generate_teams(team_style : list[str], players : list[Player]):

    teams = []

    # get the player count per team
    team_size = len(team_style)

    # find the total average
    total_average = 0.0
    for p in players:
        total_average = total_average + float(p.rating)

    total_average = total_average / len(players)

    # add placeholders so the teams can have equal amount of players, including empty spots
    while not len(players) % team_size == 0:
        players.append(Player("Empty Slot", [], False, 0.0))
    
    team_count = len(players) / len(team_size)

    # generate teams
    # first, fill the nonrandom roles
    for team_index in range(team_count):

        # generate a team object with a temporary name 
        temp_team = Team(team_index, [], 0.0)

        # fill the roles for that team
        for role in team_style: 
            if not role == "random":
                possiblePlayers = []

                # find possible players for that role and populate a list with them
                for p in players: 
                    if not p.is_taken and not p.name == "Empty Slot" and role in p.roles:
                        possiblePlayers.append(p)
                
                if not len(possiblePlayers) == 0: # there are possible players for the role
                    
                    if not role == team_style[0] and not team_index == 0: # if it's not the first player of the team
                        
                        # choose the best player for the spot based on rating
                        best_player = possiblePlayers[0]
                        for p in possiblePlayers:
                            if rating_difference(total_average, best_player) > rating_difference(total_average, temp_team.new_average(p)):
                                best_player = p

                        temp_team.add_member(best_player)
                        best_player.is_taken = True

                    else: # if it's the first player of the team

                        # put a random player filling this initial role
                        temp_player = rnd.randint(0, len(possiblePlayers) - 1)
                        temp_team.add_member(temp_player)
                        temp_player.is_taken = True

                else: # there are no possible players for the role, add a free/wildcard spot
                    temp_team.add_member(Player("Empty Slot", 1200, role))

        teams.append(temp_team)

    # after that, fill random roles
    for team in teams:
        possibleRandomPlayers = []

        # gather available players
        for p in players:
            if not p.is_taken and not p.name == "Empty Slot":
                possibleRandomPlayers.append(p)
        
        if len(possibleRandomPlayers) > 0: # if there are available players

            best_player = possibleRandomPlayers[0]
            for p in possibleRandomPlayers:
                if rating_difference(total_average, best_player) > rating_difference(total_average, team.new_average(p)):
                    best_player = p
        
            team.add_member(best_player)
            best_player.is_taken = True
        else:
            team.add_member(Player("Empty Slot", [], True, 0.0))
            
    
    # return the teams created
    return teams



if __name__=="__main__":
    pass