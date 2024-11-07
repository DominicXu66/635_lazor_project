
def read_bff_file(file_path):
    grid_flag = False
    grid    = []
    blocks  = {}
    lazors  = []
    points  = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():

                    if line.strip()[0] == '#':
                        continue;

                    ### Read 'GRID START'
                    if line.strip() == 'GRID START':
                        grid_flag = True
                        continue;
                    ### Read 'GRID STOP'
                    elif line.strip() == 'GRID STOP':
                        grid_flag = False
                        continue;

                    ### Read the grid board
                    if grid_flag and line.strip() != 'GRID START':
                        grid.append(line.strip().replace(" ", ""))
                        continue;
                    
                    ### Read the blocks
                    elif not grid_flag and line.strip()[0] != 'L' and line.strip()[0] != 'P':
                        parts = line.strip().split()
                        blocks[parts[0]] = int(parts[1])
                        continue;

                    ### Read the lazors
                    elif not grid_flag and line.strip()[0] == 'L' and line.strip()[0] != 'P':
                        lazor = []
                        parts = line.strip().split()
                        for i in parts[1:]:
                            lazor.append(int(i))
                        lazors.append(lazor)
                        continue;

                    ### Read the points
                    elif not grid_flag and line.strip()[0] != 'L' and line.strip()[0] == 'P':
                        parts = line.strip().split()
                        coord = (int(parts[1]), int(parts[2]))
                        points.append(coord)

                    elif line.strip()[0] == '#':
                        continue;

    except UnicodeDecodeError:
        print("File is not in a readable text format.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return grid, blocks, lazors, points


def write_txt_file(case_name, answers):
    with open('./results/output.txt', 'w') as file:
        for i in range(len(case_name)):
            file.write(f"{case_name[i]}\n")
            for row in answers[i]:
                file.write(f"{row}\n")
            file.write("\n")



if __name__ == '__main__':
    grid, blocks, lazors, points = read_bff_file('/Users/oaoa/Desktop/Lazor_Project/bff_files/dark_1.bff')

    print(grid)
    print(blocks)
    print(lazors)
    print(points)