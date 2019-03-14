
game_dictionary = {'home':{'team_name': 'Brooklyn Nets',
                              'colors': ['Black', 'White'],
                             'players': {'Alan Anderson': {'number': 0,'shoe': 16,'points': 22,'rebounds': 12,'assists': 12,'steals': 3,'blocks': 1,'slam_dunks': 1},
                                          'Reggie Evans': {'number': 30,'shoe': 14,'points': 12,'rebounds': 12,'assists': 12,'steals': 12,'blocks': 12,'slam_dunks': 7},
                                           'Brook Lopez': {'number': 11,'shoe': 17,'points': 17,'rebounds': 19,'assists': 10,'steals': 3,'blocks': 1,'slam_dunks': 15},
                                         'Mason Plumlee': {'number': 1,'shoe': 19,'points': 26,'rebounds': 12,'assists': 6,'steals': 3,'blocks': 8,'slam_dunks': 5},
                                           'Jason Terry': {'number': 31,'shoe': 15,'points': 19,'rebounds': 2,'assists': 2,'steals': 4,'blocks': 11,'slam_dunks': 11}}},
                    'away':{'team_name': 'Charlotte Hornets',
                               'colors': ['Turquoise', 'Purple'],
                              'players': {'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2},
                                      'Bismack Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10},
                                         'DeSagna Diop': {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5},
                                           'Ben Gordon': {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0},
                                      'Brendan Haywood': {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12}}}}
                                            



def game_dict():
    return game_dictionary

#accesses the nested dictionary and returns the statistic of a specified player
def get_player_stats(player_name):
    #1st level key, 1st level values
    for location, team_stats in game_dictionary.items():
        #2nd lvl keys, 2nd level values
        for team_stat, players in team_stats.items():
            #go through the 3rd layer keys or find player looking for
            for data in players:
                #check for name
                if data == player_name:
                    #return the dict statistics of player
                    return players[player_name]



def num_points_scored(player_name):
    #return number of points of player
    return get_player_stats(player_name)['points']

def shoe_size(player_name):
    #return shoe size of player
    return get_player_stats(player_name)['shoe']

def team_colors(team_name):
    #1st level key, 1st level values
    for team_stats in game_dictionary.values():
        #check if you're on the team you are looking for
        if team_stats['team_name'] == team_name:
            #return the dict['key']
            return team_stats['colors']

def team_names():
    teams = []
    #go to both home and away dictionaries and append their 'team_names'
    for team_stats in game_dictionary.values():
        teams.append(team_stats['team_name'])
    #return list of team names
    return teams

#returns a list of all the players for a given team
def get_all_players_in_team(team_name):
    team_players = []
    #1st level key, 1st level values
    for location, team_stats in game_dictionary.items():
        #check if you are on the dict branch with the correct team
        if team_stats['team_name'] == team_name:
            #2nd lvl keys, 2nd level values
            for team_stats, players in team_stats.items():
                #check if in right dictionary
                if team_stats == 'players':
                    #go through the 3rd layer keys 
                    for player in players:
                        #append the player names to a list
                        team_players.append(player)
    #return the list of the players in the list
    return team_players

def player_numbers(team_name):
    #get a list of the team, players names
    team_players =  get_all_players_in_team(team_name)
    #get a list of the numbers of each player
    return list(map(lambda player: get_player_stats(player)['number'], team_players))

def player_stats(player_name):
    #return the dict of player
    return get_player_stats(player_name)

#returns the list number of points scored by the players in a team
def team_shoe(team):
    #get a list of players on the team
    team_players = get_all_players_in_team(team)
    #get a list of the points each player has
    return list(map(lambda player: shoe_size(player), team_players))

#returns index position of max of list of numbers - takes in list(not nested)
def get_max_index(score_lst):
    #go through score list
    for i, j in enumerate(score_lst):
        #check if current score is the max score
        if j == max(score_lst):
            #return index of max score
            return i

