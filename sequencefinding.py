"""Finding a sequence.

Usage: sequencefinding.py NUMBERS...

Arguments:
    NUMBERS   your sequence of numbers
"""

import docopt


def differences(a):
    return [t - s for s, t in zip(a, a[1:])]


def constant_difference(a):
    if len(a) <= 1:
        return None
    if all(a[1] - a[0] == x for x in differences(a)):
        return a[1] - a[0]
    else:
        return None


def linear_difference(a):
    depth = 1
    while len(a) > 2:
        cdiff = constant_difference(a)
        if cdiff is not None:
            return cdiff, depth
        a = differences(a)
        depth += 1
    return None

args = docopt.docopt(__doc__)
numbers = list(map(int, args['NUMBERS']))
lin_diff = linear_difference(numbers)

if lin_diff is not None:
    print("Found a linear difference of {} on layer {}.".format(*lin_diff))
else:
    print("No sequence found.")
