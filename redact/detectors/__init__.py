"""Detection modules for Ironshell."""

from redact.detectors.regex import detect_regex
from redact.detectors.dictionary import detect_dictionary
from redact.detectors.dictionary_orgs import detect_dictionary_orgs
from redact.detectors.nlp import detect_spacy
from redact.detectors.merger import merge_spans

__all__ = [
    "detect_regex",
    "detect_dictionary",
    "detect_dictionary_orgs",
    "detect_spacy",
    "merge_spans",
]