
from textwrap import dedent

class Scene(object):
    pass

class EndGame(Scene):
    def enter(self):
        input("")
        print(dedent("""
        This is not ideal. You die too young and without any loved ones.

        Heck, you don't even know if you have any loved ones"""))
        exit(1)
class NextSeason(Scene):
    def enter(self):
        input("")
        print(dedent("""
        You're nervous, but at the same time you're excited. Whatever your future holds for you, you can't wait.

        But you do have to wait, because it's only coming out next season.

        SEE YOU SOON!

                （ ͡° ͜ʖ ͡°)つ━☆・*。
        ⊂　　 ノ 　　　・゜+.
        　しーＪ　　　°。+ ´¨)
        　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)
        　　　　　　　　　　(¸.·´ (¸.·' ☆ ABRA KADABRA...
        """))

        exit(1)
    # return 'end_game'

class Opening(Scene):
    def enter(self):
        print(dedent("""
        You wake up in a room with no memory how you got there. You try to open the door but it is locked.
        """))
        input("Press enter to continue")
        print(dedent("""
        You have three options to choose from:

        1) You bang the door and call for help hoping someone will open the door
        """))
        input("")
        print("2) You search around the room for a vent, perhaps you can escape there")
        input("")
        print("3) You look around the room for something to pick the lock. You can't remember anything, so perhaps you have some unknown skill of picking a lock")

        action = input("Which option will you choose? > ")
        if action == "1":
            print(dedent("""
            You bang the door and call for help. Some strange men with masks come in. You get knocked out. You don't know what happens next because you die.
            """))
            return 'end_game'
        elif action == "2":
            return 'vent'
        elif action == "3":
            print(dedent("""
            You did find a hair clip and try to pick the lock. You try for 5 minutes and nothing happens. Now you know - you definitely do not have special lock-picking skills.

            Let's try again, you silly person
            """))
            return 'opening'
        else:
            print(dedent("""
            Does not compute! try again.
            """))
            input("")
            return 'opening'

class Vent(Scene):
    def enter(self):
        print(dedent("""
        There are 2 vents which seem easy enough to disassmble:

        1) one at the far back of the room
        2) one closer to bed you woke up on.

        Both seem easy to disassemble. Which do you enter?
        """))

        action = input(">")

        if action == "1":
            print(dedent("""
            You crawl through the vent for what seems like hours. But as you persist and make turns according to your guy, you see some light at the end of the tunnel. Like literally.

            You approach a clear field."""))

            return 'escape'

        elif action == "2":
            print(dedent("""
            You go down the vent. You hear some people mumble. The next thing you know you hear gunshots through the vent. One hits you right at the chest and you die
            """))
            return 'end_game'
        else:
            print("Does not compute")
            return 'vent'

class Escape(Scene):
    def enter(self):
        print(dedent("""
        As you step out in the clear field you decide to:

        1) Walk by the freeway. Maybe you can get some help from passing cars
        2) Wander around the forest area a little more, trying to steer away from the freeway.

        """))

        action = input("> ")

        if action == "1":
            return 'driven'
        elif action == "2":
            return 'bar'
        else:
            print("does not compute please try again")
            return 'escape'

class Driven(Scene):
    def enter(self):
        print(dedent("""
        You walk down the street and try to hail down a car.

        A man in a truck stops and offers a seat.

        You:
        1) Get into his car. Heck, you're tired
        2) Gives him the middle x%*&x. You aren't risking your life especially after getting your freedom"""))

        action = input("> ")

        if action == "1":
            return 'facility'
        elif action == "2":
            print("As you walk further along the freeway, some men in a strange car slow down the car. You are shot.")
            return 'end_game'
        else:
            print("does not compute please try again")
            return 'driven'

class Facility(Scene):
        def enter(self):
            print(dedent("""
            You are driven through what seems like a private institutional facility. The car pulls over to the only building in sight. It is white. And you are suspicious.

            What do you do?

            1) You get out of the car and start running for what you think is your life
            2) Heck, you're tired. You're just going to wait in the car.
            """))

            action = input("> ")

            if action == "1":
                return 'unscrabble'
            elif action == "2":
                return 'clones'
            else:
                print("does not compute please try again")
                return 'facility'

class Unscrabble(Scene):
        def enter(self):
            print(dedent("""
            As you run towards the gate you see that it is locked. But there is a pad, which you perhaps can use to open the gate. It says: unscramble these letters to make the longest word:

            "ictdwal"
            """))

            words = 'wildcat'
            answer = input("> ")
            times = 1
            while times <= 2 and answer != words:
                print("Wrong, please try again")
                times += 1
                answer = input("> ")

            if answer == words:
                print("Good job, you got it! The door is opened and you run back to the freeway as fast as you can.")
                input("")
                print("As you run out of the facility, you see a floral, bright colorful bus. The bus stops and compliments your hospital outfit. They invite you in. You think they are high.")
                input("")
                print("But you figured you could get high too and it's probably more fun to have adventures with them.")

                return 'next_season'
            else:
                print("You failed 3 times here and probably way more in your sad life. You are shot at the back")

                return 'end_game'

