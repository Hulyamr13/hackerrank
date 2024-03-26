threshold = 120
reader = {'0110111110010000000000001111000000000000': 'A',
          '01111110011000110110000101100011011111100110001101100001011000010110001101111110': 'B',
          '0111110110001110000011000000100000010000001000000100000111000110111110': 'C',
          '01111110011000110110000101100001011000010110000101100001011000010110001101111110': 'D',
          '011111110011000000011000000011000000011111100011000000011000000011000000011000000011111110': 'E',
          '0111111110011000000001100000000110000000011111100001100000000110000000011000000001100000000110000000': 'F',
          '0111110110001110000001000000100000010001111000011100001111000110111110': 'G',
          '0110011001100110011101100110011001100110': 'H',
          '0110011001100110111001100110011001100110': '',
          '01111110000110000001100000011000000110000001100000011000000110000001100001111110': 'I',
          '011110000110000110000110000110000110000110000110101100111000': 'J',
          '0110011001100110011101110110011001100110': 'K',
          '0110110010000000000000000000100011000110': '', '0110011001100110011001100110011001100111': 'L',
          '0110011101110110011001100110011001100110': 'M', '0110111011100110011001100110011001100110': '',
          '0110011101110111011001100110011001100110': 'N', '0110011001100110011001101110111011100110': '',
          '011110110011100001100001100001100001100001100001110011011110': 'O',
          '011111110011000011011000011011000011011111110011000000011000000011000000011000000011000000': 'P',
          '011110110011100001100001100001100001101101100111110011011110': 'Q',
          '011111110011000011011000011011000011011111110011111000011001100011000110011000011011000011': 'R',
          '01111110110000111100000011000000011111100000001100000011000000111100001101111110': 'S',
          '0111111110000011000000001100000000110000000011000000001100000000110000000011000000001100000000110000': 'T',
          '0110011001100110011001100110011000110001': 'U', '0110011001100110011001100110011011001000': '',
          '0110011001100011001100110001000100000000': 'V', '0110011001101100110011001000100000000000': '',
          '0110011001100110011001100110011101110110': 'W', '0110011001100110011001100110111011100110': '',
          '0110011000110001000000000001001101100110': 'X', '0110011011001000000000001000110001100110': '',
          '0110011000110001000000000000000000000000': 'Y', '0110011011001000000000000000000000000000': '',
          '011111110000000110000000110000001100000011000000110000001100000011000000011000000011111110': 'Z',
          '0110111110010000000000000000100111110110': '0', '0110111011100110011001100110011001101111': '1',
          '011110110011100001000001000011000110001100011000110000111111': '2',
          '0111110110001100000010000011000111000000110000001000000111000110111110': '3',
          '0110111011100110011001101111011001100110': '4',
          '011111110011000000011000000011011100011100110000000011000000011011000011001100110000111100': '5',
          '011110110011100001100000101110110011100001100001110011011110': '6',
          '0111111110000000011000000001100000001100000001100000001100000001100000001100000001100000000110000000': '7',
          '011110110011100001110011011110110011100001100001110011011110': '8',
          '011110110011100001100001110011011101000001100001110011011110': '9'}


def getHash(l):
    return ''.join([''.join(map(str, map(int, x))) for x in l])

rows, columns = input().split()

im = []
for i in range(int(rows)):
    l = input().split()
    r = []
    for px in l:
        r.append(int(px.split(',')[0]) < threshold)
    if any(r):
        im.append(tuple(r))

hashes = []
start = None
end = None

for c in range(len(im[0])):
    if start is None:
        if im[0][c]:
            start = c - 1
    else:
        if not im[0][c]:
            end = c + 1
    if end is not None:
        h = getHash([im[x][start:end] for x in range(10)])
        hashes.append(h)
        start = None
        end = None

out = []
for h in hashes:
    try:
        out.append(reader[h])
    except KeyError:
        out.append('_')
print(''.join(out))