#returns top player in desired category(stats) - takes in a list of list
def get_top_player(teams, resp_team_stats):
    #get the index of max of each team
    max_ind = list(map(lambda team_points: get_max_index(team_points), resp_team_stats))
    #get a list of list of players on the team
    resp_team_players = list(map(lambda team: get_all_players_in_team(team), teams))
    #check which team had the higher scoring player
    #home team player = position 0 and away team player = position 1
    if resp_team_stats[0][max_ind[0]] > resp_team_stats[1][max_ind[1]]:
        return resp_team_players[0][max_ind[0]]
    else:
        return resp_team_players[1][max_ind[1]]

#returns the rebound count of the player witht the biggest foot
def big_shoe_rebounds():
    #get list of team names
    teams = team_names()
    #get a list of list of shoe size on the team
    resp_team_shoes = list(map(lambda player: team_shoe(player), teams))
    #get player with biggest foot
    big_foot = get_top_player(teams, resp_team_shoes)
    #return number of rebounds of player
    return get_player_stats(big_foot)['rebounds']



#print(game_dict())
#print(num_points_scored('Alan Anderson'))
#print(shoe_size('Alan Anderson'))
#print(team_colors('Brooklyn Nets'))
#print(team_names())
#print(player_numbers('Charlotte Hornets'))
#print(player_stats('Alan Anderson'))
#print(big_shoe_rebounds())

"""BONUS Questions: 1) Which player has the most points? Call the function most_points_scored.

                    2) Which team has the most points? Call the function winning_team.

                    3) Which player has the longest name? Call the function player_with_longest_name"""
                
#returns the list number of points scored by the players in a team
def team_points(team):
    #get a list of players on the team
    team_players = get_all_players_in_team(team)
    #get a list of the points each player has
    return list(map(lambda player: num_points_scored(player), team_players))

#returns the player who scored the most points in the game
def most_points_scored():
    #get list of team names
    teams = team_names()
    #get a list of list of scores on the team
    resp_team_points = list(map(lambda player: team_points(player), teams))
    #return player with most scored points
    return get_top_player(teams, resp_team_points)
 
#returns the winning team in the game
def winning_team():
    #get list of team names
    teams = team_names()
    #get a list of list of scores on the team
    resp_team_points = list(map(lambda player: team_points(player), teams))
    #turn list of scores into list of total's of each team - scores
    total_team_scores = list(map(lambda scores: sum(scores), resp_team_points))
    #compare who had the higher score
    if total_team_scores[0] > total_team_scores[1]:
        #return player who had the highest score in home team
        return teams[0]
    else:#return player who had the highest score in away team
        return teams[1]
    
def player_with_longest_name():
    #get list of team names
    teams = team_names()
    #list of list of players on each team
    team_players = list(map(lambda team: get_all_players_in_team(team), teams))
    #create a list of list of the len of the name of each player on each team
    name_len = []
    for team in team_players:
        #get a list of the length of each player name on team
        len_team = list(map(lambda player: len(player), team))
        #append it to another list to get a list of list
        name_len.append(len_team)
    #return the player with the longest name
    return get_top_player(teams, name_len)
    

    
#print(most_points_scored())
#print(winning_team())
#print(player_with_longest_name())
            

"""SUPER BOUNUS Question: Write a function that returns true if the player with the longest name had the most steals. Call the function long_name_steals_a_ton?."""
#returns number of steals of player
def num_points_stoled(player_name):
    #return number of points of player
    return get_player_stats(player_name)['steals']

#returns the list number of points scored by the players in a team
def steal_points(team):
    #get a list of players on the team
    team_players = get_all_players_in_team(team)
    #get a list of the points each player has
    return list(map(lambda player: num_points_stoled(player), team_players))

#returns the player who scored the most points in the game
def long_name_steals_a_ton():
    #get list of team names
    teams = team_names()
    #get a list of list of steals on the team
    resp_steal_points = list(map(lambda player: steal_points(player), teams))
    #get player with most scored points
    top_stealer = get_top_player(teams, resp_steal_points)
    #check if player witht he longest name is the top stealer
    if player_with_longest_name() == top_stealer:
        return True
    else:
        return False
    
                
print(long_name_steals_a_ton())
                
                
                
                