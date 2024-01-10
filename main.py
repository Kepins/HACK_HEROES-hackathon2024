from hall_factory import generate_nodes
from magazine_map import MagazineMap
from models import Node, Edge


def main():
    nodes = generate_nodes()
    magazine = MagazineMap(nodes=nodes, csv_path='TASK-FILES/ProductsLokalization.csv')


if __name__ == '__main__':
    main()
