def readFile():
    pass

def saveFile():
    pass

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