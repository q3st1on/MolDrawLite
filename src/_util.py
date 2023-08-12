from scipy.spatial import distance

def closestNode(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]

def nearRound(x: float | int, base: int) -> float:
    return base * round(x/base)