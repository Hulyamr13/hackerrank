from random import randint

class MonopolyBoard:
    def __init__(self, N):
        self.num_squares = 40
        self.N = N
        self.cc_cards = ["GO", "JAIL"] + [""] * 14  # Community Chest cards
        self.ch_cards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "nextR", "nextR", "nextU", "back3"] + [""] * 6  # Chance cards
        self.squares = [
            "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
            "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
            "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
            "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
        ]

    def cc(self, current_square):
        card = self.cc_cards.pop(0)
        self.cc_cards.append(card)
        if card == "GO":
            return 0
        elif card == "JAIL":
            return 10
        return current_square

    def chance(self, current_square):
        card = self.ch_cards.pop(0)
        self.ch_cards.append(card)
        if card == "GO":
            return 0
        elif card == "JAIL":
            return 10
        elif card == "C1":
            return 11
        elif card == "E3":
            return 24
        elif card == "H2":
            return 39
        elif card == "R1":
            return 5
        elif card == "nextR":
            while current_square not in [5, 15, 25, 35]:
                current_square = (current_square + 1) % self.num_squares
            return current_square
        elif card == "nextU":
            if current_square == 7:
                return 12
            elif current_square == 22:
                return 28
            else:
                return current_square
        elif card == "back3":
            return (current_square - 3) % self.num_squares
        return current_square

    def move(self, current_square):
        dice_roll = sum([randint(1, self.N) for _ in range(2)])
        current_square = (current_square + dice_roll) % self.num_squares
        if current_square in [2, 17, 33]:  # Community Chest
            current_square = self.cc(current_square)
        elif current_square in [7, 22, 36]:  # Chance
            current_square = self.chance(current_square)
        elif current_square == 30:  # Go to Jail
            current_square = 10
        return current_square

    def simulate(self, iterations=2000000):
        counts = [0] * self.num_squares
        current_square = 0
        for _ in range(iterations):
            current_square = self.move(current_square)
            counts[current_square] += 1
        return counts

    def find_top_squares(self, K=3):
        counts = self.simulate()
        top_squares = sorted(range(len(counts)), key=lambda i: counts[i], reverse=True)[:K]
        return top_squares

def main():
    N, K = map(int, input().split())
    board = MonopolyBoard(N)
    top_squares = board.find_top_squares(K)
    print(" ".join(board.squares[square] for square in top_squares))

if __name__ == "__main__":
    main()
