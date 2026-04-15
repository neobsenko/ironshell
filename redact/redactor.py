"""Core redaction logic: detect, replace, and produce a mapping."""

from typing import Dict, List, Tuple

from redact.detectors import (
    detect_dictionary,
    detect_dictionary_orgs,
    detect_regex,
    detect_spacy,
    merge_spans,
)
from redact.detectors.context_triggers import detect_context_triggers
from redact.detectors.name_morphology import detect_name_morphology

def redact(text: str, use_spacy: bool = True) -> Tuple[str, Dict[str, str]]:
    # ... (content remains the same logic-wise, just updated imports) ...