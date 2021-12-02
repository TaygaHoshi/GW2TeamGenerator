import random as rnd
from Player import Player
from Team import Team
from utility import *
from math import ceil

def generate_teams(team_style : list[str], players : list[Player]):

    # get the player count per team
    teams = []
    team_size = len(team_style)

    # find the total average
    total_average = 0.0
    for p in players:
        total_average = total_average + float(p.rating)

    total_average = total_average / len(players)

    # find number of teams
    # if there are more than half the player amount needed to create a new team
    if len(players) % team_size >= ceil(team_size/2.0):
        while not len(players) % team_size == 0:
            players.append(Player("Empty Slot", [], [], rating=0.0))
        
    closest_player_count = len(players) - (len(players) % team_size)
    team_count = closest_player_count // team_size
    
    
    

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
                    if not (p.is_taken == True or p.name == "Empty Slot") and any(role in s for s in p.roles):
                        possiblePlayers.append(p)
                
                if not len(possiblePlayers) == 0: # there are possible players for the role
                    if not (role == team_style[0] or  team_index == 0): # if it's not the first player of the team
                        
                        # choose the best player for the spot based on rating
                        best_player = possiblePlayers[0]
                        for p in possiblePlayers:
                            if rating_difference(total_average, best_player.rating) > rating_difference(total_average, temp_team.new_average(p)):
                                best_player = p

                        temp_team.add_member(best_player)
                        best_player.is_taken = True

                    else: # if it's the first player of the team

                        # put a random player filling this initial role
                        temp_player = possiblePlayers[rnd.randint(0, len(possiblePlayers) - 1)]
                        temp_team.add_member(temp_player)
                        temp_player.is_taken = True

                else: # there are no possible players for the role, add a free/wildcard spot
                    temp_team.add_member(Player("Empty Slot", [], [role], rating=0.0))

        teams.append(temp_team)

    # after that, fill random roles
    random_role_count = 0
    for role in team_style:
        if role == "random":
            random_role_count += 1
    
    for team in teams:

        for i in range(random_role_count):

            possibleRandomPlayers = []

            # gather available players
            for p in players:
                if not p.is_taken and not p.name == "Empty Slot":
                    possibleRandomPlayers.append(p)
        
            if len(possibleRandomPlayers) > 0: # if there are available players

                best_player = possibleRandomPlayers[0]
                for p in possibleRandomPlayers:
                    if rating_difference(total_average, best_player.rating) > rating_difference(total_average, team.new_average(p)):
                        best_player = p
        
                team.add_member(best_player)
                best_player.is_taken = True
            else: # if there are no available players
                team.add_member(Player("Empty Slot", [], [], True, 0.0))
            
    
    # return the teams created
    return teams

def generate_result(style:list[str], player_list:list[Player], reroll_count:int):

    # find best result
    best_result = generate_teams(style, player_list)

    for x in range(reroll_count):
        reset_players(player_list)
        temp_result = generate_teams(style, player_list)
        if is_result_better(temp_result, best_result):
            best_result = temp_result
    
    # these next two for loops should not be necessary, needs further bugfixing
    # the script might put the same player in more than once because of this bug:
    # sometimes, when a player is put into a team, its is_taken flag do not update and the player is put to leftovers. 
    
    for temp_player in player_list:
        temp_player.is_taken = False

    for gend_team in best_result:
        for gend_player in gend_team.members:
            gend_player.is_taken = True
            

    # find leftover players
    leftovers = []
    for p in player_list:
        if not p.name == "Empty Slot" and not p.is_taken:
            leftovers.append(p)

    return (best_result, leftovers)

if __name__=="__main__":
    # description of the No GUI version
    print("Please use Start.py instead.")
    input("Press Return/Enter to exit.")