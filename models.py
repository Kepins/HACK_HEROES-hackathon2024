from dataclasses import dataclass


@dataclass
class Node:
    x: float
    y: float
    hall: int
    lane: int
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

    def distance(self):
        return abs(self.to_node.x - self.from_node.x) + abs(self.to_node.y - self.from_node.y)


@dataclass
class Graph:
    nodes: list[Node]

    def find_shortest_path(self, start: Node, end: Node) -> list[Node]:
        @dataclass
        class AStarNode:
            node: Node
            parent: "AStarNode" = None
            g: int = 0
            h: int = 0
            f: int = 0

            def __eq__(self, other):
                return self.node is other.node

        # Create start and end node
        start_node = AStarNode(node=start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = AStarNode(node=end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.node)
                    current = current.parent
                return path[::-1]  # Return reversed path

            # Loop through children
            for edge in current_node.node.edges:
                child = AStarNode(node=edge.to_node, parent=current_node)

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + edge.distance()
                child.h = ((child.node.x - end_node.node.x) ** 2) + (
                            (child.node.y - end_node.node.y) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

        return None

