from src.parser import url, issue as issue_parser, article as article_parser

def fetch_data_for_issue(issue_url: str):
    issue = issue_parser.get_issue(issue_url)
    for tsv_str in issue.tsv_list():
        print(tsv_str)


# def print_metrics_for_article(article_url: str):
#     try:
#         metrics = article_parser.get_metrics(article_url)
#     except Exception as e:
#         print(f"Failed to retrieve metrics for {article_url}. Error: {e}")
#         return
#     print(metrics.get_article_accesses_readable())
#     print(metrics.get_web_of_science_readable())
#     print(metrics.get_cross_ref_readable())
#     print(metrics.get_almetric().get_score_readable())
#     print(metrics.get_almetric().get_details_readable())