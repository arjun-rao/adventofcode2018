"""Advent of code 2018 solution: Day 02"""
import re
import itertools as it

class Rectangle:
    """Rectangle class to hold coordinates of one rectangle"""
    def __init__(self, id_, x0, y0, x1, y1):
        self.id = id_
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.overlapping = False

    def generate_coordinates(self):
        """Returns an iterator for all coordinates contained by this rectangle
        """
        x_coords = range(self.x0, self.x1+1)
        y_coords = range(self.y0, self.y1+1)
        return it.product(x_coords, y_coords)




def parse_claim(claim):
    """Parse a claim and return set of coordinates of the contained rectangle

    # Arguments:
        claim: string, the claim string in the format `#123 @ 3,2: 5x4`
    # Returns:
        list, [id, x0, y0, x1, y1],
            (x0,y0) and (x1, y1) are the coordinates of
            top left and bottom right corners of the rectangle.
    """
    # Claim Regex pattern for matching claim strings
    pattern = re.compile('^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$')
    items = re.match(pattern, claim).groups()
    x0 = int(items[1])
    y0 = int(items[2])
    x1 = x0 + int(items[3]) - 1
    y1 = y0 + int(items[4]) - 1
    return Rectangle(int(items[0]), x0, y0, x1, y1)


def solve_part1(claims):
    """Solves part 1 by counting all rectangles which contain a coordinate
    """
    rectangles = [parse_claim(claim) for claim in claims]
    coordinates_to_rectangles = {}
    for rectangle in rectangles:
        coords = rectangle.generate_coordinates()
        for point in coords:
            if point not in coordinates_to_rectangles:
                coordinates_to_rectangles[point] = [rectangle]
            else:
                coordinates_to_rectangles[point].append(rectangle)
    solution = [item for item in coordinates_to_rectangles \
                    if len(coordinates_to_rectangles[item]) >= 2]
    print('Solution to part1: %d' % len(solution))
    return rectangles, coordinates_to_rectangles, solution

def solve_part2(claims):
    """Solves part 1 by counting all rectangles which contain a coordinate
    """
    rectangles, coordinates_to_rectangles, coords = solve_part1(claims)
    for item in coords:
        parent_rectangles = coordinates_to_rectangles[item]
        for rect in parent_rectangles:
            rect.overlapping = True
    non_overlapping = [rect for rect in rectangles if rect.overlapping is False]
    solution = non_overlapping[0].id if len(non_overlapping) == 1 else 'No Solution'
    print('Solution to part 2: %s' % solution)
    return non_overlapping

with open('input.txt', 'r') as f:
    CLAIMS = [line.strip() for line in f]

TEST_CLAIMS = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
