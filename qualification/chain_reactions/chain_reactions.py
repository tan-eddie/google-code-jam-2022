class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def max_score(root):
    root_child_scores = []
    stack = [(root, 0, [], root_child_scores)]
    while stack:
        current, next_child_idx, parent_scores, child_scores = stack.pop()
        if next_child_idx < len(current.children):
            next_child = current.children[next_child_idx]
            stack.append((current, next_child_idx + 1,
                         parent_scores, child_scores))
            stack.append((next_child, 0, child_scores, []))
        else:
            if child_scores:
                min_score = min([score[1] for score in child_scores])
                score_sum = sum([score[0] + score[1]
                                for score in child_scores]) - min_score
                parent_scores.append((score_sum, max(current.val, min_score)))
            else:
                parent_scores.append((0, current.val))

    return sum([score[0] + score[1] for score in root_child_scores])


def main():
    num_cases = int(input())
    for i in range(num_cases):
        # Don't need num_modules
        int(input())

        # Build graph in reversed order, i.e. root is abyss
        nodes = [Node(int(x)) for x in input().split(" ")]
        edges = [int(x) for x in input().split(" ")]
        abyss = Node(0)
        for n in range(len(nodes)):
            next_idx = edges[n] - 1
            if next_idx >= 0:
                nodes[next_idx].children.append(nodes[n])
            else:
                abyss.children.append(nodes[n])

        result = max_score(abyss)
        print("Case #{:d}: {:d}".format(i + 1, result))


if __name__ == "__main__":
    main()
