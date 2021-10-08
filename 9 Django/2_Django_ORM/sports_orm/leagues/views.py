from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_league": League.objects.filter(sport='Baseball'),
		"womens_league":League.objects.filter(name__contains='Womens'),
		"hockeys_league":League.objects.filter(sport__contains='Hockey'),
		"no_football_league":League.objects.exclude(sport='Football'),
		"conference_league":League.objects.filter(name__contains='Conference'),
		"atlantic_league":League.objects.filter(name__contains='Atlantic'),
		"dallas_teams":Team.objects.filter(location='Dallas'),
		"raptor_teams":Team.objects.filter(team_name='Raptor'),
		"city_teams":Team.objects.filter(location__contains='City'),
		"t_teams":Team.objects.filter(team_name__startswith='T'),
		"teams_order_by_location": Team.objects.all().order_by('location'),
		"teams_order_by_name": Team.objects.all().order_by('-team_name'),
		"player_cooper": Player.objects.filter(last_name='Cooper'),
		"player_joshua": Player.objects.filter(first_name='Jaxon'),
		"player_cooper_no_joshua": Player.objects.filter(last_name='Cooper').exclude(first_name='Jaxon'),
		"player_alexander_or_wyatt": Player.objects.filter(first_name='Alexander') | Player.objects.filter(first_name='Wyatt'),
		#"all_teams_Atlantic_Soccer_Conference":Team.objects.filter(league=League.objects.get(name="Atlantic League of Ice Hockey")),
		#"all_players_for_team":Player.objects.filter(curr_team=Team.objects.get(team_name="Hustlers")),
		#"all_players_for_league":Player.objects.filter(curr_team__in=Team.objects.filter(league=League.objects.get(name="Atlantic League of Ice Hockey"))),#""" se utiliza __in para hacer un filter anidado en otro filter y no utilizar get()"""
		#"all_players_for_league_last_name":Player.objects.filter(last_name="Lee",curr_team__in=Team.objects.filter(league=League.objects.get(name="Atlantic League of Ice Hockey"))),
		#"all_players_for_Football":Player.objects.filter(curr_team__in=Team.objects.filter(league__in=League.objects.filter(sport="Football"))),
		#"all_teams_with_player_name":Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia")),
		#"all_leagues_with_player_name":League.objects.filter(teams__in=Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia"))),
		#"all_players_last_name_exclude_team":Player.objects.filter(last_name="Lopez",curr_team__in=Team.objects.exclude(team_name="Roughriders")),
		#"all_teams_evans":Team.objects.filter(all_players__in=Player.objects.filter(first_name="Ethan",last_name="Rogers")),
		#"all_players_team":Player.objects.filter(all_teams__in=Team.objects.filter(team_name="Rough Riders")),
		#"past_all_players_team":Player.objects.filter(all_teams__in=Team.objects.filter(team_name="Rough Riders"),curr_team__in=Team.objects.exclude(team_name="Rough Riders")),
		#"all_teams_coleman_sophia":Team.objects.filter(all_players__in=Player.objects.filter(first_name="Sophia",last_name="Coleman")).exclude(team_name="Hornets"),
		#"all_player_past_league":Player.objects.filter(first_name="Ethan", all_teams__in=Team.objects.filter(league=League.objects.get(name="Atlantic League of Ice Hockey"))),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")