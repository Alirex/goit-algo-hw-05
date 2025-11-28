from goit_algo_hw_05.task_3.services.articles import ARTICLES_CONFIGS, Articles


def test_articles_all() -> None:
    articles_from_enum = set(Articles)
    articles_from_configs = set(ARTICLES_CONFIGS.keys())

    difference = articles_from_enum - articles_from_configs
    assert not difference


def test_articles_available() -> None:
    for article in Articles:
        assert ARTICLES_CONFIGS[article].get_file_path().exists()
