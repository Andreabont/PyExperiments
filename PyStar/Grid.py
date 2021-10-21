class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = set([])

    def in_bounds(self, p):
        px, py = p
        return ( 0 <= px < self.x and 0 <= py < self.y )

    def passable(self, point):
        return ( point not in self.walls )

    def neighbors(self, p):
        px, py = p
        result = [(px+1,py),(px-1,py),(px,py+1),(px,py-1)]
        result = filter(self.in_bounds, result)
        result = filter(self.passable, result)
        return result

    def set_wall(self, a, b):
        ax, ay = a
        bx, by = b
        minx = min(ax, bx)
        maxx = max(ax, bx)
        miny = min(ay, by)
        maxy = max(ay, by)
        self.walls = self.walls.union(set([(x,y) for x in range(minx,maxx+1) for y in range(miny,maxy+1)]))

class GridWithWeights(Grid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, a, b):
        return self.weights.get(b, 1)

def drawGrid(grid, mark = None, draw_function = None):
    for y in reversed(range(0, grid.y)):
        line = "";
        for x in range(0, grid.x):
            if (x,y) in mark:
               line += '* '
            else:
               if grid.passable((x,y)):
                  line += '. ' if draw_function is None else draw_function((x,y)) + ' '
               else:
                  line += '█ '
        print(line)
