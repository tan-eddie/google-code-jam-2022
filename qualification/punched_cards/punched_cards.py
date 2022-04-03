def solve(rows, cols):
    for r in range(rows):
        for i in range(2):
            for c in range(cols):
                if r == 0 and c == 0:
                    print("..", end="")
                elif i == 0:
                    print("+-", end="")
                else:
                    print("|.", end="")
            if i == 0:
                print("+")
            else:
                print("|")

    # Bottom of last row
    for c in range(cols):
        print("+-", end="")
    print("+")


def main():
    num_cases = int(input())
    for i in range(num_cases):
        case = input().split(" ")
        rows = int(case[0])
        cols = int(case[1])
        print("Case #{:d}:".format(i + 1))
        solve(rows, cols)


if __name__ == "__main__":
    main()
