from sqlutils import Converter
from lingany_api.models.language import Language
from lingany_api.persistance.dto.language_dto import LanguageDTO


class LanguageConverterUserConverter(Converter[Language, LanguageDTO]):

    def convert(self, entity: LanguageDTO) -> Language:
        return Language(uid=entity.uid).fill(title=entity.title)
