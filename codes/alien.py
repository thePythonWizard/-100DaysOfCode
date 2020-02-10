# Game plot
# alien attaked on earth and they killed every starfleet operatives on earth and some of them escaped to moon starfleet base with all the earth alive civilians now you are the only one on the earth and your mission is to activate the nucleur bomb to destroy the earth and leave before bomb explodes.
# Scene : So you walk up and see no one around you and find out that the aliens have captured starfleet newyork base now you will go to to substation and drive the train to nasa but at substation aliens are parametering the trains. you will have to escape from them and board on to the train and drive it by yourself.
# When you reach nasa you are gonna enter a passcode. you will get some hints with 5 chances. if you enter wrong password every single time alarm will buzzed off and aliens will come to know about your location and you will be killed.

# If you get success full in getting inside the nasa hidden base than you will need to take the bomb and place it at the white house because that's the place where alien bosses are with their max fleets as well as their spaceship. then you are gonna theft a spaceship and go to moon base to prepare of future attak on aliens.

# PLots:
"""
Map : current_scene
      next_scene
      opening_scene = 'NewYork Starfleet'
      final_scene = 'Spaceship'

Engine : play

Scene :

    -enter
    * NewYork
    * SubStation
    * NasaBase
    * WhiteHouse
    * SpaceShip()
    * MoonBase
"""
from random import randint
from sys import exit
from textwrap import dedent

class Scene:

    def enter(self):
        print("This scene is not yet configured.")
        print("Implement enter()")
        exit(1)

class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('moon_base')
        print(">>>> current_scene = ", current_scene, ">>>> last_scene = ", last_scene)
        while current_scene != last_scene:

            next_scene_name = current_scene.enter()
            print(">> next_scene_name = ", next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quotes = [
        'You really sucks.',
        'You let aliens captured the earth.',
        'You let starfleet get destroyed.',
        'You were the last lope and you destroyed it.'
    ]
    def enter(self):
        print(Death.quotes[randint(0, 3)])
        exit(1)


class NewYork(Scene):

    def enter(self):

        print(dedent("""
            You woke up see aliens captured everything and starfleet officers have left the earth.with all the civilins and you are the last human alive on this planet now its your mission to destroy their mother ship and return to moon base.
            """))

        print(dedent("""
            You saw aliens approcahing you and you have 3 choices:
            kill them
            hide from them
            jump from the window
            """))
        response = input("> ")

        if response == 'kill them':
            print(dedent("""
                You try to kill them and even kill two of them but last one killed you.
                """))
            return 'death'

        elif response == 'hide from them':
            print(dedent("""
                You try to hide from them but they saw your shadow and shot you down with their laser guns.
                """))
            return 'death'

        elif response == 'jump from the window':
            print("<<<<<<<<<<<<<<<<<<<<<<<<Finally here>>>>>>>>>>>>>>>>>>>>>>>")
            print(dedent("""
                You saw that there is a window behind you you jump through that window before the aliens enterd into office. and you keep going and reach the nearby substation.
                """))
            print('sub_station')
            return 'sub_station'

class SubStation(Scene):

    def enter(self):
        print("""
            Reach and pic a laser gun.
            reach to the train.
            """)
        print(dedent("""
            You have 3 shots in your gun.
            but 4 aliens are guarding a train.
            """))
        right_aliens_killed = [str(randint(1, 2)), str(randint(3, 4)), str(randint(5, 6))]
        print(right_aliens_killed)

        killed_aliens = list(input("> Enter alien with their tag you killed.."))

        if right_aliens_killed == killed_aliens:
            print(dedent("""
                last aliens didn't saw you and you can now board the train and go to nasa.
                """))
            return 'nasa_base'
        else:
            print(dedent("""
                Last alien saw you and killed you with his laser gun
                """))
            return 'death'


class NasaBase(Scene):

    def enter(self):
        print(dedent("""
            You are at the secret gate of nasa and gurads are all around you now you have only five chance to enter code to enter inside base if you get wrong more than 5 times alarm will go on and aliens will surround you and kill you.
            """))

        correct_code = int(f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}")
        print(correct_code)
        passcode = int(input("> [PassCode plz: ] "))
        guesses = 0
        while passcode != correct_code and guesses < 5:
            guesses += 1
            passcode = input("> [PassCode plz: ] ")
            print(passcode)

        if passcode == correct_code:
            print("You are entering into nasa base")
            print("""
                you picked up the nuclear bomb and now moving to white house to plant the nuclear bomb.
                """)
            return 'white_house'
        else:
            print(dedent("""
                Alarm goes on as you enterd passcode 5 times wrong. alien surrounded you and killed you.
                """))
            return 'death'

class WhiteHouse(Scene):

    def enter(self):
        print(dedent("""
            You planted the bomb and now moving to the spaceship to get to the starfleet moon base.
            """))
        return 'space_ship'

class SpaceShip(Scene):

    def enter(self):
        print(dedent("""
            You caught starship and now moving to your moon base.
            """))
        return 'moon_base'

class MoonBase(Scene):

    def enter(self):
        print(dedent("""
            You can see white house blowing as you are moving to Your office on moon to prepare to return to earth and capture it away from alien again.
            """))
        print("You won now celebrate your winning")


class Map:
    scenes = {

        'newyork_starfleet': NewYork(),
        'sub_station': SubStation(),
        'nasa_base': NasaBase(),
        'white_house': WhiteHouse(),
        'space_ship': SpaceShip(),
        'moon_base': MoonBase(),
        'death': Death()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('newyork_starfleet')
a_game = Engine(a_map)
a_game.play()
