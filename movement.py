from DungeonMap import DungeonMap

b = int(input("How big do you want your map? "))

class Movement:
    def __init__(self):
        self.start = (0,0)
        self.goal = (3,3)
        self.player = (0,0)

    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d[0] == 'r':
            pos = (x + 1, y)
            print(pos)

        if d[0] == 'l':
            pos = (x - 1, y)
            print(pos)

        if d[0] == 'u':
            pos = (x, y - 1)
            print(pos)

        if d[0] == 'd':
            pos = (x, y + 1)
            print(pos)

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print("You made it to the end!")

        while self.player != self.goal:
            d = input("Which way? (r, l, u, d\n")
            self.move_player(d)
            a.display_map()



a = DungeonMap(b)
a.display_map()
Movement.move_player()



