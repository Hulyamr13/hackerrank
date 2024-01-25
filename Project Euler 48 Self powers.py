# Enter your code here. Read input from STDIN. Print output to STDOUT

def count(num):
    modulus = 10**10
    total_sum = 0
    for i in range(1, num + 1):
        total_sum += pow(i, i, modulus)
    return str(total_sum % modulus)

if __name__ == "__main__":
    t = int(input())
    print(count(t))
