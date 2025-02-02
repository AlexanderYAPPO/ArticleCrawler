from typing import Dict, List, Tuple

import requests
import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from src.entity import issue
from src.parser.url import get_base_url
from src.parser import article as article_parser

def get_issue(url: str) -> issue.Issue:
    session = requests_cache.CachedSession(backend="filesystem", use_cache_dir=True)
    response = session.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article_links = _get_links_by_section(soup, get_base_url(url))

    issue_articles = []
    for section, links in article_links.items():
        for link in links:
            article = article_parser.get_article(link)
            issue_articles.append((article, section))

    title, description = _get_cover_title_and_description(soup)
    print(title, description)

    return issue.Issue(url, 2021, 1, issue_articles)

def _get_cover_title_and_description(soup: BeautifulSoup) -> Tuple[str, str]:
    volume_cover_node = soup.find("div", class_="app-volumes-cover__copy")
    if volume_cover_node is None:
        return "", ""
    title = volume_cover_node.find("h2").get_text(strip=True)
    description = volume_cover_node.find("p").get_text(strip=True)
    return title, description

def _get_links_by_section(soup: BeautifulSoup, base_url: str) -> Dict[str, List[str]]:
    sections = {}

    for section in soup.find_all("section", class_="u-mb-48 u-mt-48"):
        section_id = section.get("id", "Unknown ID")

        articles = []
        for article in section.find_all("article"):
            link_tag = article.find("a", href=True)
            if link_tag:
                relative_link = link_tag["href"]
                full_link = urljoin(base_url, relative_link)
                articles.append(full_link)

        if articles:
            sections[section_id] = articles

    return sections
