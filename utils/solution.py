class Solution:
    def __init__(self, block_board):
        self.solutions = []
        self.block_board = block_board
        self.available_positions = [(i, j) for i, row in enumerate(self.block_board) for j, cell in enumerate(row) if cell == 'o']


    def backtrack(self, board, remaining_blocks, pos_index):
        ### All blocks have been placed
        if all(count == 0 for count in remaining_blocks.values()):
            self.solutions.append([''.join(row) for row in board])
            return

        ### Block placed out of bounds
        if pos_index >= len(self.available_positions):
            return

        ### Available positions to place blocks
        x, y = self.available_positions[pos_index]

        ### Placement of blocks
        for block_type in remaining_blocks:
            if remaining_blocks[block_type] > 0:
                board[x][y] = block_type
                remaining_blocks[block_type] -= 1
                # Recursion for next Placement
                self.backtrack(board, remaining_blocks, pos_index + 1)
                # Traceback to previous state
                board[x][y] = 'o'
                remaining_blocks[block_type] += 1

        ### Skip the current Placement
        self.backtrack(board, remaining_blocks, pos_index + 1)


    def place_blocks(self, blocks):
        initial_board = [list(row) for row in self.block_board]
        self.backtrack(initial_board, blocks.copy(), 0)

        return self.solutions


### DEBUG
if __name__ == '__main__':
    blocks = {'A': 1, 'B': 1}
    block_board = ['ooo', 'xxx', 'ooo']
    solution = Solution(block_board)
    all_solutions = solution.place_blocks(blocks)
    # for solution in all_solutions:
    #     print("\n".join(solution))
    #     print("-------")

    print(all_solutions)