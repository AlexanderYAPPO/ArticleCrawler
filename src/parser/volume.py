from typing import Iterator

URL_VOLUME_TEMPLATE = "https://www.nature.com/nm/volumes/%s"
URL_ISSUE_PART_TEMPLATE = "/issues/%s"
LAST_VOLUME = 31
LAST_ISSUE = 12

def yield_volume_urls(start=1) -> Iterator[str]:
    for volume in range(start, LAST_VOLUME + 1):
        yield URL_VOLUME_TEMPLATE % volume

def yield_issue_urls_for_volume(volume_url: str) -> Iterator[str]:
    for issue in range(1, LAST_ISSUE + 1):
        yield volume_url + URL_ISSUE_PART_TEMPLATE % issue

def yield_issue_urls(start=1) -> Iterator[str]:
    for volume_url in yield_volume_urls(start):
        for issue_url in yield_issue_urls_for_volume(volume_url):
            yield issue_url
