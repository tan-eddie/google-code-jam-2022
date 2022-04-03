TARGET_SUM = 1000000


def solve(inks):
    color = [min(x) for x in zip(*inks)]
    s = sum(color)
    diff = s - TARGET_SUM
    if diff < 0:
        return "IMPOSSIBLE"
    elif diff > 0:
        for i in range(len(color)):
            adjust = min(color[i], diff)
            color[i] = color[i] - adjust
            diff -= adjust

    return " ".join(str(x) for x in color)


def main():
    num_cases = int(input())
    for i in range(num_cases):
        a = [int(x) for x in input().split(" ")]
        b = [int(x) for x in input().split(" ")]
        c = [int(x) for x in input().split(" ")]
        result = solve([a, b, c])
        print("Case #{:d}: {:s}".format(i + 1, result))


if __name__ == "__main__":
    main()
