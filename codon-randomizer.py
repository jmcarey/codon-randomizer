# -*- coding: utf-8 -*-
"""
Codon Randomizer
Given an animo acid sequence, returns a nucleotide sequence with a random codon
selected from translation table 1 for that amino acid.

Created on Tue Sep 22 13:45:24 2020

@author: Jordan Carey
"""

import random, sys

amino = {
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAT', 'AAC'],
    'D': ['GAT', 'GAC'],
    'B': ['AAT', 'AAC', 'GAT', 'GAC'],
    'C': ['TGT', 'TGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'Z': ['CAA', 'CAG', 'GAA', 'GAG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'H': ['CAT', 'CAC'],
    'I': ['ATT', 'ATC', 'ATA'],
    'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
    'K': ['AAA', 'AAG'],
    'M': ['ATG'],
    'F': ['TTT', 'TTC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'W': ['TGG'],
    'Y': ['TAT', 'TAC'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'START': ['ATG'],
    'STOP': ['TAA', 'TGA', 'TAG']
}

if len(sys.argv) != 3:
    raise ValueError("Please provide input and output file.")
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    sequence =  f.read().upper()
    sequence = sequence.replace(' ', '').replace('\t', '').replace('\n', '')


try:
   codons = [random.choice(amino[x]) for x in sequence]
except KeyError:
    print('Unrecognized character in sequence.')
nucleotides = ''.join(codons)
with open(output_file, 'w') as f:
    f.write(nucleotides)