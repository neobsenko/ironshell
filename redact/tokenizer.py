"""Token map generation and hydration logic for Ironshell."""

import re
from typing import Dict

_PLACEHOLDER_RE = re.compile(
    r"\b(?:PERSON|ORG|ORG_NR|LOCATION|EMAIL|PHONE|URL|SSN|IP|IBAN|PAYMENT_REF|ITEM)_\d+\b"
)

def hydrate(text: str, mapping: Dict[str, str]) -> str:
    """Rehydrate redacted text with original PII values from the token map."""
    def _sub(match: re.Match) -> str:
        placeholder = match.group(0)
        # Strip brackets if they exist in the token map but not the search
        clean_ph = placeholder.strip("[]")
        return mapping.get(placeholder, mapping.get(f"[{placeholder}]", placeholder))

    return _PLACEHOLDER_RE.sub(_sub, text)