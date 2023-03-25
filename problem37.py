from collections import deque

# function to check if the cubes can be stacked vertically
def can_stack_cubes(n, cubes):
    # create a deque to represent the vertical pile of cubes
    pile = deque()

    # maintain two pointers at the beginning and end of the array of cube lengths
    left = 0
    right = n - 1

    # stack the cubes according to the given rule
    while left <= right:
        # compare the lengths of the cubes at the current positions of the two pointers
        if cubes[left] >= cubes[right]:
            pile.appendleft(cubes[left])
            left += 1
        else:
            pile.appendleft(cubes[right])
            right -= 1

        # check if the last cube in the pile violates the given rule
        if len(pile) > 1 and abs(pile[0] - pile[1]) > 1:
            return "No"

    # all cubes have been stacked successfully
    return "Yes"

# main function to read input and print output
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        cubes = list(map(int, input().split()))
        result = can_stack_cubes(n, cubes)
        print(result)
