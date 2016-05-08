import numpy as np
from collections import defaultdict

doors = [1, 2, 3]

# num trials
N = 10000

strategy = defaultdict(int)

for _ in range(N):
    # which door do you choose and which door hides the car?
    car, you = np.random.choice(doors, 2)

    # which door does monty choose to show?
    # if you == car monty shows any of other two goat doors
    # if you != car monty shows the goat door
    monty = np.random.choice([d for d in doors if d != car]) if you == car else 6 - car - you

    # monty never shows the door with the car
    assert(monty != car)

    if you == car:
        strategy['stick'] += 1
    else:
        strategy['switch'] += 1

# this should be approximately 2
print(strategy['switch']/strategy['stick'])
