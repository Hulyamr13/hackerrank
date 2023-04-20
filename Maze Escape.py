strs = ['UP', 'RIGHT', 'DOWN', 'LEFT']
player_id = int(input())  # Read player id as integer
mp = []
for i in range(3):
    mp.append(input())  # Read visible maze as input

# Extract the adjacent cells of the bot based on its position and orientation
C = [mp[0][1], mp[1][2], mp[2][1], mp[1][0]]
f = 0
for i in range(4):
    if C[i] == 'e':
        print(strs[i])  # Print the next move of the bot based on door position
        f = 1
        break
if f == 0:
    for i in range(4):
        if C[i] == '-' or C[i] == 'b':
            print(strs[i])  # Print the next move of the bot based on available path
            break
