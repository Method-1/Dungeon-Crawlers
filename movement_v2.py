from DungeonWorld import DungeonMap
from pickle_menu import *
from monster_treasure import *
from fight_adi import *


class Movement:
    def __init__(self, startzone, endzone):
        self.start = (startzone[0], startzone[1])
        self.goal = endzone
        self.player = startzone
        self.walls = (0, 0)
        self.clean = ("\n" * 100)
        self.banana = 0


    def move_player(self, d, startzone, mapsize, a, in_game_char, all_obj):
        x = self.player[0]
        y = self.player[1]
        pos = startzone

        if d == 'd':
            pos = (x + 1, y)
            banner_text("You move to the right...\n")

        elif d == 'a':
            pos = (x - 1, y)
            banner_text("You move to the left...\n")

        elif d == 'w':
            pos = (x, y - 1)
            banner_text("You take the stairs up...\n")

        elif d == 's':
            pos = (x, y + 1)
            banner_text("You take the stairs down...\n")

        else:
            pos = self.player

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print(self.clean)
            banner_text("You have made it to a very large mechanical door of sort, with a lever right next to it...\n")
            banner_text("there is also sunbeams coming in from the bottom of the door...\n")
            banner_text('"This must be the exit!" You think to yourself\n')
            last_choice = int(input("But do you greed more treasure or leave with what you have?\n1 = Stay\n2 = Leave\n"))

            # NEEDS TRY/EXCEPT
            if last_choice == 1:
                banner_text("You have decided to stay and return to the previous room...")
                input()
                self.player = (x, y)
                pos = self.player
                print(self.clean)

            else:
                banner_text("You pull the lever and is met with fresh air and sound of outside, you leave the dungeon")
                input()
                self.banana = 5
                quit_game()    

        if (pos[1] < 0) or (pos[0] < 0) or (pos[0] > (mapsize - 1)) or (pos[1] > (mapsize - 1)):
            print(self.clean)
            print("As you leave the room, darkness sweeps over you! When you finally manage to find your bearings, your back in the previous room again...")
            input("Something doesn't let you leave this way... (OUTSIDE BOUNDS)")
            print(self.clean)
            self.player = (x, y)
            pos = self.player
        else:
            victory = False
            goldpls = 0
            if a.board[self.player[1]][self.player[0]] == "+":
                handle = HandleFunc()
                monst = handle.ShuffleMonster()
                
                for i in monst:
                    if i != None:
                        victory = fightOrFlight(i, in_game_char)
                        goldpls += 1
                        
                if (victory == True or goldpls == 0):
                    handle2 = ShuffleTest()
                    loot = handle2.ShuffleBro()
                    summa = sum(loot)
                    print(loot)
                    print(summa)
                    handle3 = Handle()
                    # all_obj = handle3.load_pickle()
                    
                    for i in all_obj:
                        if i.name == in_game_char.name:
                            in_game_char.wallet += summa
                    handle3.edit_char(all_obj)
                    # ADD IF STATEMENT FOR DIFFERENT LOOT
                    input(f'Coin value = {loot[0]}')
                else:
                    self.player = (x, y)
                    pos = self.player
                    

            a.board[self.goal[1]][self.goal[0]] = "E"
            a.board[self.player[1]][self.player[0]] = "O"
            a.board[y][x] = "-"
            a.board[self.start[1]][self.start[0]] = "S"

def ok(mapsize, startzone, endzone, in_game_char, all_obj):
    c = Movement(startzone, endzone)
    a = DungeonMap(mapsize)
    in_game_char = in_game_char

    while c.banana != 5:
        print(c.clean)
        # print(f'You loot from the previous room was {c.loot.treasure}')
        print("Theres a light both left and right of you, but also from a couple stairs leading up and down...")
        a.display_map()
        d = input("Which way? (d, a, w, s)  >>")
        c.move_player(d, startzone, mapsize, a, in_game_char, all_obj)