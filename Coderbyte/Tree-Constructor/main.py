def TreeConstructor(strArr):
    parent_of = {} # {chidren: parent}
    children_count = {} # {parent: count}
    children_of = {}
    nodes = set()

    for pair in strArr:
        # extract child, parent
        child, parent = map(int, pair.strip("()").split(","))
        nodes.add(child)
        nodes.add(parent)

        # 1. child could only has one parent
        if child in parent_of:
            if parent_of[child] != parent:
                return "false"
            continue

        parent_of[child] = parent
        children_count[parent] = children_count.get(parent, 0) + 1

        # 2. parent could only has two children at most
        if children_count[parent] > 2:
            return "false"

        children_of.setdefault(parent, []).append(child)

    # roots should only has one
    roots = [node for node in nodes if node not in parent_of]
    if len(roots) != 1:
        return "false"

    visited = set()
    stack = [roots[0]]
    while stack:
        node = stack.pop()

        if node in visited:
            return "false"
        
        visited.add(node)
        stack.extend(children_of.get(node, []))
    
    return "true"



# Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: true
# Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
# Output: false
assert TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]) == "true"
assert TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]) == "false"
