from abc import abstractmethod

from models import Node


def generate_nodes():
    HALL_WIDTH = 30.0
    HALL_HEIGHT = 32.2

    hall4 = HallFactory.get_hall('full', 0, 0)
    hall5 = HallFactory.get_hall('partial', HALL_WIDTH, 0)
    hall2 = HallFactory.get_hall('full', 0, HALL_HEIGHT)
    hall3 = HallFactory.get_hall('full', HALL_WIDTH, HALL_HEIGHT)
    hall1 = HallFactory.get_hall('partial', HALL_WIDTH, HALL_HEIGHT * 2)

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
    def get_hall(cls, hall_type: str, offset_x: float, offset_y: float):
        if hall_type == 'full':
            return FullHall(offset_x, offset_y)
        elif hall_type == 'partial':
            return PartialHall(offset_x, offset_y)


class Hall:
    vertical_small_corridor = 1.5
    vertical_big_corridor = 3
    horizontal_corridor = 2
    shelf_width = 3
    shelf_height = 1.3

    def __init__(self, hall_id: int):
        self.hall_id = hall_id


    def _generate_row_left(self, y: float):
        pass

    def _generate_row_right(self, y: float):
        node_1 = Node(x=0.75, y=0, hall=self.hall_id, shelves=[], edges=[])


    @abstractmethod
    def get_nodes(self):
        pass


class FullHall(Hall):
    def __init__(self, hall_id: int, offset_x: float, offset_y: float):
        super().__init__(hall_id=hall_id)
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.nodes = self._generate()

    def _generate(self):
        return ''

    def get_nodes(self):
        return self.nodes

class PartialHall(Hall):
    def __init__(self, offset_x: float, offset_y: float):
        super().__init__()
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.nodes = self._generate()

    def _generate(self):
        return ''

    def get_nodes(self):
        return self.nodes