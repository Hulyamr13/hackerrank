# Enter your code here. Read input from STDIN. Print output to STDOUT

digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
          "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def word(num):
    if num // 100 > 0:
        print(digits[num // 100] + " Hundred ", end="")
    if (num % 100) < 20 and (num % 100) > 0:
        print(digits[num % 100] + " ", end="")
    elif (num // 10) % 10 > 0:
        print(tens[(num // 10) % 10] + " ", end="")
        if num % 10 > 0:
            print(digits[num % 10] + " ", end="")


num_cases = int(input())

for _ in range(num_cases):
    num = int(input())
    tn = num // 1000000000000
    bn = (num // 1000000000) % 1000
    mn = (num // 1000000) % 1000
    th = (num // 1000) % 1000
    hd = num % 1000

    if (tn + bn + mn + th + hd) == 0:
        print("Zero")
    if tn > 0:
        word(tn)
        print("Trillion ", end="")
    if bn > 0:
        word(bn)
        print("Billion ", end="")
    if mn > 0:
        word(mn)
        print("Million ", end="")
    if th > 0:
        word(th)
        print("Thousand ", end="")
    if hd > 0:
        word(hd)
    print()
