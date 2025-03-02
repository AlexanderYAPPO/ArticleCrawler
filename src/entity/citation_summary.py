from typing import Dict, List
from src.entity.readable_score import _ReadableScore


class AlmetricScore:
    _score: _ReadableScore
    _details: Dict[str, int]

    def __init__(self, score: _ReadableScore, details: Dict[str, int]):
        self._score = score
        self._details = details

    def get_score_readable(self) -> str:
        return self._score.get_readable()

    def get_details_readable(self) -> str:
        if not self._details:
            return "N/A"
        return ', '.join([f"{key}: {value}" for key, value in self._details.items()])

    def tsv(self) -> str:
        return f"{self.get_score_readable()}\t{self.get_details_readable()}"

    def dict(self):
        return {
            "almetric_score": self.get_score_readable(),
            "almetric_details": self.get_details_readable()
        }

    def key_value(self) -> List:
        return [
            ("almetric_score", self.get_score_readable()),
            ("almetric_details", self._details)
        ]


class CitationSummary:
    _article_accesses: _ReadableScore
    _web_of_science: _ReadableScore
    _cross_ref: _ReadableScore
    _almetric: AlmetricScore

    def __init__(self, article_accesses: _ReadableScore, web_of_science: _ReadableScore, cross_ref: _ReadableScore, almetric: AlmetricScore):
        self._article_accesses = article_accesses
        self._web_of_science = web_of_science
        self._cross_ref = cross_ref
        self._almetric = almetric

    def get_article_accesses_readable(self) -> str:
        return self._article_accesses.get_readable()

    def get_web_of_science_readable(self) -> str:
        return self._web_of_science.get_readable()

    def get_cross_ref_readable(self) -> str:
        return self._cross_ref.get_readable()

    def get_almetric(self) -> AlmetricScore:
        return self._almetric

    def tsv(self) -> str:
        return f"{self.get_article_accesses_readable()}\t{self.get_web_of_science_readable()}\t{self.get_cross_ref_readable()}\t{self.get_almetric().tsv()}"

    def dict(self):
        d = self._almetric.dict()
        d["article_accesses"] = self.get_article_accesses_readable()
        d["article_web_of_science"] = self.get_web_of_science_readable()
        d["article_cross_ref"] = self.get_cross_ref_readable()
        return d

    def key_value(self) -> List:
        return [
            ("article_accesses", self.get_article_accesses_readable()),
            ("article_web_of_science", self.get_web_of_science_readable()),
            ("article_cross_ref", self.get_cross_ref_readable()),
            *self._almetric.key_value()
        ]

class AlmetricScoreBuilder:
    def __init__(self):
        self._score = _ReadableScore.default()
        self._details = {}

    @staticmethod
    def default() -> 'AlmetricScore':
        return AlmetricScore(_ReadableScore.default(), {})

    def set_score(self, score: int):
        self._score = _ReadableScore(score)
        return self

    def set_details(self, details: Dict[str, int]):
        self._details = details
        return self

    def build(self):
        return AlmetricScore(self._score, self._details)

class CitationSummaryBuilder:
    def __init__(self):
        self._articleAccesses = _ReadableScore.default()
        self._webOfScience = _ReadableScore.default()
        self._crossRef = _ReadableScore.default()
        self._almetric = AlmetricScoreBuilder.default()

    def set_article_accesses(self, article_accesses: int):
        self._articleAccesses = _ReadableScore(article_accesses)
        return self

    def set_web_of_science(self, web_of_science: int):
        self._webOfScience = _ReadableScore(web_of_science)
        return self

    def set_cross_ref(self, cross_ref: int):
        self._crossRef = _ReadableScore(cross_ref)
        return self

    def set_almetric(self, almetric: AlmetricScore):
        self._almetric = almetric
        return self

    def build(self):
        return CitationSummary(self._articleAccesses, self._webOfScience, self._crossRef, self._almetric)
