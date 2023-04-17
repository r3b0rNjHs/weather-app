import os

from flask import Flask, request, jsonify, make_response
from flask_restx import Api, Resource, fields

from src.infrastructure.use_case_factory import *

app = Flask(__name__)
api = Api(app, version='1.0', title='Tmc2 Backend Code Challenge', description='API for managing your highlighted places')

app.config['JSONIFY_MIMETYPE'] = 'application/json'

resource_model = api.model('HighlightedPlace', {
    'name': fields.String(required=True, description='Name of your Highlighted Place'),
    'description': fields.String(required=True, description='Description for your Highlighted Place'),
    'coordinates': fields.String(required=True, description='Coordinates'),
})


@api.route('/api/highlight_place/<int:id>')
@api.response(404, 'Highlighted Place not found')
class HighlightedPlace(Resource):
    @api.doc('get_highlight_place')
    def get(self, id):
        try:
            result = get_highlighted_place_use_case().execute(highlighted_place_id=id)
            return make_response(jsonify(result.to_dict()), 200)
        except Exception as e:
            print('ErrorAddingHighlightedPlace', e)

    @api.doc('delete_highlight_place')
    def delete(self, id):
        try:
            result = delete_highlighted_place_use_case().execute(highlighted_place_id=id)
            return make_response(jsonify(result.to_dict()), 200)
        except Exception as e:
            print('ErrorDeletingHighlightedPlace', e)


@api.route('/api/highlight_place')
class HighlightedList(Resource):
    @api.doc('list_highlight_places')
    def get(self):
        try:
            result = get_all_highlighted_places_use_case().execute()
            return make_response(jsonify([place.to_dict() for place in result]), 200)
        except Exception as e:
            print('ErrorListingHighlightedPlaces', e)

    @api.doc('create_highlight_place')
    @api.expect(resource_model)
    def post(self):
        try:
            data = request.get_json()
            name = data.get('name')
            description = data.get('description')
            coordinates = data.get('coordinates')
            result = create_highlighted_place_use_case().execute(name, description, coordinates)
            return make_response(jsonify(result.to_dict()), 200)
        except Exception as e:
            print('ErrorCreatingHighlightedPlace', e)


PORT = int(os.environ.get('FLASK_PORT', 5000))

if __name__ == '__main__':
    highlight_place = []
    app.run(debug=True, port=PORT, host='0.0.0.0')
