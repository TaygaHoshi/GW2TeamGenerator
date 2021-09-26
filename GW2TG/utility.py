from Team import Team
from Player import Player

def readFile(filepath:str):
    
    player_list = []
    player_list.append(Player("Player1", ["healsupport","conditiondamage","powerdamage","bunker"], False, 1400))
    player_list.append(Player("Player2", ["powerdamage"], False, 1260))
    player_list.append(Player("Player3", ["healsupport","conditiondamage","powerdamage"], False, 1400))
    player_list.append(Player("Player4", ["conditiondamage","powerdamage"], False, 1300))
    player_list.append(Player("Player5", ["conditiondamage","powerdamage"], False, 1150))
    player_list.append(Player("Player6", ["conditiondamage","powerdamage","bunker"], False, 1600))
    player_list.append(Player("Player7", ["powerdamage"], False, 1450))
    player_list.append(Player("Player8", ["powerdamage"], False, 1350))
    player_list.append(Player("Player9", ["boonsupport","conditiondamage","powerdamage"], False, 1600))
    player_list.append(Player("Player10", ["healsupport","boonsupport"], False, 1200))
    player_list.append(Player("Player11", ["healsupport","conditiondamage","bunker"], False, 1500))
    player_list.append(Player("Player12", ["healsupport","conditiondamage","powerdamage"], False, 1300))

    return player_list

def saveFile(filepath:str, result:list[Team], leftovers:list[Player]):
    
    output_file = open(filepath, "w")

    for team in result:
        output_file.write(str(team.to_string()) + "\n")
        

    output_file.write("Maximum rating difference between teams:" + str(int(max_difference_in_result(result)))  + "\n")
    
    # print leftovers
    if len(leftovers) > 0:
        output_file.write("Leftover players:" + "\n")
        for player in leftovers:
            output_file.write(player.to_string() + "\n")
    else:
        output_file.write("There are no leftover players." + "\n")


def max_difference_in_result(teams):
    ratings = []
    for team in teams:
        ratings.append(team.average_rating)

    ratings.sort()
    return ratings[len(ratings) - 1] - ratings[0]

def is_result_better(teams_a, teams_b):
    if max_difference_in_result(teams_a) < max_difference_in_result(teams_b):
        return True
    else:
        return False

def reset_players(players):
    for p in players:
        p.is_taken = False

def rating_difference(a:float, b:float):
    if a >= b:
        return a - b
    else:
        return b - a

def print_result(result:list[Team], leftovers:list[Player]):
    
    print("-"*10)
    # print best resuls
    for team in result:
        print(team.to_string())

    print("-"*10)
    print("Maximum rating difference between teams:", int(max_difference_in_result(result)))
    
    # print leftovers
    if len(leftovers) > 0:
        print("Leftover players:")
        for player in leftovers:
            print(player.to_string())
    else:
        print("There are no leftover players.")