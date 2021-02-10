def check_neighbors(currentState, fringe, prev):
    print('my sack')


def dfs(startState, goalState):

    fringe = []
    closed_set = set()
    prev = {}

    while fringe:
        current_state = fringe.pop()
        if current_state == goalState:
            return "Success!", current_state, prev
        check_neighbors(current_state, fringe, prev)
        closed_set.append(current_state)

    return "No Solution", None, None
