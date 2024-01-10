from abc import abstractmethod

from models import Node


def generate_nodes():
    HALL_WIDTH = 30.0
    HALL_HEIGHT = 32.2

    hall4 = HallFactory.get_hall('full', 0, 0, hall_id=4)
    hall5 = HallFactory.get_hall('partial', HALL_WIDTH, 0, hall_id=5)
    hall2 = HallFactory.get_hall('full', 0, HALL_HEIGHT, hall_id=2)
    hall3 = HallFactory.get_hall('full', HALL_WIDTH, HALL_HEIGHT, hall_id=3)
    hall1 = HallFactory.get_hall('partial', HALL_WIDTH, HALL_HEIGHT * 2, hall_id=1)

    # join hall 4 with 5
    node_from_4 = hall4.get_row(2)[0]
    node_from_5 = hall5.get_row(2)[-1]

    node_from_5.connect(node_from_4)

    node_from_5 = hall5.get_row(5)[0]
    node_from_4 = hall4.get_row(5)[-1]

    node_from_4.connect(node_from_5)

    # join hall 2 with 3
    node_from_2 = hall2.get_row(2)[0]
    node_from_3 = hall3.get_row(2)[-1]

    node_from_3.connect(node_from_2)

    node_from_3 = hall3.get_row(5)[0]
    node_from_2 = hall2.get_row(5)[-1]

    node_from_2.connect(node_from_3)

    # join hall 2 with 4
    node_from_2 = hall2.get_row(7)[5]
    node_from_4 = hall4.get_row(1)[5]

    Node.connect_both_ways(node_from_2, node_from_4)

    # join hall 3 with 5
    node_from_3 = hall3.get_row(7)[5]
    node_from_5 = hall5.get_row(1)[5]

    Node.connect_both_ways(node_from_3, node_from_5)

    # join hall 1 with 3
    node_from_1 = hall1.get_row(7)[5]
    node_from_3 = hall3.get_row(1)[5]

    Node.connect_both_ways(node_from_1, node_from_3)

    return hall1.get_nodes() + hall2.get_nodes() + hall3.get_nodes() + hall4.get_nodes() + hall5.get_nodes()


class HallFactory:
    @classmethod
    def get_hall(cls, hall_type: str, offset_x: float, offset_y: float, hall_id: int):
        if hall_type == 'full':
            return FullHall(offset_x=offset_x, offset_y=offset_y, hall_id=hall_id)
        elif hall_type == 'partial':
            return PartialHall(offset_x=offset_x, offset_y=offset_y, hall_id=hall_id)


class Hall:
    vertical_small_corridor = 1.5
    vertical_big_corridor = 3
    horizontal_corridor = 2
    shelf_width = 3
    shelf_height = 1.3

    def __init__(self, hall_id: int):
        self.hall_id = hall_id

    def _generate_row_left(self, y: float):
        node_11 = Node(x=0.75, y=y, hall=self.hall_id, shelves=[], edges=[])
        node_10 = Node(x=3, y=y, hall=self.hall_id, shelves=[15, 16], edges=[])
        node_9 = Node(x=6, y=y, hall=self.hall_id, shelves=[13, 14], edges=[])
        node_8 = Node(x=9, y=y, hall=self.hall_id, shelves=[11, 12], edges=[])
        node_7 = Node(x=12, y=y, hall=self.hall_id, shelves=[9, 10], edges=[])
        node_6 = Node(x=15, y=y, hall=self.hall_id, shelves=[], edges=[])
        node_5 = Node(x=18, y=y, hall=self.hall_id, shelves=[7, 8], edges=[])
        node_4 = Node(x=21, y=y, hall=self.hall_id, shelves=[5, 6], edges=[])
        node_3 = Node(x=24, y=y, hall=self.hall_id, shelves=[3, 4], edges=[])
        node_2 = Node(x=27, y=y, hall=self.hall_id, shelves=[1, 2], edges=[])
        node_1 = Node(x=29.25, y=y, hall=self.hall_id, shelves=[], edges=[])

        row = [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, node_11]
        for i in range(0, len(row) - 1):
            row[i].connect(row[i + 1])

        return row

    def _generate_row_right(self, y: float):
        node_1 = Node(x=0.75, y=y, hall=self.hall_id, shelves=[], edges=[])
        node_2 = Node(x=3, y=y, hall=self.hall_id, shelves=[1, 2], edges=[])
        node_3 = Node(x=6, y=y, hall=self.hall_id, shelves=[3, 4], edges=[])
        node_4 = Node(x=9, y=y, hall=self.hall_id, shelves=[5, 6], edges=[])
        node_5 = Node(x=12, y=y, hall=self.hall_id, shelves=[7, 8], edges=[])
        node_6 = Node(x=15, y=y, hall=self.hall_id, shelves=[], edges=[])
        node_7 = Node(x=18, y=y, hall=self.hall_id, shelves=[9, 10], edges=[])
        node_8 = Node(x=21, y=y, hall=self.hall_id, shelves=[11, 12], edges=[])
        node_9 = Node(x=24, y=y, hall=self.hall_id, shelves=[13, 14], edges=[])
        node_10 = Node(x=27, y=y, hall=self.hall_id, shelves=[15, 16], edges=[])
        node_11 = Node(x=29.25, y=y, hall=self.hall_id, shelves=[], edges=[])

        row = [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10, node_11]
        for i in range(0, len(row) - 1):
            row[i].connect(row[i + 1])

        return row

    @abstractmethod
    def get_nodes(self):
        pass

    @abstractmethod
    def get_row(self, row_id):
        pass


class FullHall(Hall):
    def __init__(self, hall_id: int, offset_x: float, offset_y: float):
        super().__init__(hall_id=hall_id)
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rows = self._generate_rows()

    def _generate_rows(self):
        rows = {}
        prev = self._generate_row_right(y=4.6 * 6 + 2.3)
        rows[1] = prev
        for i in range(2, 8):
            if i % 2 == 0:
                row = self._generate_row_left(y=4.6 * (7-i) + 2.3)
            else:
                row = self._generate_row_right(y=4.6 * (7-i) + 2.3)

            Node.connect_both_ways(prev[0], row[-1])
            Node.connect_both_ways(prev[5], row[5])
            Node.connect_both_ways(prev[-1], row[0])
            prev = row
            rows[i] = row
        return rows

    def get_nodes(self):
        return [node for row in self.rows.values() for node in row]

    def get_row(self, row_id: int):
        return self.rows[row_id]


class PartialHall(Hall):
    def __init__(self, offset_x: float, offset_y: float, hall_id: int):
        super().__init__(hall_id=hall_id)
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.nodes = self._generate()

    def _generate(self):
        return ''

    def get_nodes(self):
        return self.nodes
