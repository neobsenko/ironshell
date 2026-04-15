"""Ironshell Redaction Engine: BERT NER + regex hybrid logic."""

from typing import Dict, List, Tuple
import re

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
    """Redact sensitive entities in text - RAM only processing."""
    regex_spans = detect_regex(text) + detect_context_triggers(text)
    dict_spans = (
        detect_dictionary(text)
        + detect_dictionary_orgs(text)
        + detect_name_morphology(text)
    )
    spacy_spans = detect_spacy(text) if use_spacy else []
    
    spans = merge_spans(regex_spans, dict_spans, spacy_spans, text=text)

    type_counters: Dict[str, int] = {}
    value_to_placeholder: Dict[Tuple[str, str], str] = {}
    mapping: Dict[str, str] = {}

    replacements: List[Tuple[int, int, str]] = []
    for start, end, entity_type, original in spans:
        key = (entity_type, original)
        placeholder = value_to_placeholder.get(key)
        if placeholder is None:
            type_counters[entity_type] = type_counters.get(entity_type, 0) + 1
            placeholder = f"[{entity_type}_{type_counters[entity_type]}]"
            value_to_placeholder[key] = placeholder
            mapping[placeholder] = original
        
        replacements.append((start, end, placeholder))

    redacted = text
    for start, end, placeholder in sorted(replacements, key=lambda r: -r[0]):
        redacted = redacted[:start] + placeholder + redacted[end:]

    return redacted, mapping