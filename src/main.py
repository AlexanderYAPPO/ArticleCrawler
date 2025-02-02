from src.parser.volume import get_links_by_section
from src.parser.url import build_article_metrics_link
from src.parser.article import get_metrics
from src.parser import flow

if __name__ == "__main__":
    volume_url = "https://www.nature.com/nm/volumes/28/issues/1"
    flow.fetch_data_for_volume(volume_url)
