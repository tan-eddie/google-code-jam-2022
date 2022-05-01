
class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


def solve(words):
    # Build nodes
    nodes = []
    for word in words:
        nodes.append(Node(word))

    middle_chars = set()
    left_chars = set()
    right_chars = set()

    for node in nodes:
        # Check middle of each word satisfies contiguous char requirement
        word = node.word
        prev_char = word[0]
        if prev_char in middle_chars:
            return "IMPOSSIBLE"
        left_chars.add(prev_char)
        is_left = True
        for i in range(1, len(word)):
            if word[i] != prev_char:
                if not is_left:
                    if prev_char in middle_chars or prev_char in left_chars or prev_char in right_chars:
                        return "IMPOSSIBLE"
                    middle_chars.add(prev_char)
                prev_char = word[i]
                is_left = False

        # Handle right char
        if prev_char in middle_chars:
            return "IMPOSSIBLE"
        right_chars.add(prev_char)

    # Match the nodes using greedy method
    matched_nodes = set()
    for node in nodes:
        # Search for left char in unmatched right chars
        if node.left is None:
            left_char = node.word[0]
            for match_node in nodes:
                if match_node is node or (match_node in matched_nodes and node in matched_nodes):
                    continue
                if match_node.right is None and match_node.word[-1] == left_char:
                    node.left = match_node
                    match_node.right = node
                    matched_nodes.add(node)
                    matched_nodes.add(match_node)
                    break

        # Search for right char in unmatched left chars
        if node.right is None:
            right_char = node.word[-1]
            for match_node in nodes:
                if match_node is node or (match_node in matched_nodes and node in matched_nodes):
                    continue
                if match_node.left is None and match_node.word[0] == right_char:
                    node.right = match_node
                    match_node.left = node
                    matched_nodes.add(node)
                    matched_nodes.add(match_node)
                    break

    # Check if there are any nodes remaining
    if len(matched_nodes) != len(nodes):
        return "IMPOSSIBLE"

    # Build result string
    result = nodes[0].word
    left = nodes[0].left
    while left != None:
        result = left.word + result
        left = left.left
    right = nodes[0].right
    while right != None:
        result = result + right.word
        right = right.right
    return result


def main():
    num_cases = int(input())
    for i in range(num_cases):
        # Don't need number of words
        input()
        words = input().split(" ")
        result = solve(words)
        print("Case #{:d}: {:s}".format(i + 1, result))
        pass


if __name__ == "__main__":
    main()
