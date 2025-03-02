import sys

from src.lib import formatter
from src.parser import issue as issue_parser, volume
from src.entity import issue

sys.stdout.reconfigure(encoding='utf-8')

def run():
    print(issue.Issue.produce_keys_tsv())
    for issue_url in volume.yield_issue_urls(start=16):
        try:
            fetch_data_for_issue(issue_url)
        except Exception as e:
            print(f"Error fetching issue {issue_url}: {e} {e.__class__}")

def fetch_data_for_issue(issue_url: str):
    i = issue_parser.get_issue(issue_url)
    issue_data = i.tsv_list()
    for i in issue_data:
        print(i)

    # str_to_print = formatter.list_of_dicts_to_list_of_tsv(issue_data)
    #
    # for article in str_to_print:
    #     print(article)


if __name__ == "__main__":
    run()
