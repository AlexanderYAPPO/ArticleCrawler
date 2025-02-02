from urllib.parse import urlparse

def get_base_url(url: str) -> str:
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def build_article_metrics_link(article_url: str) -> str:
    return f"{article_url}/metrics"
