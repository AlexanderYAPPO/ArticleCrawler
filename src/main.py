import requests_cache

from src.parser import flow, volume

if __name__ == "__main__":
    issue_url = "https://www.nature.com/nm/volumes/28/issues/1"
    flow.fetch_data_for_issue(issue_url)

    # session = requests_cache.CachedSession(backend="filesystem", use_cache_dir=True)
    #
    # for url in volume.yield_issue_urls():
    #     print(url)
    #     r = session.get(url)
    #     if r.status_code != 200:
    #         print(r)
    #
