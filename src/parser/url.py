from urllib.parse import urlparse

def get_base_url(url: str) -> str:
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def fetch_doi_from_article_url(article_url: str) -> str:
    parsed_url = urlparse(article_url)
    return parsed_url.path.rstrip("/").split("/")[-1]

def build_article_metrics_link(article_url: str) -> str:
    return f"{article_url}/metrics"
