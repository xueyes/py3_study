import random
import  time
print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())

def roll_dice(numbers=3,points=None):
    print('<<<<<ROLL THE DICE ！>>>>>')
    if points is  None:
         points = []
    while numbers >0:
            point = random.randrange(1,7)
            points.append(point)
            numbers = numbers - 1
    return  points

def roll_result(total):
    isBig = 11 <=total <=18
    isSmall = 3 <= total <=10
    if isBig:
        return 'Big'

    elif isSmall:
        return 'Small'



def start_game():
    print("<<<<<<GAME STARTS !!>>>>>>>")
    choices  = ['Big','Small']

    your_choice = input('Big or Small :')

    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:

            print('The points are',points,'you Win  !')
            time.sleep(10)

        else:

            print('The points are',points,'you Lose  !')
            time.sleep(10)
    else:
        print('Invalid word')
        start_game()
start_game()