from redact.detector import redact
from pathlib import Path

def test_ironshell_redaction():
    # Load synthetic contract
    sample_path = Path("training/synthetic/contract_01.txt")
    text = sample_path.read_text(encoding="utf-8")
    
    print("--- ORIGINAL TEXT ---")
    print(text)
    
    # Run redaction
    redacted, mapping = redact(text, use_spacy=False)
    
    print("\n--- REDACTED TEXT ---")
    print(redacted)
    
    print("\n--- TOKEN MAP (IN RAM ONLY) ---")
    for token, val in mapping.items():
        print(f"{token}: {val}")

if __name__ == "__main__":
    test_ironshell_redaction()