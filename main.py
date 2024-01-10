from draw_on_map import Point, PathDrawer
from hall_factory import generate_nodes
from models import Graph
from magazine_map import MagazineMap


def main():
    nodes = generate_nodes()
    graph = Graph(nodes=nodes)
    magazine = MagazineMap(nodes=nodes, csv_path='TASK-FILES/ProductsLokalization.csv')

    path = graph.find_shortest_path(start=graph.nodes[1], end=graph.nodes[0])
    p = PathDrawer(
        real_points=[Point(n.x, n.y) for n in path])
    p.draw_path()


if __name__ == '__main__':
    main()
