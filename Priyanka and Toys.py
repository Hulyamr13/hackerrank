import sys

def toys(w):
    w.sort()  # Sort the list of weights

    count = 0  # Initialize the count of containers
    i = 0  # Initialize the index of the weights list

    while i < len(w):
        temp = w[i] + 4  # Calculate the weight limit for the container
        count += 1  # Increment the count of containers
        while i < len(w) and w[i] <= temp:
            i += 1  # Move to the next weight within the weight limit

    return count


if __name__ == '__main__':
    N = int(input())  # Read the number of orders to ship
    a = list(map(int, input().split()))  # Read the weight array

    result = toys(a)  # Call the toys function to get the minimum number of containers
    print(result)  # Print the result