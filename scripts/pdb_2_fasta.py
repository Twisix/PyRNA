#!/usr/bin/env python3
"""
This script takes as first argument a PDB ID, extracts the RNA sequences and prints them using the FASTA format
"""

import sys
from pyrna.db import PDB
from pyrna.model import Guanine
from pyrna.parsers import parse_pdb, to_fasta

def fetch(pdb_id):
    pdb = PDB()
    content = pdb.get_entry(pdb_id)
    print(to_fasta([ts.rna for ts in parse_pdb(content)]))  



if __name__ == "__main__":
    g = Guanine()
    custom = {
        "N1": (0.0, 0.0, 0.0),
        "N2": (1.0, 1.0, 1.0),
        "C2": (2.0, 2.0, 2.0),
        "N3": (3.0, 3.0, 3.0),
        "C4": (4.0, 4.0, 4.0),
        "C5": (5.0, 5.0, 5.0),
        "C6": (6.0, 6.0, 6.0),
        "O6": (7.0, 7.0, 7.0),
        "N7": (8.0, 8.0, 8.0),
        "C8": (9.0, 9.0, 9.0),
        "N9": (10.0, 10.0, 10.0),
        }
    g2 = Guanine(custom)
    print(g2.residue_name)
    print(g.residue_name)
    if len(sys.argv) < 2:
        print("Usage: pdb2_fasta.py PDB_ID (try for example: pdb2_fasta.py 1HR2)")
        sys.exit()
    fetch(sys.argv[1])