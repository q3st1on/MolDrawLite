from scipy.spatial import distance
from collections import namedtuple

def closestNode(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]

def nearRound(x, base):
    return base * round(x/base)

Offsets = namedtuple("Offsets", "x y")

offsets = Offsets(-0.5, +2.5)