def solve(nums):
    a = sum(nums)
    b = 0
    for n in nums:
        b += n*n

    if a == 0:
        if b == 0:
            return "1"
        else:
            return "IMPOSSIBLE"

    result = (b - a*a) / (2*a)
    if result.is_integer():
        return str(int(result))
    else:
        return "IMPOSSIBLE"


def main():
    num_cases = int(input())
    for i in range(num_cases):
        _, k = tuple(int(x) for x in input().split(" "))
        nums = [int(x) for x in input().split(" ")]
        result = solve(nums)
        print("Case #{:d}: {:s}".format(i + 1, result))


if __name__ == "__main__":
    main()
