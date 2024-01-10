from abc import abstractmethod

from models import Node


def generate_nodes():
    hall4 = HallFactory.get_hall('full', 0, 0)
    hall5 = HallFactory.get_hall('partial', 0, 0)
    hall3 = HallFactory.get_hall('full', 0, 0)
    hall2 = HallFactory.get_hall('full', 0, 0)
    hall1 = HallFactory.get_hall('partial', 0, 0)



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