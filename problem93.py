def print_formatted(number):
    width = len(bin(number)[2:]) # binary representation width
    for i in range(1, number+1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = (hex(i)[2:]).upper()
        binary = bin(i)[2:]
        print("{0:>{width}} {1:>{width}} {2:>{width}} {3:>{width}}".format(dec, octal, hexa, binary, width=width))