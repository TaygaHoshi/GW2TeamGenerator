from Team import Team
from Player import Player

def read_file(filepath:str):
    # read a .tsv file
    
    if len(filepath) == 0 or not filepath[-4:] == ".tsv":
        filepath = ".\\players.tsv"

    inputfile = open(filepath, "r") 
    player_list = []

    # skip the first line because it's a header
    lines = inputfile.readlines()[1:]

    # split the line and populate a list with Players
    # see https://docs.google.com/spreadsheets/d/1O0T7o7Ba5PsGFEjuCciyZzo7o7KxsEjgKuqQEnJ10pg
    
    for line in lines:
        splitted_line = line.split("\t")
        
        timestamp = splitted_line[0]
        name = splitted_line[1]
        classes = splitted_line[2].split(",")
        roles = splitted_line[3].split(",")
        rating = int(splitted_line[4])

        generated_player = Player(name, classes, roles, rating=rating)
        player_list.append(generated_player)
    
    return player_list

def save_file(filepath:str, result:list[Team], leftovers:list[Player]):
    
    # Save a .txt file

    if len(filepath) == 0:
        filepath = ".\\GW2TG_Output.txt"
    else:
        filepath = filepath + "\\GW2TG_Output.txt"
    
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