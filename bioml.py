# bioml.py

def gc_content(sequence: str) -> float:
    """Calculate the GC content of a DNA sequence as a percentage."""
    s = str(sequence).upper()
    if not s:
        return 0.0
    
    # Count G and C bases
    gc_count = s.count("G") + s.count("C")
    return (gc_count / len(s)) * 100
