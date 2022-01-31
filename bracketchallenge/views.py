from django.shortcuts import render
from django.template import loader, RequestContext
from . import bracket_formatter as brackets
from . import leaderboard_generator

from django.http import HttpResponse
from django import template
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    distributions = leaderboard_generator.getDistributionsOfAllGames()
    superbowl = distributions['superbowl']
    superbowl = dict(
        sorted(superbowl.items(), key=lambda item: item[1], reverse=True))
    afcChampions = distributions['afcChampions']
    afcChampions = dict(sorted(afcChampions.items(),
                               key=lambda item: item[1], reverse=True))
    nfcChampions = distributions['nfcChampions']
    nfcChampions = dict(sorted(nfcChampions.items(),
                               key=lambda item: item[1], reverse=True))
    return render(request, 'index.html', {'superbowl': superbowl,
                                          'afcChampions': afcChampions,
                                          'nfcChampions': nfcChampions})


def leaderboards(request):
    leaderboard = leaderboard_generator.sortLeaderboardHighToLow()
    return render(request, 'leaderboards.html', {"leaderboard": leaderboard})


def update(request):
    if request.method == 'POST':
        if request.POST.get('id_password') == 'kavinEshaan':
            brackets.updatePerfectBracket(
                request.POST.get('game'), request.POST.get('winner'))
            leaderboard_generator.updateScores()
            # brackets.removeGame(request.POST.get('game'))
            # brackets.removeTeam(request.POST.get('loser'))
    games = brackets.getGames()
    teams = brackets.getTeams()
    return render(request, 'update.html', {'games': games,
                                           'teams': teams})


def bracket(request, id):
    number = int(id)
    player_bracket = brackets.generateDisplayBracket(number)
    return render(request, 'bracket.html', {"bracket": player_bracket, })


def perfectbracket(request):
    bracket = brackets.generatePerfectBracket()
    return render(request, 'perfectbracket.html', {'bracket': bracket})


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))
