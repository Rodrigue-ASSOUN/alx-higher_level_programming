import sys

def solve_n_queens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(n, index, ocuppied_positions):
        if index == n:
            return [ocuppied_positions]
        else:
            result = []
            for pos in range(n):
                if can_place(pos, ocuppied_positions):
                    result += place_queen(n, index + 1, ocuppied_positions + [pos])
            return result

    return place_queen(n, 0, [])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print(solution)
