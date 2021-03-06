from flask import Blueprint, request
from injector import singleton, inject

from apiutils import BaseBlueprint
from lingany_api.serializers.word_serializer import WordSerializer
from lingany_api.services.word_service import WordService
from sqlutils import ExpandSet


@singleton
class WordBlueprint(BaseBlueprint[WordService]):

    @inject
    def __init__(self, service: WordService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'words'

    @property
    def _serializer(self) -> WordSerializer:
        return WordSerializer()

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/<uid>', methods=['GET'])
        def _get_by_id(uid: str):
            raise NotImplementedError

        @blueprint.route('/', methods=['GET'])
        def _get_all():
            raise NotImplementedError

        @blueprint.route('/text/<text>/<ref_id>', methods=['GET'])
        def _get_translation_by_text(text: str, ref_id: str):
            expand = ExpandSet.load(request.args.get('expand'))
            model = self._service.get_translation_by_text(text, ref_id, expand=expand)
            return self._return_one(model)

        @blueprint.route('/translation/<translation>/<ref_id>', methods=['GET'])
        def _get_text_by_translation(translation: str, ref_id: str):
            expand = ExpandSet.load(request.args.get('expand'))
            model = self._service.get_text_by_translation(translation, ref_id, expand=expand)
            return self._return_one(model)

        return blueprint
