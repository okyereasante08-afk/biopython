from bioml import gc_content
for s in ["ATGC", "GGGGCCCC", "ATATATAT"]:
    print(s, "->", round(gc_content(s), 1), "%")
