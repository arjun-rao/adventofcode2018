"""Advent of code 2018 solution: Day 02"""
from collections import Counter

def solve_part1(box_ids):
    """Returns the checksum given a list of box ids"""
    twos = 0
    threes = 0
    for box_id in box_ids:
        counts = Counter(box_id)
        has_twos = any([item[1] == 2 for item in counts.most_common()])
        has_threes = any([item[1] == 3 for item in counts.most_common()])
        if has_twos:
            twos += 1
        if has_threes:
            threes += 1
    return twos*threes

def solve_part2(box_ids):
    """Returns remaining characters of first pair that differes 
       by 1 letter in the same position
    """
    seen = []
    for box in box_ids:
        if box in seen:
            continue
        for candidate in box_ids:
            if candidate != box and candidate not in seen:
                mismatch = 0
                mismatch_index = -1
                for index, item in enumerate(candidate):
                    if item != box[index]:
                        mismatch +=1
                        mismatch_index = index
                if mismatch == 1:                    
                    seen.append(box)
                    seen.append(candidate)
                    return [(box, candidate), box[:mismatch_index]+box[mismatch_index+1:]]
    return None

# Solution to part 1: Checksum = Product of number of IDs with repeat 2s and 3s
BOX_IDS = []
with open('input.txt', 'r') as f:
    BOX_IDS = [line.strip() for line in f]
# BOX_IDS = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']


# BOX_IDS = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']



