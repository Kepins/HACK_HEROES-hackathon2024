import uuid
from collections import namedtuple

from PIL import Image, ImageDraw


Point = namedtuple('Point', ['x', 'y'])


class PathDrawer:
    PIXELS_PER_METER = 22.132505276

    def __init__(self):
        self.image_path = "TASK-FILES/RysunekTechnicznyMagazynuA4-1.png"

    def _convert_to_pixel(self, real_point: Point):
        x = real_point.x * self.PIXELS_PER_METER
        y = real_point.y * self.PIXELS_PER_METER

        return Point(x=x + 113, y=2265 - y)

    def draw_path(self, real_points: list[Point], output_image_path):
        # open file
        image = Image.open(self.image_path)
        pencil = ImageDraw.Draw(image)

        # draw lines
        for i in range(0, len(real_points) - 1):
            pixel_start_point = self._convert_to_pixel(real_points[i])
            pixel_end_point = self._convert_to_pixel(real_points[i + 1])
            start_point = (pixel_start_point.x, pixel_start_point.y)
            end_point = (pixel_end_point.x, pixel_end_point.y)

            pencil.line([start_point, end_point], fill="red", width=5)

        # draw endpoint
        pixel_endpoint = self._convert_to_pixel(real_points[-1])
        pencil.ellipse((pixel_endpoint.x - 15, pixel_endpoint.y - 15, pixel_endpoint.x + 15, pixel_endpoint.y + 15), fill='red', outline='red')

        image.save(output_image_path)

        image.close()
