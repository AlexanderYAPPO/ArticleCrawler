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
        keys = self.produce_keys()
        dicts = self.dict_flat()
        res = []
        for d in dicts:
            res.append("\t".join([str(d[key]) for key in keys]))
        return res

    def dict_flat(self) -> List[Dict]:
        res = []
        for article, section in self.articles:
            d = article.dict()
            d["issue_url"] = self.url
            d["issue_title"] = self.title
            d["article_section"] = section
            res.append(d)
        return res

    @staticmethod
    def produce_keys():
        return ["issue_url", "issue_title", "article_section", "article_url", "article_title", "article_used_on_cover", "article_accesses", "article_web_of_science", "article_cross_ref", "almetric_score", "almetric_details"]

    @staticmethod
    def produce_keys_tsv():
        return "\t".join(Issue.produce_keys())

    def key_value_flat(self) -> List[List]:
        res = []
        for article, section in self.articles:
            a = article.key_value()
            res.append(
                [
                    ("issue_url", self.url),
                    ("issue_title", self.title),
                    ("article_section", section),
                    *a
                ]
            )
        return res
