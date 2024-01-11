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
            start_node = list(filter(lambda n: (n.x==45 and n.y==75.9), nodes))[0]
            path_drawer = PathDrawer()

            for idx, row in csv_data.iterrows():
                path_obj = Path(pick_up=row["Nazwa Produktu"], count=row["Ilość"], tour_id=tour.id, path_to_png="")
                db.add(path_obj)
                db.commit()

                end_node = magazine.get_node(row["ID Produktu"])
                path = graph.shortest_path(start=start_node, end=end_node)
                start_node = end_node

                png_path = os.path.join("static", str(tour.id), f"{path_obj.id}.png")
                path_drawer.draw_path(real_points=[Point(n.x, n.y) for n in path], output_image_path=png_path)

                path_obj.path_to_png = f'/{png_path}'
                db.add(path_obj)
                db.commit()

            path_obj = Path(pick_up="put down", count=0, tour_id=tour.id, path_to_png="")
            db.add(path_obj)
            db.commit()

            end_node = list(filter(lambda n: (n.x==45 and n.y==11.5), nodes))[0]
            path = graph.shortest_path(start=start_node, end=end_node)

            png_path = os.path.join("static", str(tour.id), f"{path_obj.id}.png")
            path_drawer.draw_path(real_points=[Point(n.x, n.y) for n in path], output_image_path=png_path)
            path_obj.path_to_png = f'/{png_path}'

            db.add(path_obj)
            db.commit()


            return redirect("/paths/" + str(tour.id))
    return render_template('upload_form.html')


@app.route('/paths/<id>', methods=['GET'])
def pathsid(id):
    paths_files = db.query(Path.path_to_png).filter(Path.tour_id == id).all()
    p_f = [paths_files[i][0] for i in range(0, len(paths_files))]
    paths_files = p_f
    return render_template('index.html', paths_files=paths_files)


if __name__ == '__main__':
    app.run(debug=True)

