import os
import sys
import glob
from utils.utils import read_bff_file, write_txt_file
from utils.grids import Block, Grids, Lazors
from utils.solution import Solution

def main(input_file):
    grids_board, user_blocks, lazors, target_points = read_bff_file(input_file)
    ### DEBUG
    # print(grids_board)
    # print(user_blocks)
    # print(lazors)
    # print(target_points)
    # print()

    # grids_obj = Grids(grids_board, user_blocks, lazors, target_points)
    
    ### DEBUG
    # for row in grids_obj.grids:
    #     for block in row:
    #         print(block.x, block.y, block.type)
    # print()


    solution = Solution(grids_board)
    possible_solutions = solution.place_blocks(user_blocks)

    
    for possible_solution in possible_solutions:
        lazors_obj = Lazors(possible_solution, user_blocks, lazors, target_points)
        lazors_trace = lazors_obj.trace
        ### DEBUG
        # print(possible_solution.trace)
        success_count = 0
        for target_pt in target_points:
            for trace in lazors_trace:
                if target_pt in trace:
                    success_count += 1
                    if success_count == len(target_points):
                        return possible_solution
                    # print(f"Intersection at:  {target_pt}")
                    break;
                else:
                    # print(f"No intercetion at {target_pt}")
                    continue;


    
if __name__ == '__main__':
    case_name = []
    answers   = []

    bff_files = glob.glob("./bff_files/*.bff")
    for bff_path in bff_files:
        ans = main(bff_path)
        if ans:
            case_name.append(bff_path.split("/")[-1])
            answers.append(ans)

    write_txt_file(case_name, answers)