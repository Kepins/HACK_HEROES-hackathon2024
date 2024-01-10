from draw_on_map import Point, PathDrawer
from hall_factory import generate_nodes
from graphs import Graph
from magazine_map import MagazineMap
from session import db

def main():
    nodes, doors = generate_nodes()
    graph = Graph(nodes=nodes, doors=doors)
    magazine = MagazineMap(nodes=nodes, csv_path='TASK-FILES/ProductsLokalization.csv')

    path = graph.shortest_path(start=graph.nodes[217], end=graph.nodes[35])
    p = PathDrawer(
        real_points=[Point(n.x, n.y) for n in path])
    p.draw_path()


if __name__ == '__main__':
    main()
