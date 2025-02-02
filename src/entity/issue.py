from typing import List, Tuple, Dict

from src.entity.article import Article


class Issue:
    url: str
    year: int
    issue: int
    articles: List[Tuple[Article, str]]

    def __init__(self, url: str, title: str, articles: List[Tuple[Article, str]]):
        self.url = url
        self.title = title
        self.articles = articles

    def tsv_list(self) -> List[str]:
        return [
            f"{self.url}\t{self.title}\t{section}\t{article.tsv()}"
            for article, section in self.articles
        ]

    def dict_flat(self) -> List[Dict]:
        res = []
        for article, section in self.articles:
            d = article.dict()
            d["issue_url"] = self.url
            d["issue_title"] = self.title
            d["article_section"] = section
            res.append(d)
        return res
