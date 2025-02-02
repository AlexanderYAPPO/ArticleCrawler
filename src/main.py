from src.parser.volume import get_links_by_section
from src.parser.url import build_article_metrics_link
from src.parser.article import get_metrics

if __name__ == "__main__":
    # links_by_section = get_links_by_section("https://www.nature.com/nm/volumes/28/issues/1")
    #
    # for section, links in links_by_section.items():
    #     print(f"Section: {section}")
    #     for link in links:
    #         print(build_article_metrics_link(link))
    #     print()

    metrics = get_metrics('https://www.nature.com/articles/s41591-021-01599-w/metrics')

    print(metrics.get_article_accesses_readable())
    print(metrics.get_web_of_science_readable())
    print(metrics.get_cross_ref_readable())
    print(metrics.get_almetric().get_score_readable())
    print(metrics.get_almetric().get_details_readable())
