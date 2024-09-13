from collections import deque
import math
from queue import PriorityQueue



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
        if goal_test(next_state[0]) :
            print("Goal found")
            # print(next_state, "\n")
            # ptr = next_state[0]
            # while ptr is not None :
            #     ptr = ptr.prev
            #     print(ptr, "\n")
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
        if goal_test(next_state[0]) :
            print("Goal found")
            # print(next_state)
            # ptr = next_state[0]
            # while ptr is not None :
            #     ptr = ptr.prev
            #     print(ptr)
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
def depth_limited_search(startState, action_list, goal_test, use_closed_list=True, limit=0) :
    search_stack = []
    closed_list = {}
    state_count = 0

    search_stack.append((startState, "", 0))  # (state, action, depth)
    if use_closed_list :
        closed_list[startState] = True
    state_count += 1

    while len(search_stack) > 0 :
        # This is a (state, action, depth) tuple
        next_state, action, depth = search_stack.pop()

        if goal_test(next_state) :
            print(f"Goal found at depth {depth}")
            # print(next_state)
            # ptr = next_state
            # while ptr is not None :
            #     ptr = ptr.prev
            #     print(ptr)
            print(f"Number of states generated: {state_count}")
            return next_state

        if depth < limit :
            successors = next_state.successors(action_list)

            if use_closed_list :
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True

            for succ, action_name in successors :
                search_stack.append((succ, action_name, depth + 1))

            state_count += len(successors)

    print("No goal found")
    print(f"Number of states generated: {state_count}")
    return None


## add iterative deepening search here
def iterative_deepening_search(startState, action_list, goal_test, use_closed_list=True, limit=0) :
    state_count = 0

    for i in range(1, limit + 1):
        result, state_count = depth_limited_search_helper(startState, action_list, goal_test, use_closed_list, i)
        state_count += state_count
        if result is not None:
            print(f"Goal found at depth {i}")
            print(f"Number of states generated: {state_count}")
            return result

    print("No goal found")
    print(f"Number of states generated: {state_count}")
    return None


def depth_limited_search_helper(startState, action_list, goal_test, use_closed_list=True, limit=0) :
    search_stack = []
    closed_list = {}
    state_count = 0

    search_stack.append((startState, "", 0))  # (state, action, depth)
    if use_closed_list:
        closed_list[startState] = True
    state_count += 1

    while len(search_stack) > 0 :
        # This is a (state, action, depth) tuple
        next_state, action, depth = search_stack.pop()

        if goal_test(next_state) :
            # Goal found
            return next_state, state_count

        if depth < limit :
            successors = next_state.successors(action_list)

            if use_closed_list :
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True

            for succ, action_name in successors :
                search_stack.append((succ, action_name, depth + 1))

            state_count += len(successors)

    # No goal found
    return None, state_count


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0


## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    x, y = map(int, state.location.split(','))
    return math.sqrt((x - 1)**2 + (y - 1)**2)