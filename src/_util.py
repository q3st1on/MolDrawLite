from scipy.spatial import distance

def closestNode(node, nodes): # find closes node from list, used for snapping to existing canvas objects
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]

def nearRound(x: float | int, base: int) -> float: # round to nearest arbitrary int. used for canvas grid snapping
    return base * round(x/base)