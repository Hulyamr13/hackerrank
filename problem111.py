k = int(input())
room_list = list(map(int, input().split()))

# Using dictionary to count occurrences of each room number
room_count = {}
for room in room_list:
    if room in room_count:
        room_count[room] += 1
    else:
        room_count[room] = 1

# Finding the Captain's room number
for room, count in room_count.items():
    if count != k:
        print(room)
        break