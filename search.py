def check_neighbors(currentState, fringe, prev):
    print('my sack')


def dfs(start_state, goal_state):

    fringe = []
    closed_set = set()
    prev = {}
    fringe.append(start_state)

    while fringe:
        current_state = fringe.pop()
        if current_state == goal_state:
            return "Success!", current_state, prev
        check_neighbors(current_state, fringe, prev)
        closed_set.append(current_state)

    return "No Solution", None, None
