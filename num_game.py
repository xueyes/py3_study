#coding:utf8
import random
import  time
print ("Start : %s" % time.ctime())
time.sleep( 2 )
print ("End : %s" % time.ctime())



def roll_dice(numbers=3,points=None):
    print('<<<<<ROLL THE DICE(摇骰子)>>>>>')
    if points is  None:
         points = []
         Bets = 1000
    while numbers >0:
            point = random.randrange(1,7)
            points.append(point)
            numbers = numbers - 1
    return  points

def roll_result(total):
    isBig = 11 <=total <=17
    isSmall = 3 <= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    your_money = 1000
    while your_money >0:
        print("<<<<<<押大押小GAME STARTS(游戏开始)  Created by xueyes  !!>>>>>>>")
        print("<<<<<<三个骰子总合大于11小于17为大,大于3小于10为小,以下只能输入Big 或者 Small!>>>>>>>")
        time.sleep(2)
        choices  = ['Big','Small']
        your_choice = input('Big or Small(Big大,Small小) :')




        if your_choice in choices:

            your_bet = int(input('How much you wanna bet(你想赌多少钱) :? '))
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)

            if youWin:
                print('The points are',points,'you Win  !')
                print('You gained(增加) {} , you have {} now'.format(your_bet,your_money + your_bet))
                your_money = your_money + your_bet

                time.sleep(3)

            else:

                print('The points are',points,'you Lose  !')
                print('You lost(损失) {}, you have {} now'.format(your_bet,your_money - your_bet))
                print('江南皮革产倒闭了,老板带着小姨子要逃跑了......')

                your_money = your_money - your_bet


                time.sleep(2)
        else:
             print('Invalid word')
    else:

        print('没钱了要好好活着,加油挣钱还债!')

        print('欠债还钱,天经地义!')
        print('Game Over(游戏结束)')

start_game()