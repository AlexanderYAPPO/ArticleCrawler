from typing import Dict, List, Tuple, Set

import requests
import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from src.entity import issue
from src.parser import article as article_parser
from src.parser import url as url_parser

def get_issue(url: str) -> issue.Issue:
    session = requests_cache.CachedSession(backend="filesystem", use_cache_dir=True)
    response = session.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1", class_="u-h2 u-mb-0 u-mr-8").get_text(strip=True)

    _, _, dois = _get_cover_info(soup)

    article_links = _get_links_by_section(soup, url_parser.get_base_url(url))
    issue_articles = []
    for section, links in article_links.items():
        for link in links:
            article = article_parser.get_article(link)
            article.used_on_cover = url_parser.fetch_doi_from_article_url(article.url) in dois
            issue_articles.append((article, section))

    return issue.Issue(url, title, issue_articles)

def _get_cover_info(soup: BeautifulSoup) -> Tuple[str, str, Set[str]]:
    volume_cover_node = soup.find("div", class_="app-volumes-cover__copy")
    if volume_cover_node is None:
        return "", "", set()
    title = volume_cover_node.find("h2").get_text(strip=True)
    description = volume_cover_node.find("p").get_text(strip=True)

    links = [a['href'] for a in volume_cover_node.find_all('a', href=True)]
    dois = {url_parser.fetch_doi_from_article_url(u) for u in links}

    return title, description, dois

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
