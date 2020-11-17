# jgi2sra_mapper
A small dirty script to get a mapping from Gold Stamp ID from JGI to an SR-ID easity downloadable by `fastq-dump`.
Really convinent if you want to use the metagenomic libraries used in Nayfach et al's for further analysis, about half of the libraries can be obtained with this. Probably more could be obtained with more clever queries, but I am lazy, and it was good for my purposes.

Can easily be modified to obtaine other samples.

## REQUIREMENTS

Needs `biopython`, easily installable with `pip install biopython` for example

## USAGE

```
python jgi2sra_mapper.py NCBI_USER GOLD_IDS OUTPUT_FILE
```

with `NCBI_USER` the email you use to log into NCBI, `GOLD_IDS` a text file with a 'Gold Stamp ID', typically an ID from IMG/JGI starting with Gp, the file provided with this archive (`GEMs_metagenomes_ids.txt`) is the third column of Supplemental Table 1 of Nayfach et al. `OUTPUT_FILE` is the name of the file you want the output saved in.

## Acknowlegments
Thanks Maliheh Mehrshad, Julia Nuy, Alejandro Rodriguez Gijón and Sarahi L. Garcia, as well as the whole team at IMG and JGI for the 'inspiration' for this...
