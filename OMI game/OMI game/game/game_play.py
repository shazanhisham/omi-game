import random

def robot_trick_checking_result (user_trick_card,robot_trick_card,trump):
        robot_count=0
        user_count=0
        robot_mark=0
        user_mark=0
        win=""
        precedence_order=["7","8","9","10","J","Q","K","A"]
        if user_trick_card[-1]==robot_trick_card[-1]:
                for i in range(len(precedence_order)):
                        if precedence_order[i] == user_trick_card[0:(len(user_trick_card)-1)]:
                                user_count=i
                        elif precedence_order[i] == robot_trick_card[0:(len(robot_trick_card)-1)]:
                                robot_count=i
                if robot_count>user_count:
                        print("Robot wins +2")
                        robot_mark+=2
                        win="robot"
                else:
                        print("You wins +2")
                        user_mark+=2
                        win="user"
        elif  user_trick_card[-1]!=robot_trick_card[-1]:
                if user_trick_card[-1]==trump:
                        print("You wins +2")
                        user_mark+=2
                        win="user"
                elif robot_trick_card[-1]==trump:
                        print("Robot wins +2")
                        robot_mark+=2
                        win="robot"
                else:
                     print("Robot wins +2")
                     robot_mark+=2
                     win="robot"
        return(robot_mark,user_mark,win)

def user_trick_checking_result (user_trick_card,robot_trick_card,trump):
        robot_count=0
        user_count=0
        robot_mark=0
        user_mark=0
        precedence_order=["7","8","9","10","J","Q","K","A"]
        if user_trick_card[-1]==robot_trick_card[-1]:
                for i in range(len(precedence_order)):
                         if precedence_order[i] == user_trick_card[0:(len(user_trick_card)-1)]:
                                user_count=i
                         elif precedence_order[i] == robot_trick_card[0:(len(robot_trick_card)-1)]:
                                robot_count=i
                if robot_count>user_count:
                        print("Robot wins +2")
                        robot_mark+=2
                        win="robot"
                else:
                        print("You wins +2")
                        user_mark+=2
                        win="user"
        elif  user_trick_card[-1]!=robot_trick_card[-1]:
                if user_trick_card[-1]==trump:
                        print("You wins +2")
                        user_mark+=2
                        win="user"
                elif robot_trick_card==trump:
                        print("Robot wins +2")
                        robot_mark+=2
                        win="robot"
                else:
                     print("User wins +2")
                     user_mark+=2
                     win="user"
        return(robot_mark,user_mark,win)
               
        

def robot_chance (user_cards,robot_cards,trump,trick):
        signs_of_user_valid_cards=[]
        user_choice=0
        robot_choice=0
        robot_trick_card=0
        user_trick_card=0
        
        print("Trick : ",trick)
        print("Trump suit : ",trump)
        print("Your hand in : ",end="")
        for i in range(len(user_cards)):
                print("("+(str(i+1))+")",user_cards[i],end=" ")

        robot_choice=random.randrange(0,len(robot_cards))
        print("\nRobot suits : ",robot_cards[robot_choice])
        robot_trick_card=robot_cards[robot_choice]
        del robot_cards[robot_choice]

        for i in user_cards:
                        if i[-1]==robot_trick_card[-1]:
                                signs_of_user_valid_cards.append(i[-1])
        
        while True:
                try:
                        user_choice=int(input("User suits : "))
                        if user_choice<9 and (user_cards[user_choice-1][-1] in signs_of_user_valid_cards):
                                user_trick_card=user_cards[(user_choice-1)]
                                del user_cards[(user_choice-1)]
                                del signs_of_user_valid_cards[0]
                                break
                        elif user_choice<9 and (len(signs_of_user_valid_cards)==0):
                                user_trick_card=user_cards[(user_choice-1)]
                                del user_cards[(user_choice-1)]
                                break
                        else:
                                print("Invalid choice. Try again")
                                        

                           
                except:
                        print("Invalid choice. Try again")

        robot_mark,user_mark,win=robot_trick_checking_result(user_trick_card,robot_trick_card,trump)
        return(robot_mark,user_mark,win,user_cards,robot_cards)
        

def user_chance(user_cards,robot_cards,trump,trick):
        signs_of_robot_valid_cards=[]
        user_choice=0
        robot_choice=0
        robot_trick_card=0
        user_trick_card=0

        print("Trick : ",trick)
        print("Trump suit : ",trump)
        print("Your hand in : ",end="")
        for i in range(len(user_cards)):
                print("("+(str(i+1))+")",user_cards[i],end=" ")

        while True:
                try:
                        user_choice=int(input("\nYour choice : "))
                        while True:
                                if user_choice-1<len(user_cards):
                                        break
                                else:
                                        print("Invalid choice. Try again",end="")
                                        user_choice=int(input("\nYour choice : "))
                        break
                                        
                except:
                        print("Invalid choice. Try again",end="")
                        
        print("Your suits : ",user_cards[user_choice-1])
        user_trick_card=user_cards[user_choice-1]
        del user_cards[user_choice-1]

        for i in robot_cards:
                        if i[-1]==user_trick_card[-1]:
                                signs_of_robot_valid_cards.append(i[-1])

        while True:
                robot_choice=random.randrange(0,len(robot_cards))
                if robot_cards[robot_choice][-1]==user_trick_card[-1]:
                        print("Robot suits : ",robot_cards[robot_choice])
                        robot_trick_card=robot_cards[robot_choice]
                        del robot_cards[robot_choice]
                        break

                elif len(signs_of_robot_valid_cards)!=0:
                        continue

                elif len(signs_of_robot_valid_cards)==0:
                        print("Robot suits : ",robot_cards[robot_choice])
                        robot_trick_card=robot_cards[robot_choice]
                        del robot_cards[robot_choice]
                        break

        robot_mark,user_mark,win=user_trick_checking_result(user_trick_card,robot_trick_card,trump)
        return(robot_mark,user_mark,win,user_cards,robot_cards)
        
                             
def start (user_cards,robot_cards,trump,trick):
        print("\nLets play\n")
        trick=trick
        for i in range(8):
                if trick == 1 or win == "robot":
                         robot_mark,user_mark,won_player,reamine_user_cards,remaine_robot_cards=(robot_chance(user_cards,robot_cards,trump,trick))
                         user_cards=[]
                         robot_cards=[]
                         user_cards=user_cards+reamine_user_cards
                         robot_cards=robot_cards+remaine_robot_cards
                         win=won_player
                         trick+=1
                         print("\n",end="")
                else:
                         win == "user"
                         robot_mark,user_mark,won_player,reamine_user_cards,remaine_robot_cards=(user_chance(user_cards,robot_cards,trump,trick))
                         user_cards=[]
                         robot_cards=[]
                         user_cards=user_cards+reamine_user_cards
                         robot_cards=robot_cards+remaine_robot_cards
                         win=won_player
                         trick+=1
                         print("\n",end="")
                 

