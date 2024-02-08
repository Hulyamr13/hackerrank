import math

# generate pseudo-random numbers (Blum Blum Shub algorithm)
def next():
    global seed
    seed *= seed
    seed %= 50515093
    return seed % 500

# a 2D point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # needed for sorting
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y

    # hash method
    def __hash__(self):
        return hash((self.x, self.y))

    # equality method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# define a segment
class Segment:
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

# find intersection of two segments, out parameter "where" is only valid if function returns true
def intersect(segment1, segment2):
    # shorter names for the four endpoints
    a = segment1.from_
    b = segment1.to
    c = segment2.from_
    d = segment2.to

    # store slope in a Point (just because I'm lazy and don't want to introduce another data type)
    slope1 = Point(b.x - a.x, b.y - a.y)
    slope2 = Point(d.x - c.x, d.y - c.y)

    determinant = slope1.x * slope2.y - slope2.x * slope1.y
    # parallel ?
    if determinant == 0:
        return False, None

    # now the lines intersect, but not necessarily the segments
    s = (slope1.x * (a.y - c.y) - slope1.y * (a.x - c.x)) / determinant
    t = (slope2.x * (a.y - c.y) - slope2.y * (a.x - c.x)) / determinant

    # parameters s and t must be in (0 ... 1)
    # borders (=endpoints) are not true intersections according to problem statement
    if s <= 0 or s >= 1 or t <= 0 or t >= 1:
        return False, None

    # yes, intersection found (might be a duplicate, though !)
    where = Point(a.x + t * slope1.x, a.y + t * slope1.y)

    # cut off a few digits to avoid rounding issues
    Precision = 0.00000001
    where.x = round(where.x / Precision) * Precision
    where.y = round(where.y / Precision) * Precision

    return True, where

def main():
    global seed
    segments = []
    intersections = set()

    seed = 290797
    limit = int(input())

    for _ in range(limit):
        # create "random" segment
        current = Segment(Point(next(), next()), Point(next(), next()))

        # try to intersect with all other segments
        for compare in segments:
            found, where = intersect(current, compare)
            if found:
                intersections.add(where)

        # add current segment to list of segments
        segments.append(current)

    # display result
    print(len(intersections))

if __name__ == "__main__":
    main()
