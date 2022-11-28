import sys


def minimumDistances(a):
    matchingElements = dict()
    minDistnce = sys.maxsize
    oldIndex = 0
    newIndex = 0
    for i in range(len(a)):
        if a[i] in matchingElements:
            newIndex = i
            oldIndex = matchingElements[a[i]]
            minDistnce = min((newIndex - oldIndex), minDistnce)
        matchingElements[a[i]] = i
    if minDistnce == sys.maxsize:
        return -1
    return minDistnce
