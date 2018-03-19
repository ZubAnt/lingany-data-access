import logging
from typing import List

from manager.models.category import Category
from manager.services.reader import FolderReader, LineReader


class CategoryService(object):

    @staticmethod
    def get_supported_categories(path: str) -> List[Category]:
        files = FolderReader.get_files(path)
        categories = []
        for filename in files:
            logging.info(f'load category from {filename}')
            data = LineReader.read(filename)
            if len(data) < 2:
                continue
            title = data[0]
            values = set(data[1:])
            categories.append(Category(title=title, values=values))

        return categories
