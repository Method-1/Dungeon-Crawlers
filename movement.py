from DungeonWorld import DungeonMap
allowed_movement = 'rlud'
final_answer = 'ls'

# MENY SAKER
mapsize = int(input("How big do you want your map? "))
corner = int(input("Which corner do you want to start in?\nTop Left = 1\nBottom Left = 2\nTop Right = 3\nBottom Left = 4\n"))
if corner == 1:
    startzone = (0,0)
    endzone = (mapsize - 1, mapsize - 1)

elif corner == 2:
    startzone = (0, mapsize - 1)
    endzone = (mapsize - 1, 0)

elif corner == 3:
    startzone = (mapsize - 1, 0)
    endzone = (0, mapsize - 1)

elif corner == 4:
    startzone = (mapsize - 1, mapsize - 1)
    endzone = (0,0)

class Movement:
    def __init__(self):
        self.start = (startzone[0],startzone[1])
        self.goal = endzone
        self.player = startzone
        self.walls = (0,0)
        self.clean = ("\n" * 100)
        self.finished = 1
                
    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = self.player

        if d == 'r':
            input("You go right...")
            pos = (x + 1, y)

        elif d == 'l':
            input("You go left...")
            pos = (x - 1, y)

        elif d == 'u':
            input("You go upstairs...")
            pos = (x, y - 1)
            
        elif d == 'd':
            input("You go downstairs...")
            pos = (x, y + 1)

        else:
            pass

            # CALL FUNCTION TO EXIT
 
        if pos not in self.walls:
            self.player = pos


        if pos == self.goal:
            print(self.clean)
            print("You have made it to a very large mechanical door of sort, with a lever right next to it...")
            print("there is also sunbeams coming in from the bottom of the door...")
            print('"This must be the exit!" You think to yourself\n')
            last_choice = int(input("But do you greed more treasure or leave with what you have?\n1 = Stay\n2 = Leave\n"))

            if last_choice == 1:
                input("You have decided to stay and return to the previous room...")
                self.player = (x, y)
                pos = self.player
                print(self.clean)

            else:
                # EXIT GAME! HIGHSCORE! SAVE CHARACTER!
                pass


        if (pos[1] < 0) or (pos[0] < 0) or (pos[0] > (mapsize - 1)) or (pos[1] > (mapsize - 1)):
            print(self.clean)
            print("As you leave the room, darkness sweeps over you! When you finally manage to find your bearings, your back in the previous room again...")
            input("Something doesn't let you leave this way... (OUTSIDE BOUNDS)")
            print(self.clean)
            self.player = (x, y)
            pos = self.player
        else:
            a.board[self.goal[1]][self.goal[0]] = "E"
            a.board[self.player[1]][self.player[0]] = "O"
            a.board[y][x] = "-"
            a.board[self.start[1]][self.start[0]] = "S"

    def allowed(self, d):
        test = d
        while True:
            try:
                if test in allowed_movement and len(test) != 0 and len(test) == 1:
                    break
                else:
                    print("\nYou think to yourself is that really a direction? (INPUT ERROR)\n")
                    return test
            except:
                print("Input Error")
                return test

c = Movement()
a = DungeonMap(mapsize)

while c.finished != 0:
    print(c.clean)
    print("You ponder which direction to go next.")
    print("Theres a light both left and right of you, but also from a couple stairs leading up and down...")
    a.display_map()
    d = input("Which way? (r, l, u, d)\n")
    c.allowed(d)
    c.move_player(d)
