from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from src.parser.url import get_base_url

def get_links_by_section(url: str) -> Dict[str, List[str]]:
    base_url = get_base_url(url)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    sections = {}

    for section in soup.find_all('section', class_='u-mb-48 u-mt-48'):
        section_id = section.get('id', 'Unknown ID')

        articles = []
        for article in section.find_all('article'):
            link_tag = article.find('a', href=True)
            if link_tag:
                relative_link = link_tag['href']
                full_link = urljoin(base_url, relative_link)
                articles.append(full_link)

        if articles:
            sections[section_id] = articles

    return sections
