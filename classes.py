#!/usr/bin/env python3
from sys import exit
from random import randint

class Scene():

    def enter(self):
        print("This scene is not yet configured. Subclass it and implelent enter().")
        exit(1)

class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    def enter(self):
        print("You have died! Better luck next time asshole!")
        play_again()


class CentralCorridor(Scene):
 
    def enter(self):
        print("you have entered the Central Corridor! Beware!")
        print("you have the following options...choose wisely!")
        print("Shoot, tell a joke, run")
        print("what will it be?")
        print("1. shoot")
        print("2. run")
        print("3. tell a joke")
       

        action = input("> ")

        if action == '1' or action == '2':
            return 'death'
        elif action == '3':
            return 'laser_weapon_armory'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You have entered the Laser Weapon Armory! Beware!")
        print("you msut enter a code to escape!")
        print("it is a 3 digit code! if you are really stuck maybe if you were l33t you would figure it out!")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        cheat_code = '1337'
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            if  guess != cheat_code:
                print("Bzzzed!")
            if guess == cheat_code:
                 print("well arent you smart...here is the code!\nCode: " + code)
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            return 'the_bridge'

        

class TheBridge(Scene):

    def enter(self):
        print("You have entered the endless bridge! Beware!")
        return 'escape_pod'

class Finished(Scene):

    def enter(self):
        print("You have escaped good luck to you out in the galaxy!")
        play_again()
        

class EscapePod(Scene):

    def enter(self):
        print("You have entered the escape pod!")
        print("There are 5 pods but only one is good! you must decide which one!")
        good_pod = randint(1,5)
        print(good_pod)
        cheat_code = '1337'
        guess = input("[Pod #]> ")

        if int(guess) != good_pod:
            print("you jumped into pod %s and hit the eject button." % guess)
            return 'death'
        else:
            print("you jump into pod %s and hit the eject button." % guess)
            return 'finished'


class Map():

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death' : Death(),
            'finished': Finished()
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)


    def opening_scene(self):
        return self.next_scene(self.start_scene)


def play_again():
    print("would you like to play again?")
    print("Yes or No?")
    answer = input("> ")
    if answer == 'y':
        a_game.play()
    else:
        exit()

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()