class Clones(Scene):
        def enter(self):
            print(dedent("""
            You wait in the car and start seeing a group of people who look exactly like you. This is weird.
            """))
            input("")
            print("You think: maybe you are a clone. But perhaps it's not such a bad thing. Perhaps you and your clones can fight some crime together, afterall there is probably no attachment to family and family expectation to meet. That becomes a huge relief, because you realize you are Asian.")
            input("")
            print("You step out, and are ready to embrace your lookalike siblings for the next adventure")
            return 'next_season'

class Bar(Scene):
    def enter(self):
        print(dedent("""
        You find some clothes left to hang dry outside the house. No one is there so you decide to change. After all, you are in some strange surgery type clothes. A little girl comes by and points at you.

        What do you do?

        1. You run
        2. You approach her nicely
        """))

        action = input("> ")

        if action == '1':
            return 'drinks'
        elif action == '2':
            return 'cat_question'
        else:
            print("Does not compute! Please try again")
            return 'bar'

class CatQuestion(Scene):
    def enter(self):
        print(dedent("""
                As you approach her she asks: What do you call a group of unorganized cats? (you have 3 tries).

              ,/|         _.--''^``-...___.._.,;
             /, \'.     _-'          ,--,,,--'''
            { \    `_-''       '    /}
             `;;'            ;   ; ;
         ._.--''     ._,,, _..'  .;.'
          (,_....----'''     (,..--''

                """))


        word = 'cat-astrophe'
        times = 1
        answer = input("> ")

        while word != answer and times <3:
            print("wrong, please try again")
            answer = input("> ")
            times += times

        if answer == word:
            print(dedent("""
            You pass and you are free to walk down to town nearby.
            """))
            input("> ")
            print(dedent("""
            As you walk along the path to the freeway, you see a few cats playing on the fence.

                                 *     ,MMM8&&&.            *
                                      MMMM88&&&&&    .
                                     MMMM88&&&&&&&
                         *           MMM88&&&&&&&&
                                     MMM88&&&&&&&&
                                     'MMM88&&&&&&'
                                       'MMM8&&&'      *    _
                              |\___/|                      \\
                             =) ^Y^ (=   |\_/|              ||    '
                              \  ^  /    )a a '._.---- --.  //
                               )=*=(    =\T_= /    ~  ~  \//
                              /     \     `"`\   ~   / ~  /
                              |     |         |~   \ |  ~/
                             /| | | |\         \  ~/- \ ~\
                             \| | |_|/|        || |  // /`
                         _/\_//_// __//\_/\_/\_((_|\((_//\_/\_/\_
                      |  |  |  | \_) |  |  |  |  |  |  |  |  |  |
                      |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
                      |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
                      |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
                      |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

            """))
            input("")
            return 'drinks'
        else:
            print("You tried too many times and fail. The answer is: a cat-astrophe")
            return 'end_game'
class Drinks(Scene):
    def enter(self):
        print("You walk further down and see a town nearby. You walk into a bar and order a drink even though you do not have any cash")

        print(dedent("""
        A bald dark man comes by and sits next to you. He offers to buy you that drink.

        1. You take his offer
        2. You reject his offer
        """))
        action = input("> ")

        if action == '1':
            return 'code'
        elif action == '2':
            print("if you can't pay for this drink , you should get out.")
            input("")
            print("So you walk outside of the bar.")
            input("")
            print("as you walk out, some random people who pull out of their dark mustangs and shoot you. ")
            return 'end_game'
        else:
            print("does not compute. Please try again")
            return 'drinks'

class Code(Scene):
    def enter(self):
        print(dedent("""
        The strange man than asks you, hey can you help remember this passcode?

        38w4skvais2all2400fcka336cq2rjajnvaiwoesdfaseb95 """))

        input("")
        print(" <( ͡° ͜ʖ ͡°)> <( ͡° ͜ʖ ͡°)> ")
        input("")
        answer = input("passcode is: ")
        passcode = '38w4skvais2all2400fcka336cq2rjajnvaiwoesdfaseb95'
        if answer == passcode:
            print("Amazingly, you remember everything.")
            input("")
            print("You didn't think you had super powers, but maybe you do.")
            input("")
            print("This looks like the start of a super interesting superhero origin story.")
            return 'next_season'
        else:
            print(dedent("""
            Wow you can't even remember that? All you had to do was copy and paste.

            ಠ_ಠ

            The bald man pulls out a gun and shoots you
            """))
            return 'end_game'
