from DungeonMap import DungeonMap

b = int(input("How big do you want your map? "))

class Movement:
    def __init__(self):
        self.start = (0,0)
        self.goal = (b,b)
        self.player = (0,0)
        self.walls = ((b + 1), (b + 1))


    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d == 'r':
            pos = (x + 1, y)
            print(pos)
            print("pos")
            print(self.player)
            print("player")


        if d == 'l':
            pos = (x - 1, y)
            print(pos)
            print("pos")
            print(self.player)
            print("player")

        if d == 'u':
            pos = (x, y - 1)
            print(pos)
            print("pos")
            print(self.player)
            print("player")

        if d == 'd':
            pos = (x, y + 1)
            print(pos)
            print("pos")
            print(self.player)
            print("player")

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print("You made it to the end!")

        if (pos[1] > b):
            print("Outside bounds Y")
            self.player = (x, y)
            pos = self.player
            print(pos)
            print(self.player)
        
        if (pos[0] > b):
            print("Outside bounds X")
            self.player = (x, y)
            pos = self.player
            print(pos)
            print(self.player)

        if (pos[0] < 0):
            print("Outside bounds X")
            self.player = (x, y)
            pos = self.player
            print(pos)
            print(self.player)

        if (pos[1] < 0):
            print("Outside bounds X")
            self.player = (x, y)
            pos = self.player
            print(pos)
            print(self.player)

c = Movement()
a = DungeonMap(b)

while c.player != c.goal:
    d = input("Which way? (r, l, u, d\n")
    c.move_player(d)
    a.display_map()






