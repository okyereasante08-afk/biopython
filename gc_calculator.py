from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

def gc_content(sequence):
  """Return GC content of a DNA sequence as a percentage."""
  s = str(sequence).upper()
  gc = s.count("G") + s.count("C")
  return 100 * gc/ len(s)

dna = Seq("AGCTCAACGTTAAAGGGAGAGCGAGAGCTTCCTA")
print(f"My function : {gc_content(dna):.1f}%")
print(f"Biopython   : {gc_fraction(dna) * 100:.1f}%")
