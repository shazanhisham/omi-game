import random

def selecting_trump():
        global trump
        trump=0
        while True:
                        try:
                                trump=int(input("Please enter the trump suit: "))
                                if trump==1:
                                        trump=user_cards[0][-1]
                                        break
                                elif trump==2:
                                        trump=user_cards[1][-1]
                                        break
                                elif trump==3:
                                        trump=user_cards[2][-1]
                                        break
                                elif trump==4:
                                        trump=user_cards[3][-1]
                                        break
                                else:
                                        print("Invalide choice. ",end="")
                        except:
                                print("Invalide choice. ",end="")
        return

def user(game_cards):
        global user_cards
        global robot_cards
        user_cards=[]
        robot_cards=[]
        print("\nWelcome to OMI")
        print("You are responsible to choose the trump suit")
        for i in range(4):
                if i<3:
                        print("("+str(i+1)+")",game_cards[i],end=",")
                        user_cards.append(game_cards[i])
                else:
                        print("("+str(i+1)+")",game_cards[i])
                        user_cards.append(game_cards[i])
                        selecting_trump()

        for i in range(4,8):
                if i<3:
                        user_cards.append(game_cards[i])
                else:
                        user_cards.append(game_cards[i])

        for i in game_cards[8:16]:
                robot_cards.append(i)
        return user_cards,robot_cards,trump





