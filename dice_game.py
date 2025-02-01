import random

def roll():
    
    roll=random.randint(1,6)
    return roll

print("GAME RULES\n")
print("1. if you roll a 1 you are out\n")
print("2. if you score above 50 you win!\n")
print("3. otherwise highest scoring player is the winner!\n")
  

while bool:    
    num_players=int(input("enter the ammount of player (2-6) "))
    if num_players<2 or num_players>6:
        print("enter players between 2 and 6\n")
        bool=True
    else:
        bool=False

players=[]

for i in range(num_players):
    name=input(f"\nenter name of player {i+1}: ")
    players.append({"name": name,"score":0})
    

      

for player in players:
    bool=True
    total=0
    while bool:
      
        y=input(f"\n{player['name']} do you want to roll the dice? y/n \n")

        if y=='y':
            x=roll()
            if x==1:
                print("oops! you rolled a 1! game over\n")
                
                
                break
        
            else:
                print("you rolled: ",x) 
               
                player['score']=x
                total=total+player['score']
                
                
                print("total score: ",total)
                if total>=50:
                    print(f"CONGRATULATIONS {player['name']}YOU WON!\n")
                    break
               
        
            
        elif y=='n':
            print("your score is ",total)
            player['score']=total
            bool=False
            break
            


winner=max(players,key=lambda x:x['score'])

print(f"CONGRATULATIONS! {winner['name']}! YOU WON!\n")

print(players)


            

