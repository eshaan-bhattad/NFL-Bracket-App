import json


def sortLeaderboardHighToLow():
    leaderboard = list()
    updateScores()
    with open(
            'data/brackets.json') as data:
        brackets = json.load(data)
        for bracket in brackets:
            leaderboardEntry = dict()
            leaderboardEntry['name'] = bracket['name']
            leaderboardEntry['points'] = bracket['points']
            leaderboardEntry['id'] = bracket['id']
            leaderboardEntry['superbowl'] = bracket['superbowl']
            leaderboardEntry['maxpoints'] = getRemainingPointsPossible(
                bracket['id']) + bracket['points']
            leaderboardEntry['tiebreaker'] = bracket['tiebreaker']
            leaderboard.append(leaderboardEntry)
    return sorted(leaderboard, key=lambda i: i['points'], reverse=True)


def getDistributionsOfPickedGame(game):
    counts = dict()
    with open(
            'data/brackets.json') as data:
        brackets = json.load(data)
    for bracket in brackets:
        if bracket[game] in counts:
            counts[bracket[game]] += 1
        else:
            counts[bracket[game]] = 1
    return counts


def getMostCommonTeam(distribution):
    count = 0
    winner = ""
    for team in distribution:
        if distribution.get(team) > count:
            count = distribution.get(team)
            winner = team
    return winner


def getDistributionsOfAllGames():
    games = ['afcWildCard1', 'afcWildCard2', 'afcWildCard3', 'nfcWildCard1',
             'nfcWildCard2', 'nfcWildCard3', 'afcDivisional1', 'afcDivisional2',
             'nfcDivisional1', 'nfcDivisional2', 'afcChampions', 'nfcChampions', 'superbowl']
    distributions = dict()
    for game in games:
        distributions[game] = getDistributionsOfPickedGame(game)

    return distributions


def updateScores():
    brackets = dict()
    winners = dict()
    games = ['afcWildCard1', 'afcWildCard2', 'afcWildCard3', 'nfcWildCard1',
             'nfcWildCard2', 'nfcWildCard3', 'afcDivisional1', 'afcDivisional2',
             'nfcDivisional1', 'nfcDivisional2', 'afcChampions', 'nfcChampions',
             'superbowl']
    points = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 6, 6, 12]
    with open(
            'data/original_brackets.json') as data:
        brackets = json.load(data)
    with open(
            'data/perfectbracket.json') as data:
        winners = json.load(data)

    for bracket in brackets:
        counter = 0
        bracket['points'] = 0
        for game in games:
            if winners[game] == bracket[game]:
                bracket['points'] += points[counter]
            counter += 1
        print(bracket['name'] + ': ' + str(bracket['points']))

    with open('data/brackets.json', 'w') as fout:
        json_dumps_str = json.dumps(brackets, indent=4)
        print(json_dumps_str, file=fout)


def getRemainingPointsPossible(id):
    games = ['superbowl']
    points = [12]
    teams = ['Cincinnati Bengals',
             'Los Angeles Rams']
    possiblePoints = 0
    with open('data/brackets.json') as data:
        brackets = json.load(data)
    for bracket in brackets:
        if(bracket['id'] == id):
            for game in games:
                if bracket[game] in teams:
                    possiblePoints += points[games.index(game)]
    return possiblePoints

# print(sortLeaderboardHighToLow())


def alternativeScoring():
    winners = {'WildCard': ['Bills', 'Buccaneers', 'Saints', 'Ravens', 'Browns', 'Rams'],
               'Divisional': ['TBD', 'TBD', 'TBD', 'TBD'],
               'Champions': ['TBD', 'TBD'],
               'superbowl': ['TBD']
               }
    games = {'WildCard': ['afcWildCard1', 'afcWildCard2', 'afcWildCard3', 'nfcWildCard1',
                          'nfcWildCard2', 'nfcWildCard3'],
             'Divisional': ['afcDivisional1', 'afcDivisional2',
                            'nfcDivisional1', 'nfcDivisional2'],
             'Champions': ['afcChampions', 'nfcChampions'],
             'superbowl': ['superbowl']
             }
    points = {'WildCard': 2,
              'Divisional': 3,
              'Champions': 6,
              'superbowl': 12
              }
    with open(
            'data/brackets.json') as data:
        brackets = json.load(data)
    for bracket in brackets:
        bracket['points'] = 0
        for round in winners:
            for game in games[round]:
                if bracket[game] in winners[round]:
                    print(round + ": " + bracket[game] + " W")
                    bracket['points'] += points[round]
                else:
                    print(round + ": " + bracket[game] + " L")

    with open('data/brackets.json', 'w') as fout:
        json_dumps_str = json.dumps(brackets, indent=4)
        print(json_dumps_str, file=fout)


print(getRemainingPointsPossible(3866))
