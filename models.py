from dataclasses import dataclass
from functools import cache

@dataclass
class Node:
    x: float
    y: float
    hall: int
    shelves: list[int]
    edges: list["Edge"]

@dataclass
class Edge:
    from_node: Node
    to_node: Node

    @cache
    def distance(self):
        return abs(self.to_node.x - self.from_node.x) + abs(self.to_node.y - self.from_node.y)

@dataclass
class Graph:
    nodes: list[Node]
