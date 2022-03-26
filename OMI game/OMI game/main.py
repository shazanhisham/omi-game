import random
import game.dividing_cards
import game.game_play
trick=1
mark_robot=0
mark_user=0


game_cards=["7\u2663","8\u2663","9\u2663","10\u2663","J\u2663","Q\u2663","K\u2663","A\u2663","7\u2666","8\u2666","9\u2666","10\u2666","J\u2666","Q\u2666","K\u2666","A\u2666","7\u2660","8\u2660","9\u2660","10\u2660","J\u2660","Q\u2660","K\u2660","A\u2660","7\u2665","8\u2665","9\u2665","10\u2665","J\u2665","Q\u2665","K\u2665","A\u2665"]
random.shuffle(game_cards)
user_cards,robot_cards,trump=game.dividing_cards.user(game_cards)
game.game_play.start(user_cards,robot_cards,trump,trick)
        

