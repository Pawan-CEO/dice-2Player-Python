import random

dice={
    'first_username':"unknown",
    'second_username':"unknown",
    'first_value':0,
    'second_value':0,
    'first_won':0,
    'second_won':0,
    'tie':0,
    'turn':1
}
def dice_value():
    return int(random.randint(1,6))

def dice_role():
    value=dice_value()
    if dice['turn']==1:
        dice['first_value']=value
        dice['turn']=2
    else:
        dice['second_value']=value
        dice['turn']=1
def username():
    first_username=input('Enter first user name:\t')
    second_username=input('Enter second user name:\t')
    dice['first_username']=first_username
    dice['second_username']=second_username
    print('----------------------------------------')
def score():
    print("----------------------------------------")
    print(str(dice['first_username'])+"\t|\t"+str(dice['second_username'])+"\t||\t Tie Games")
    print("   "+str(dice['first_won'])+"\t|\t   "+str(dice['second_won'])+"\t||\t   "+str(dice['tie']))
    print("----------------------------------------") 
def compare():
    print("----------------------------------------")
    if dice['first_value']==dice['second_value']:
        dice['tie']+=1
        print('--------------Game Tie--------------')
    elif dice['first_value']>dice['second_value']:
        dice['first_won']+=1
        print("\t\t"+str(dice['first_username'])+" won the match")        
    else:
        dice['second_won']+=1
        print("\t\t"+str(dice['second_username'])+" won the match")        
    dice['first_value']=0
    dice['second_value']=0
    print('------------------------------------------')

print("=============================================")
print("============Play Ludo Game===================")
print("---------------------------------------------")
print("Welcome to game:")
username()

while True:
    print("press 1 -- \t role dice")
    print("press 2 -- \t Score")
    print("press 3 -- \t exit")
    user_input=int(input('selected value is -: '))
    if user_input==1:
        for a in range(0,2):
            if dice['turn']==1:
                print(str(dice['first_username'])+" roles a dice.....")
                dice_role()
                print("\t\t"+str(dice['first_value']))
            elif dice['turn']==2:
                print(str(dice['second_username'])+" roles a dice.....")
                dice_role()
                print("\t\t"+str(dice['second_value']))
        
        compare()

    elif user_input==2:
        score()
    elif user_input==3:
        break
    temp=input('Press Enter to continue')
    print('=========================================')
