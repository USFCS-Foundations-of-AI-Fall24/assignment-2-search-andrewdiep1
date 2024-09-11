from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    state_count += 1

    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"Number of states generated: {state_count}")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            state_count += len(successors)

    print("No goal found")
    print(f"Number of states generated: {state_count}")
    return None

### Note the similarity to BFS - the only difference is the search queue

def depth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    state_count += 1

    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print(f"Number of states generated: {state_count}")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            state_count += len(successors)

    print("No goal found")
    print(f"Number of states generated: {state_count}")
    return None

## use the limit parameter to implement depth-limited search
def depth_limited_search(startState, action_list, goal_test, use_closed_list=True, limit=0):
    search_stack = []
    closed_list = {}
    state_count = 0

    search_stack.append((startState, "", 0))  # (state, action, depth)
    if use_closed_list:
        closed_list[startState] = True
    state_count += 1

    while len(search_stack) > 0:
        # This is a (state, action, depth) tuple
        next_state, action, depth = search_stack.pop()

        if goal_test(next_state):
            print("Goal found")
            print(next_state)
            ptr = next_state
            while ptr is not None:
                ptr = ptr.prev
                print(ptr)
            print(f"Number of states generated: {state_count}")
            return next_state

        if depth < limit:
            successors = next_state.successors(action_list)

            if use_closed_list:
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True

            for succ, action_name in successors:
                search_stack.append((succ, action_name, depth + 1))

            state_count += len(successors)

    print("No goal found")
    print(f"Number of states generated: {state_count}")
    return None


## add iterative deepening search here
