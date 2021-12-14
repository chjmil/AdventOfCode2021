import argparse
import os


def main(input_file: str):
    """
    """
    if not os.path.exists(input_file):
        print(f"Input file does not exist: {input_file}")
        exit(1)
    
    with open(input_file, "r") as f:
        input = [x.strip().split(' ') for x in f.readlines()]
    
    ## PART 1
    pos = 0
    depth = 0

    for i in input:
        if i[0] == 'forward':
            pos += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        else:
            depth -= int(i[1])
    
    print(f"PART 1: {pos * depth}")

    # Part 2
    pos = depth = aim = 0

    for i in input:
        if i[0] == 'forward':
            pos += int(i[1])
            depth += aim*int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
        else:
            aim -= int(i[1])
    
    print(f"PART 2: {pos * depth}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the program")
    parser.add_argument("--input", help="Path to the input file", type=str, required=True)

    args = parser.parse_args()
    main(args.input)
