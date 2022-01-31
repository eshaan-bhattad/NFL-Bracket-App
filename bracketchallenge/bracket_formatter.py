import json


def getPlayerBracket(id):
    with open('data/brackets.json') as data:
        brackets = json.load(data)
        for key in brackets:
            if key['id'] == id:
                return key


def convertBracketToLogos(bracket):
    logos = dict()
    with open(
            'data/logos.json') as data:
        logos = json.load(data)
    teams = list(logos.keys())
    for key in bracket:
        if bracket.get(key) in teams:
            bracket[key] = logos[bracket.get(key)]

    return bracket


def generateDisplayBracket(id):
    return convertBracketToLogos(getPlayerBracket(id))


def generatePerfectBracket():
    bracket = dict()
    with open(
            'data/perfectbracket.json') as data:
        bracket = json.load(data)
    bracket = convertBracketToLogos(bracket)
    return bracket


def getGames():
    games = ['afcWildCard1', 'afcWildCard2', 'afcWildCard3', 'nfcWildCard1',
             'nfcWildCard2', 'nfcWildCard3', 'afcDivisional1', 'afcDivisional2',
             'nfcDivisional1', 'nfcDivisional2', 'afcChampions', 'nfcChampions', 'superbowl']

    return games


def getTeams():
    teams = ['Cincinnati Bengals', 'Buffalo Bills', 'Philadelphia Eagles', 'Tampa Bay Buccaneers', 'San Francisco 49ers',
             'Dallas Cowboys', 'Pittsburgh Steelers', 'Kansas City Chiefs', 'Arizona Cardinals', 'Los Angeles Rams', 'Tennessee Titans', 'Green Bay Packers']

    return teams


def updatePerfectBracket(game, winner):
    bracket = dict()
    with open(
            'data/perfectbracket.json') as data:
        bracket = json.load(data)

    bracket[game] = winner

    with open('data/perfectbracket.json', 'w') as fout:
        json_dumps_str = json.dumps(bracket, indent=4)
        print(json_dumps_str, file=fout)
