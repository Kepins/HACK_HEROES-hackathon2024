import pandas as pd

from models import Node


class MagazineMap:
    def __init__(self, csv_path, nodes: list[Node]):
        self._magazine = self.load_csv(csv_path=csv_path, nodes=nodes)

    def load_csv(self, csv_path: str, nodes: list[Node]):
        products = pd.read_csv(csv_path)
        magazine = {}
        for index, row in products.iterrows():
            localisation = row['Lokacja']
            product_hall = int(localisation[1])
            product_lane = int(localisation[2:4])
            product_shelf = int(localisation[5:7])

            # find Nodes
            filtered_nodes = [node for node in nodes if node.hall == product_hall and node.lane == product_lane and product_shelf in node.shelves]
            magazine[row['ID Produktu']] = filtered_nodes

        return magazine

    def get_node(self, item_id: int):
        return self._magazine.get(item_id, None)
