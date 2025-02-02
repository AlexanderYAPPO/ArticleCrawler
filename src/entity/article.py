from src.entity import citation_summary


class Article:
    url: str
    title: str
    metrics: citation_summary.CitationSummary

    def __init__(self, url: str, title: str, metrics: citation_summary.CitationSummary):
        self.url = url
        self.title = title
        self.metrics = metrics

    def tsv(self) -> str:
        return f"{self.url}\t{self.title}\t{self.metrics.tsv()}"
