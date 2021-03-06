from injector import inject
from typing import Any, List

from lingany_api.persistance.dto.reflection_dto import ReflectionDTO
from sqlutils import Repository, DataContext, create_one, create_many


class ReflectionRepository(Repository[ReflectionDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> ReflectionDTO:
        data = self._context.callproc('get_reflection_by_id', [uid])
        return create_one(ReflectionDTO, data)

    def get_all(self) -> List[ReflectionDTO]:
        data = self._context.callproc('get_all_reflections', [])
        return create_many(ReflectionDTO, data)

    def get_reflection_by_languages(self, native_language_id: str,
                                    foreign_language_id: str) -> ReflectionDTO:
        data = self._context.callproc('get_reflection_by_languages', [native_language_id, foreign_language_id])
        return create_one(ReflectionDTO, data)

    def add(self, entity: ReflectionDTO) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
