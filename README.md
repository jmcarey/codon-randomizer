# codon-randomizer
Python script to convert amino acid sequence to nucleotide sequence by selecting random codons

Randomize the codons coding for your amino acids to reduce repetition in the coding sequence for a protein with repetitive domains.

Uses standard code. To use alternative codons, edit the dictionary at the start of codon-randomizer.py.

Run the script from the terminal with the input and output file as arguments.
python codon-randomizer.py amino_acids.txt nucleotides.txt

Input file should contain only the amino acid sequence, can contain whitespace.
Output will be nucleotide sequence as unformatted text.
