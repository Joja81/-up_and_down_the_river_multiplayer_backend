from flask import current_app as app
from app.functions.game import next_play, prepare_new_round
import time

from app.models import Game, Play

def check_db():
    with app.app_context():
        # Checking for plays to start
        plays = Play.query.filter(Play.round_status == "w", Play.wait_end <= time.time()).all()
        
        for play in plays:
            play.round_status = "f"
            next_play(play.game_id, play.round_id) 
        
        #check for new rounds
        games = Game.query.filter(Game.game_stage == "R", Game.new_round_time <= time.time()).all()
        
        for game in games:
            prepare_new_round(game.id)