import uuid
from collections import namedtuple

from PIL import Image, ImageDraw


Point = namedtuple('Point', ['x', 'y'])


class PathDrawer:
    PIXELS_PER_METER = 22.132505276

    def __init__(self, real_points: list[Point]):
        self.real_points = real_points
        self.image_path = "TASK-FILES/RysunekTechnicznyMagazynuA4-1.png"
        self.output_image_path = f"temp_path_png/output_image_{str(uuid.uuid4())}.png"

    def _convert_to_pixel(self, real_point: Point):
        x = real_point.x * self.PIXELS_PER_METER
        y = real_point.y * self.PIXELS_PER_METER

        return Point(x=x + 113, y=2265 - y)

    def draw_path(self):
        # open file
        image = Image.open(self.image_path)
        pencil = ImageDraw.Draw(image)

        # draw lines
        for i in range(0, len(self.real_points) - 1):
            pixel_start_point = self._convert_to_pixel(self.real_points[i])
            pixel_end_point = self._convert_to_pixel(self.real_points[i + 1])
            start_point = (pixel_start_point.x, pixel_start_point.y)
            end_point = (pixel_end_point.x, pixel_end_point.y)

            pencil.line([start_point, end_point], fill="red", width=5)

        # draw endpoint
        pixel_endpoint = self._convert_to_pixel(self.real_points[-1])
        pencil.point([pixel_endpoint.x, pixel_endpoint.y], fill="red")

        output_path = "temp_path_png/output_image.png"
        image.save(output_path)

        image.close()
