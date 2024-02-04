# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

Epsilon = 0.00001

# Try all arithmetic operations of any two elements of "numbers", set their result in "used" to true
def eval(numbers, used):
    # Step 1: if array holds just one element, add it to the "used" list and we are done
    if len(numbers) == 1:
        result = numbers[0] + Epsilon
        # Reject non-integer result (caused by division)
        if math.fmod(result, 1) > 10 * Epsilon:
            return
        index = int(result + Epsilon)
        # Reject negative and very large results
        if index >= 0 and index < len(used):
            used[index] = True
        return

    # Step 2: pick any two numbers
    next_numbers = numbers[:]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Fetch two numbers
            a = numbers[i]
            b = numbers[j]

            # Prepare for next recursive step
            next_numbers = numbers[:]
            next_numbers.remove(b)  # Delete the higher index first
            next_numbers.remove(a)

            # Steps 3 and 4 (unrolled)
            next_numbers.append(a + b)  # add
            eval(next_numbers, used)
            next_numbers[-1] = a - b    # subtract (I)
            eval(next_numbers, used)
            next_numbers[-1] = b - a    # subtract (II)
            eval(next_numbers, used)
            next_numbers[-1] = a * b    # multiply
            eval(next_numbers, used)
            if b != 0:
                next_numbers[-1] = a / b  # divide (I)
                eval(next_numbers, used)
            if a != 0:
                next_numbers[-1] = b / a  # divide (II)
                eval(next_numbers, used)

# Evaluate all expressions and count how many numbers from 1 to x can be expressed without any gaps
def get_sequence_length(numbers):
    # Find all results
    used = [False] * 1000
    eval(numbers, used)

    # Longest sequence, beginning from 1
    result = 0
    while used[result + 1]:
        result += 1
    return result

def main():
    num_digits = int(input())

    # 1..5 digits
    numbers = list(map(float, input().split()))

    # Print length of longest sequence
    print(get_sequence_length(numbers))

if __name__ == "__main__":
    main()
