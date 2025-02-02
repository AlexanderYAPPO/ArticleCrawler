from typing import List, Tuple

from src.entity.article import Article


class Issue:
    url: str
    year: int
    issue: int
    articles: List[Tuple[Article, str]]

    def __init__(self, url: str, year: int, issue: int, articles: List[Tuple[Article, str]]):
        self.url = url
        self.year = year
        self.issue = issue
        self.articles = articles

    def tsv_list(self) -> List[str]:
        return [
            f"{self.url}\t{self.year}\t{self.issue}\t{section}\t{article.tsv()}"
            for article, section in self.articles
        ]
