import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.console.models import Console
from my_app import api, db

console = Blueprint('console', __name__)

parser = reqparse.RequestParser()
parser.add_argument('tituloSerie', type=str)
parser.add_argument('genero', type=str)
parser.add_argument('tlTemporadas', type=int)
parser.add_argument('mediaIMDB', type=float)
parser.add_argument('ativa', type=str)


@console.route("/")
@console.route("/home")
def home():
    return "Catálogo de Consoles"


class ConsoleAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            consoles = Console.query.paginate(page, 10).items
        else:
            consoles = [Console.query.get(id)]
        if not consoles:
            abort(404)
        res = {}
        for con in consoles:
            res[con.id] = {
                'tituloSerie': con.tituloSerie,
                'genero': con.genero,
                'tlTemporadas': str(con.tlTemporadas),
                'mediaIMDB': str(con.mediaIMDB),
                'ativa': con.ativa
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        tituloSerie = args['tituloSerie']
        genero = args['genero']
        tlTemporadas = args['tlTemporadas']
        mediaIMDB = args['mediaIMDB']
        ativa = args['ativa']

        # con = Console(name, year, price)
        con = Console(tituloSerie, genero, tlTemporadas, mediaIMDB, ativa)
        db.session.add(con)
        db.session.commit()
        res = {}
        res[con.id] = {
            'tituloSerie': con.tituloSerie,
            'genero': con.genero,
            'tlTemporadas': str(con.tlTemporadas),
            'mediaIMDB': str(con.mediaIMDB),
            'ativa': con.ativa
        }
        return json.dumps(res)


api.add_resource(
    ConsoleAPI,
    '/api/console',
    '/api/console/<int:id>',
    '/api/console/<int:id>/<int:page>'
)
