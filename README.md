## Introduction

The script run TMHMM on protein sequences and help in curating the predicted transmembrane motifs. The transmembrane motifs have hydrophobic amino acids. The sequence before transmembrane motif is pre-transmembrane and the sequence after transmembrane motif is post-transmembrane sequence. The predicted transmembrane motifs should begin and end at hydrophobic amino acids. If the predicted start and end positions have non hydrophobic amino acid, it is pushed to pre and post transmembrane sequence. If the end of pre-transmembrane or the start of post-transmembrane is a hydrophobic amino acid, it is added to transmembrane sequence. For easy readability, the character hyphens are added before and after transmembrane motif sequence.

Currently, the script works on sequences with one transmembrane sequence.

## Requirements

1) python v3.6+
2) TMHMM for transmembrane prediction 
