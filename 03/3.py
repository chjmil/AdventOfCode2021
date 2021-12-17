import argparse
import os
from copy import deepcopy

def get_common_bit(input):
    """
    """
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
    
    return gamma

def bit_criteria(input, bit_position, oxygen=True):
    """
    :param bit_position: which bit to look at
    :param oxygen: if true, find oxygen value. Else find c02
    :return dict of c02 and o2 values
    """
    if len(input) <= 1:
        return input
    
    
    bit_string = ''
    for i in input:
        bit_string += i[bit_position]
    
    count = bit_string.count('1')

    if count > len(input)/2:
        important_char = '1' if oxygen else '0'
    elif count < len(input)/2:
        important_char = '0' if oxygen else '1'
    else:
        important_char = '1' if oxygen else '0'
    
    return [x for x in input if x[bit_position] == important_char]
    

def main(input_file: str):
    """
    """
    if not os.path.exists(input_file):
        print(f"Input file does not exist: {input_file}")
        exit(1)
    
    with open(input_file, "r") as f:
        input = [x.strip() for x in f.readlines()]
    
    gamma = get_common_bit(input)    
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(''.join('1' if x == '0' else '0' for x in gamma), 2)
    print(f"PART 1: {gamma_dec * epsilon_dec}")

    # PART 2
    # get oxygen first
    o2_output = deepcopy(input)
    bit_position = 0
    while len(o2_output) > 1 and bit_position < len(input[1]):
        o2_output = bit_criteria(o2_output, bit_position=bit_position, oxygen=True)
        bit_position += 1
    
    co2_output = deepcopy(input)
    bit_position = 0
    while len(co2_output) > 1 and bit_position < len(input[1]):
        co2_output = bit_criteria(co2_output, bit_position=bit_position, oxygen=False)
        bit_position += 1
    
    print(f"o2:{o2_output[0]}\nc02:{co2_output[0]}")

    o2_dec = int(o2_output[0], 2)
    co2_dec = int(co2_output[0], 2)
    print(f"PART 2: {o2_dec * co2_dec}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the program")
    parser.add_argument("--input", help="Path to the input file", type=str, required=True)

    args = parser.parse_args()
    main(args.input)
