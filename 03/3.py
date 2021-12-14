import argparse
import os
from copy import deepcopy


def main(input_file: str):
    """
    """
    if not os.path.exists(input_file):
        print(f"Input file does not exist: {input_file}")
        exit(1)
    
    with open(input_file, "r") as f:
        input = [x.strip() for x in f.readlines()]
    
    # Combine all of the same digit into a single string
    lists = []
    length = len(input[0])
    for i in range(length):
        l = ''
        for j in input:
            l += j[i]
        lists.append(l)
    
    gamma = ''
    for i in lists:
        gamma += '1' if i.count('1') > len(i)/2 else '0'
    
    gamma_binary = int(gamma, 2)
    epsilon_binary = int(''.join('1' if x == '0' else '0' for x in gamma), 2)

    print(gamma)
    print(input[1])
    print(f"PART 1: {gamma_binary * epsilon_binary}")

    # PART 2
    oxygen = ''
    co2 = ''

    oxygen_deepcopy = deepcopy(input)
    co2_deepcopy = deepcopy(input)

    # get oxygen
    for i in range(length):
        # get oxygen
        if len(oxygen_deepcopy) == 1:
            break
        print(f"\n\ni:{i}")
        for j in input:
            print(f"j:{j}")
            print(f"g:{gamma[i]}")
            if gamma[i] != j[i]:
                print(f"remove:{j}")
                oxygen_deepcopy.remove(j)

    print(oxygen_deepcopy)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the program")
    parser.add_argument("--input", help="Path to the input file", type=str, required=True)

    args = parser.parse_args()
    main(args.input)
