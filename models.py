from dataclasses import dataclass
from functools import cache


@dataclass
class Node:
    x: float
    y: float
    hall: int
    shelves: list[int]
    edges: list["Edge"]

    def connect(self, other: "Node"):
        self.edges.append(Edge(from_node=self, to_node=other))

    @staticmethod
    def connect_both_ways(a: "Node", b: "Node"):
        a.edges.append(Edge(from_node=a, to_node=b))
        b.edges.append(Edge(from_node=b, to_node=a))


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
