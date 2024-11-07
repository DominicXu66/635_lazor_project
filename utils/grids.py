
class Block:
    def __init__(self, x, y, type):       
        self.x = x
        self.y = y
        self.type = type

class Grids:
    def __init__(self, grids, blocks, lazors, points):
        self.blocks = blocks
        self.lazors = lazors
        self.points = points
        self.grids = self.__set_grid(grids)

    def __set_grid(self, grids):
        grid_board = []
        for i, row in enumerate(grids):
            grid_row = []
            for j, block in enumerate(row):
                grid_row.append(Block(i, j, block))
            grid_board.append(grid_row)

        return grid_board
    
class Lazors(Grids):
    def __init__(self, grids, blocks, lazors, points):
        super().__init__(grids, blocks, lazors, points)
        self.trace = [self.__get_lazor_trace(lazor, []) for lazor in self.lazors]
    

    def __get_lazor_trace(self, lazor, trace=[]):
        ### start coord and direction of one lazor
        x, y, vx, vy = lazor

        ### Out of grids board's boundary, Stop
        if y < 0 or x < 0 or y > 2*len(self.grids) or x > 2*len(self.grids[0]):
            return trace
        
        ### Trace of the lazor
        trace.append((x, y))

        ### Will out of grids board's boundary, Stop
        if y+vy < 0 or x+vx < 0 or y+vy > 2*len(self.grids) or x+vx > 2*len(self.grids[0]):
            return trace
        
        ### Coordinate of lazor's next step
        x_, y_ = x + vx, y + vy
        
        ### Which block will be penetrated by the lazor's next step
        m, n = (y+y_)//2//2, (x+x_)//2//2

        ### Opaque block
        if self.grids[m][n].type == 'B':
            return trace

        ### Reflect block
        elif self.grids[m][n].type == 'A':
            reflect_lazor = [x-vx, y+vy, -vx, vy] if x%2 == 0 else [x+vx, y-vy, vx, -vy]
            self.__get_lazor_trace(reflect_lazor, trace)
        
        ### Refract block
        elif self.grids[m][n].type == 'C':
            direct_lazor = [x+vx, y+vy, vx, vy]
            self.__get_lazor_trace(direct_lazor, trace)
            reflect_lazor = [x-vx, y+vy, -vx, vy] if x%2 == 0 else [x+vx, y-vy, vx, -vy]
            self.__get_lazor_trace(reflect_lazor, trace)

        ### No block
        elif self.grids[m][n].type in ['o', 'x']:
            direct_lazor = [x+vx, y+vy, vx, vy]
            self.__get_lazor_trace(direct_lazor, trace)
        
        return trace


if __name__ == '__main__':
    block = Block(5, 10, 'A')
    print(block)


