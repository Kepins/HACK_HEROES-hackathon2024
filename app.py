import csv
import io
import os

import pandas
from flask import Flask, render_template, request, redirect

from draw_on_map import PathDrawer, Point
from graphs import Graph
from hall_factory import generate_nodes
from magazine_map import MagazineMap
from models import Tour, Path
from session import db

app = Flask(__name__)


@app.route('/')
def upload_csv():
    return render_template('upload_form.html')


@app.route('/path/', methods=['POST'])
def paths():
    paths = []
    map_path = ''
    if request.method == 'POST':
        if 'file' in request.files:
            csv_file = request.files['file']
            stream = io.StringIO(csv_file.stream.read().decode("UTF-8"), newline="")
            csv_data = pandas.read_csv(stream, )

            tour = Tour()
            db.add(tour)
            db.commit()

            os.mkdir(os.path.join("static", str(tour.id)))

            # shared
            nodes, doors = generate_nodes()
            graph = Graph(nodes=nodes, doors=doors)
            magazine = MagazineMap(nodes=nodes, csv_path='TASK-FILES/ProductsLokalization.csv')
            path_drawer = PathDrawer()

            for idx, row in csv_data.iterrows():
                path_obj = Path(pick_up=row["Nazwa Produktu"], count=row["Ilość"], tour_id=tour.id, path_to_png="")
                db.add(path_obj)
                db.commit()


                path = graph.shortest_path(start=graph.nodes[217], end=magazine.get_node(row["ID Produktu"]))

                png_path = os.path.join("static", str(tour.id), f"{path_obj.id}.png")

                path_drawer.draw_path(real_points=[Point(n.x, n.y) for n in path], output_image_path=png_path)

                path_obj.path_to_png = png_path
                db.add(path_obj)
                db.commit()



            return redirect("/paths/" + str(tour.id))
    return render_template('upload_form.html')


@app.route('/paths/<id>', methods=['GET'])
def pathsid(id):
    tour = db.query(Tour).filter(Tour.id == id)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

