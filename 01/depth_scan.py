import argparse
import os


def main(input_file: str):
    """
    """
    if not os.path.exists(input_file):
        print(f"Input file does not exist: {input_file}")
        exit(1)
    
    with open(input_file, "r") as f:
        input = [int(x) for x in f.readlines()]
    
    ## PART 1
    previous = input[0]
    increase_count = 0

    for i in input:
        if i > previous:
            increase_count+=1
        previous = i
    
    print(f"Part 1: {increase_count}")

    ## PART 2
    groups = []
    for i in range(len(input)):
        groups.append(sum(input[i:i+3]))
        
    previous = groups[0]
    increase_count = 0
    for i in groups:
        if i > previous:
            increase_count+=1
        previous = i
    
    print(f"Part 2: {increase_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the program")
    parser.add_argument("--input", help="Path to the input file", type=str, required=True)

    args = parser.parse_args()
    main(args.input)
