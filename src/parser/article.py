from typing import Dict, Tuple
from urllib.parse import urlparse, parse_qs

import requests
import requests_cache
from bs4 import BeautifulSoup

from src.entity import article
from src.parser.url import build_article_metrics_link
from src.entity.citation_summary import CitationSummaryBuilder, AlmetricScoreBuilder, CitationSummary

ARTICLE_ACCESSES_NAME = "Article Accesses"
WEB_OF_SCIENCE_NAME = "Web of Science"
CROSS_REF_NAME = "CrossRef"

def _parse_int(value: str) -> int:
    try:
        value = value.lower().replace(",", "").replace("k", "000").replace("m", "000000")
        return int(value)
    except ValueError:
        return -1


def get_article(article_url) -> article.Article:
    metrics_url = build_article_metrics_link(article_url)
    session = requests_cache.CachedSession(backend="filesystem", use_cache_dir=True)
    response = session.get(metrics_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1", class_="c-article-metrics__heading u-h1").get_text(strip=True)
    metrics = _get_metrics(soup)
    return article.Article(url=article_url, title=title, metrics=metrics)

def _get_metrics(soup: BeautifulSoup) -> "CitationSummary":
    metrics_builder = CitationSummaryBuilder()
    citations = soup.find_all("dl", class_="c-article-metrics__access-citation")
    for citation in citations:
        dt_value = citation.find("dt").get_text(strip=True)
        dd_value = citation.find("dd").get_text(strip=True)
        count = _parse_int(dt_value)
        if dd_value == ARTICLE_ACCESSES_NAME:
            metrics_builder = metrics_builder.set_article_accesses(count)
        elif dd_value == WEB_OF_SCIENCE_NAME:
            metrics_builder = metrics_builder.set_web_of_science(count)
        elif dd_value == CROSS_REF_NAME:
            metrics_builder = metrics_builder.set_cross_ref(count)

    almetrics = AlmetricScoreBuilder()
    almetric_score, almetric_details = _fetch_almetric_data(soup)
    almetrics = almetrics.set_score(almetric_score).set_details(almetric_details)

    metrics_builder = metrics_builder.set_almetric(almetrics.build())

    return metrics_builder.build()

def _fetch_almetric_data(soup: BeautifulSoup) -> Tuple[int, Dict[str, int]]:
    almetric_score = _fetch_almetric_score(soup)

    almetric_detail_items = soup.find_all("li", class_="u-list-reset")
    almetric_details = {}
    for item in almetric_detail_items:
        text = item.get_text(strip=True)
        if text:
            score, source = text.split(maxsplit=1)
            almetric_details[source] = int(score)

    return almetric_score, almetric_details

def _fetch_almetric_score(soup: BeautifulSoup) -> int:
    donut = soup.find("div", class_="c-article-metrics__altmetric-donut")
    if donut is None:
        return -1
    donut_image = donut.find("div", class_="c-article-metrics__image")
    if donut_image is None:
        return -1
    image = donut_image.find("img")
    if image is None or image.get("src") is None:
        return -1
    almetric_url = image.get("src")

    parsed_url = urlparse(almetric_url)
    query_params = parse_qs(parsed_url.query)
    score = query_params.get("score", "?")[0]
    return _parse_int(score)