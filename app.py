import os

from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Tmc2 Backend Code Challenge', description='API for managing your highlighted places')

resource_model = api.model('HighlightedPlace', {
    'id': fields.Integer(required=True, description='ID'),
    'name': fields.String(required=True, description='Name'),
    'description': fields.String(required=True, description='Description'),
    'coordinates': fields.String(required=True, description='Coordinates')
})


@api.route('/api/highlight_place/<int:id>')
@api.response(404, 'Highlighted Place not found')
class HighlightedPlace(Resource):
    @api.doc('get_resource')
    def get(self, id):
        pass

    @api.doc('delete_resource')
    def delete(self, id):
        pass


@api.route('/api/highlight_place')
class HighlightedList(Resource):
    @api.doc('list_highlight_places')
    def get(self):
        pass

    @api.doc('create_highlight_place')
    @api.expect(resource_model)
    def post(self):
        pass


PORT = int(os.environ.get('FLASK_PORT', 5000))

if __name__ == '__main__':
    highlight_place = []
    app.run(debug=True, port=PORT, host='0.0.0.0')
