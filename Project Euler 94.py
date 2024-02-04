import math

# Valid perimeters
solutions = []

# Return True if area is integral
def is_valid_triangle(one_side, two_sides):
    check = 4 * two_sides * two_sides - one_side * one_side
    root = int(math.sqrt(check))
    return root * root == check

# Brute-force approach
def find_more(perimeter, limit):
    while perimeter <= limit + 3:
        # Length of the two equal sides
        two_sides = perimeter // 3

        # Assume single side is one unit smaller than the other two sides
        one_side = two_sides - 1
        if is_valid_triangle(one_side, two_sides):
            solutions.append(perimeter - 1)

        # Assume single side is one unit bigger than the other two sides
        one_side = two_sides + 1
        if is_valid_triangle(one_side, two_sides):
            solutions.append(perimeter + 1)

        # Next group of triangles
        perimeter += 3

    return perimeter

# Just compute sequence
def sequence(limit):
    # Initial values of the equal sides
    plus_one = [1, 5]
    minus_one = [1, 17]

    solutions.clear()
    # Smallest solutions where:
    solutions.append(3 * plus_one[1] + 1)  # Single side is 1 unit longer than the equal sides
    solutions.append(3 * minus_one[1] - 1)  # Single side is 1 unit shorter than the equal sides

    while solutions[-1] <= limit + 3:
        # Compute next length of equal sides
        next_plus_one = 14 * plus_one[1] - plus_one[0] - 4
        next_minus_one = 14 * minus_one[1] - minus_one[0] + 4

        # Store it, shift off oldest values
        plus_one[0] = plus_one[1]
        plus_one[1] = next_plus_one
        minus_one[0] = minus_one[1]
        minus_one[1] = next_minus_one

        # We are interested in the perimeter
        solutions.append(3 * next_plus_one + 1)
        solutions.append(3 * next_minus_one - 1)

    # Largest perimeter found
    return solutions[-1]

def main():
    solutions.append(16)  # Perimeter of smallest triangle
    perimeter = 18  # Check 18-1 and 18+1 in next step

    tests = int(input())
    for _ in range(tests):
        limit = int(input())

        # Check all perimeters
        while perimeter <= limit + 3:
            perimeter = sequence(limit)

        # Sum of all relevant triangles
        total_sum = sum(x for x in solutions if x <= limit)

        print(total_sum)

if __name__ == "__main__":
    main()
