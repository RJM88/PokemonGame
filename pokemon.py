import time
import numpy
import sys

# delay printing
def delay_print(s):
    # print one letter at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# pokemon class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
    # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # amount of health

    def fight(self, Pokemon2):
        # allow two pokemon to fight each other.
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+numpy.mean([self.attack, self.defense])))
        print("\nVS")

        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+numpy.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        # consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # both are the same types
                if Pokemon2.types == k:
                    string_1_attack = "\nIts not very effective..."
                    string_2_attack = "\nIts not very effective..."

                # Pokemon2 is strong
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "\nIts not very effective..."
                    string_2_attack = "\nIts super effective!"

                # Pokemon2 is weak
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "\nIts super effective!"
                    string_2_attack = "\nIts not very effective..."

        # fighting will continue why pokemon still has health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"\nGo {self.name}")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # add bars back plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # check to see if pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + " fainted.")
                break

            # pokemon2s turn to attack
            print(f"\nGo {Pokemon2.name}")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # add bars back plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
            print(f"\n{self.name}\t\tHLTH\t{self.health}\n")
            time.sleep(.5)

            # check to see if pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + " fainted.")
                break

        money = numpy.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.")



if __name__ == '__main__':
    # create pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE':8})
    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'ATTACK':6, 'DEFENSE':5})
    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK':4, 'DEFENSE':2})

    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK':10, 'DEFENSE':10})
    Wartortle = Pokemon('Wartortle', 'Water', ['Water Gun', 'Bubblebeam', 'Headbutt', 'Surf'], {'ATTACK':5, 'DEFENSE':5})
    Squirtle = Pokemon('Squirtle', 'Water', ['Tackle', 'Bubblebeam', 'Headbutt', 'Surf'], {'ATTACK':3, 'DEFENSE':3})

    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Whip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK':8, 'DEFENSE':12})
    Ivysaur = Pokemon('Ivysaur', 'Grass', ['Vine Whip', 'Razor Leaf', 'Bullet Seed', 'Leach Seed'], {'ATTACK':4, 'DEFENSE':6})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Whip', 'Razor Leaf', 'Tackle', 'Leach Seed'], {'ATTACK':2, 'DEFENSE':4})

    Charizard.fight(Wartortle)
