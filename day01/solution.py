"""Advent of code 2018 solution: Day 01"""


# Solution to part 1: Sum of given input list


numbers = []
with open('input.txt', 'r') as f:
    numbers = [int(line) for line in f]
print('Part1: {}'.format(sum(numbers)))


# Solution to part 2: Sum of given input list
# Sum list one at a time, and check if current sum has occurred before.
def solve_part2_once(changelist, frequencies, init_sum=0):
    """Finds repeated frequency once"""
    freq = frequencies
    current_sum = init_sum
    freq.add(current_sum)
    for number in changelist:
        current_sum += number
        if current_sum in freq:
            print('Part 2: {}'.format(current_sum))
            return True, freq, current_sum
        freq.add(current_sum)
    return False, freq, current_sum

def solve_part2(changelist):
    """Calls solve_part2_once untill the first repeating frequency is found
       reusing the input list as needed"""
    found, freq, current = solve_part2_once(changelist, {0}, 0)
    while not found:
        found, freq, current = solve_part2_once(changelist, freq, current)

solve_part2(numbers)
