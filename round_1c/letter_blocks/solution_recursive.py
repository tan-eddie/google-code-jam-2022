def verify(word):
    letters = set()
    prev = word[0]
    for c in word:
        if c != prev:
            if prev in letters:
                return False
            else:
                letters.add(prev)
                prev = c
    if c in letters:
        return False
    return True


def solve(start, words):
    if len(words) == 0:
        return [start]

    solutions = []
    for i in range(len(words)):
        new_solutions = solve(start + words[i], words[:i] + words[i+1:])
        for solution in new_solutions:
            if verify(solution):
                solutions.append(solution)
    return solutions


def main():
    num_cases = int(input())
    for i in range(num_cases):
        # Don't need number of words
        input()
        words = input().split(" ")
        result = solve("", words)
        solution = "IMPOSSIBLE"
        if len(result) > 0:
            solution = result[0]
        print("Case #{:d}: {:s}".format(i + 1, solution))
        pass


if __name__ == "__main__":
    main()
