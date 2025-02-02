from src.parser.volume import get_links_by_section
from src.parser.url import build_article_metrics_link
from src.parser.article import get_metrics

def fetch_data_for_volume(volume_url: str):
    links_by_section = get_links_by_section(volume_url)

    print("Number of sections:", len(links_by_section))

    for section, links in links_by_section.items():
        print(f"Section: {section}, {len(links)}")
        for link in links:
            article_link = build_article_metrics_link(link)
            print_metrics_for_article(article_link)


def print_metrics_for_article(article_url: str):
    try:
        metrics = get_metrics(article_url)
    except Exception as e:
        print(f"Failed to retrieve metrics for {article_url}. Error: {e}")
        return
    print(metrics.get_article_accesses_readable())
    print(metrics.get_web_of_science_readable())
    print(metrics.get_cross_ref_readable())
    print(metrics.get_almetric().get_score_readable())
    print(metrics.get_almetric().get_details_readable())