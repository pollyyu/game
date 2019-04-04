
from textwrap import dedent

class Scene(object):
    pass

class EndGame(Scene):
    def enter(self):
        print(dedent("""
        This is not ideal. You die too young and without any loved ones.

        Heck, you don't even know if you have any loved ones"""))

        return 'next_season'

class NextSeason(Scene):
    def enter(self):
        print(dedent("""
        You discover you have super powers. Wow, what a great origin story. You're glad no one died in this origin story. But you're not sure how the future looks like.

        You're nervous, but at the same time you're excited. You cannot wait for the adventures ahead with this strange man you just met. Maybe there's an entire squad you can be part of.
        """))

    # return 'end_game'

class Opening(Scene):
    def enter(self):
        print(dedent("""
        You wake up in a room with no memory how you got there. You try to open the door but it is locked.
        """))

        return 'end_game'
