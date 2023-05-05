def find_substrings(string):
    temp_array = []
    for i in range(0, len(string)):
        for j in range(i, len(string)):
            temp_array.append(string[i:j+1])
    return set(temp_array)

def find_islands(string, substrings, k):
    island_dict = {}
    island_count = 0
    for element in substrings:
        mystring = string
        mystring = mystring.replace(element, "x")
        island_dict[element] = find_contiguous_position(mystring)
    for key in island_dict:
        if island_dict[key] == k:
            island_count += 1
    return island_count

def find_contiguous_position(string):
    count = 0
    for i in range(0, len(string)):
        if (string[i] == 'x' and (i == len(string)-1 or string[i+1] != 'x')):
            count += 1
    return count

def letterIslands(s, k):
    substrings = find_substrings(s)
    island_count = find_islands(s, substrings, k)
    return island_count

if __name__ == '__main__':
    s = input().strip()
    k = int(input().strip())
    result = letterIslands(s, k)
    print(result)