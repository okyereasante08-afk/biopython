# gc_calculator.py
import sys
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from bioml import gc_content  # Importing from your custom module

def main():
    # Check if the user provided a sequence argument
    if len(sys.argv) < 2:
        print("Usage: python gc_calculator.py <DNA_SEQUENCE>")
        print("Example: python gc_calculator.py ATGCGTAC")
        sys.exit(1)
        
    # Get the sequence from the command line argument
    dna_input = sys.argv[1]
    
    print(f"Analyzing Sequence: {dna_input}\n")
    
    # 1. Calculate using your custom bioml module
    custom_res = gc_content(dna_input)
    print(f"Custom Module (bioml) : {custom_res:.1f}%")
    
    # 2. Verify using Biopython
    try:
        bio_seq = Seq(dna_input)
        biopython_res = gc_fraction(bio_seq) * 100
        print(f"Biopython Verification: {biopython_res:.1f}%")
    except Exception as e:
        print(f"Biopython verification skipped or failed: {e}")

if __name__ == "__main__":
    main()
