import heapq

# use a priority queue to find the next cell to process
class Cell:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    # heapq returns the SMALLEST element, therefore I implement this function accordingly
    def __lt__(self, other):
        return self.weight < other.weight

# breadth-search
def search(matrix):
    # matrix height/width
    size = len(matrix)

    # store already processed cells
    processed = [[False] * size for _ in range(size)]

    # process cells in increasing distance from starting point
    next_cells = []
    # add starting points (left column)
    for i in range(size):
        heapq.heappush(next_cells, Cell(0, i, matrix[i][0]))

    while next_cells:
        # get cell with the smallest weight
        cell = heapq.heappop(next_cells)

        # we have been here before ?
        # must have been on a shorter route, hence discard current cell
        if processed[cell.y][cell.x]:
            continue

        processed[cell.y][cell.x] = True

        # finished ?
        if cell.x == size - 1:
            return cell.weight

        # one step right
        if cell.x + 1 < size:
            heapq.heappush(next_cells, Cell(cell.x + 1, cell.y, cell.weight + matrix[cell.y][cell.x + 1]))
        # one step down
        if cell.y + 1 < size:
            heapq.heappush(next_cells, Cell(cell.x, cell.y + 1, cell.weight + matrix[cell.y + 1][cell.x]))
        # one step up
        if cell.y > 0:
            heapq.heappush(next_cells, Cell(cell.x, cell.y - 1, cell.weight + matrix[cell.y - 1][cell.x]))

    return -1  # failed

def main():
    size = 80

    # Input
    size = int(input())

    matrix = []
    for _ in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)

    # go !
    print(search(matrix))

if __name__ == "__main__":
    main()
