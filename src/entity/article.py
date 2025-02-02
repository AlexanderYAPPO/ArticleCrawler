from src.entity import citation_summary


class Article:
    url: str
    title: str
    metrics: citation_summary.CitationSummary
    used_on_cover: bool

    def __init__(self, url: str, title: str, metrics: citation_summary.CitationSummary, used_on_cover: bool = False):
        self.url = url
        self.title = title
        self.metrics = metrics
        self.used_on_cover = used_on_cover

    def tsv(self) -> str:
        return f"{self.url}\t{self.title}\t{self.used_on_cover}\t{self.metrics.tsv()}"

    def dict(self):
        d = self.metrics.dict()
        d["article_url"] = self.url
        d["article_title"] = self.title
        d["article_used_on_cover"] = self.used_on_cover
        return d
