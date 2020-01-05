def game_of_thrones(states, days):
    """Return a list of integers representing next state of the houses.

    Eight houses are arranged in a straight line.
    Each day every house competes with it's adjacent houses.
    An integer value of 1 represents an active house.
    An integer value of 0 represents an inactive house.

    If the neighbors on both the sides of a house are either active or
    inactive, the house becomes inactive on the next day.
    Otherwise the house becomes active.

    The two houses on each end have a single adjacent house.
    Even after updating the house state, consider its previous state when
    updating the state of other houses.
    The state information of all houses should be updated simultaneously.

    Output: the state of houses after the given number of days.
    """
    if not days:
        return states

    next_state = []
    for idx in range(len(states)):
        left, right = 0, 0
        if idx != 0:
            left = states[idx - 1]
        if idx != len(states) - 1:
            right = states[idx + 1]

        if left == right:
            next_state.append(0)
        else:
            next_state.append(1)

    return game_of_thrones(next_state, days - 1)
