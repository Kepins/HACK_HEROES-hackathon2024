from functools import cache


class Node:
    x: float
    y: float
    edges: list["Edge"]


class Edge:
    from_node: Node
    to_node: Node

    @cache
    def distance(self):
        return abs(self.to_node.x - self.from_node.x) + abs(self.to_node.y - self.from_node.y)


class Graph:
    nodes: list[Node]
