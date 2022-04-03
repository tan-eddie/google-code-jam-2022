
def solve(dice):
    dice.sort()
    count = 0
    for d in dice:
        if d >= count + 1:
            count += 1

    return count


def main():
    num_cases = int(input())
    for i in range(num_cases):
        # Don't need number of dice
        input()
        dice = [int(x) for x in input().split(" ")]
        result = solve(dice)
        print("Case #{:d}: {:d}".format(i + 1, result))
        pass


if __name__ == "__main__":
    main()
