import enum
import pathlib
from typing import Final

from pydantic import BaseModel

PACKAGE_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
FIXTURES_PATH: Final[pathlib.Path] = PACKAGE_PATH / "fixtures"


@enum.unique
class Articles(enum.StrEnum):
    ARTICLE_1 = enum.auto()
    ARTICLE_2 = enum.auto()


class ArticleConfig(BaseModel):
    article: Articles
    file_name: str

    pattern_i_existed: str
    pattern_not_i_existed: str

    def get_file_path(self) -> pathlib.Path:
        return FIXTURES_PATH / self.file_name

    def get_article_text(self) -> str:
        return self.get_file_path().read_text()


ARTICLES_CONFIGS: Final[dict[Articles, ArticleConfig]] = {
    item.article: item
    for item in [
        ArticleConfig(
            article=Articles.ARTICLE_1,
            file_name="article_1.txt",
            pattern_i_existed="Двійковий або логарифмічний пошук часто використовується через швидкий час пошуку",  # noqa: RUF001
            pattern_not_i_existed="Було проведено серію експериментів для порівняння ефективності використання розглянутих структур даних",  # noqa: E501
        ),
        ArticleConfig(
            article=Articles.ARTICLE_2,
            file_name="article_2.txt",
            pattern_i_existed="Було проведено серію експериментів для порівняння ефективності використання розглянутих структур даних",  # noqa: E501
            pattern_not_i_existed="Двійковий або логарифмічний пошук часто використовується через швидкий час пошуку",  # noqa: RUF001
        ),
    ]
}
