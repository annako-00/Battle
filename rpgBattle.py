print('Welcome')
print()
print()

story='The hero one day wake up early in the morning to go buy a newly released game series,he was walking alone then a truck came and beat him and he died.The hero then got a chance to meet a god who asked him "did you have any regrets" and he replied "yes i wanted atleast 1 time to play the game that i just bought".The god then reincarnated him in the game world for him to play the game.The hero woke up and see a world that is similar to the world in the game he wanted to play.He started to live in the world to know that world is working-the system,The hero is reborn as afighter.One day the dragons came out of its nest to eat the people that live in the world,the hero then proceeds to fight one of the dragons'
print(story)
print()
print()

print('Do you want to play the game ?')
try:
        start=input('y/n  ')
        print()   
except ValueError:
     print("please enter 'y' or 'n'")

if start=='y':
        
              name=input('enter your name  ')
              print()
        
else:
     print('exited')
     quit()




class Character():
    def __init__(self,name,health,weapon) -> None:
        self.name=name
        self.health=health
        self.healthmax=health
        

        self.weapon=weapon
    
    def attack(self,target)->None:
        target.health-=self.weapon.damage
        target.health=max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self,name, health,weapon) -> None:
        super().__init__(name, health,weapon)

class Enemy(Character):
    def __init__(self, name, health,weapon) -> None:
        super().__init__(name, health,weapon)
    

class Weapon:
    def __init__(self,name,type,damage,value) -> None:
        self.name=name
        self.type=type
        self.damage=damage
        self.value=value

sword=Weapon('Excalibur','Sharp iron',10,10)

fire=Weapon('Fire Blast','fire',15,10)


player=Hero(name,100,sword)
enemy=Enemy('Dragon',100,fire)

while True:
    player.attack(enemy)
    enemy.attack(player)

    print(f"Health of {player.name} is {player.health}")
    print(f"Health of {enemy.name} is {enemy.health}")

    
    input()
    
        
           

    
    if player.health==0:
        print('You Lose')
        print()
        print()
        print('Game Over')
        print()
        break
    elif enemy.health==0:
        print('You Win')
        break 
