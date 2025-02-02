import sys

from src.lib import formatter
from src.parser import issue as issue_parser

sys.stdout.reconfigure(encoding='utf-8')

def fetch_data_for_issue(issue_url: str):
    issue = issue_parser.get_issue(issue_url)
    issue_data = issue.dict_flat()

    str_to_print = formatter.list_of_dicts_to_list_of_tsv(issue_data)

    for article in str_to_print:
        print(article)


if __name__ == "__main__":
    issue_url = "https://www.nature.com/nm/volumes/30/issues/12"
    fetch_data_for_issue(issue_url)

