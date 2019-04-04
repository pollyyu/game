from sys import exit
from random import randint

from game_scenes import *

class Engine(object):
    def __init__(self, scene_map):
        # current_scene =
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('end_game')
        # EndGame.enter(self)
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        last_scene.enter()


class Map(object):
    scenes = {
    'end_game': EndGame(),
    'opening': Opening(),
    'next_season': NextSeason()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)




a_map = Map('opening')
a_game = Engine(a_map)
a_game.play()
# Map('opening').opening_scene()
