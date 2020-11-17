# jgi2sra_mapper
A small dirty script to get a mapping from Gold Stamp ID from JGI to an SR-ID easity downloadable by `fastq-dump`.
Really convinent if you want to use the metagenomic libraries used in Nayfach et al 2020's for further analysis, about half of the libraries can be obtained with this. Probably more could be obtained with more clever queries, but I am lazy, and it was good for my purposes.

Can easily be modified to obtaine other samples.

## REQUIREMENTS

Needs `biopython`, easily installable with `pip install biopython` for example

## USAGE

```
python jgi2sra_mapper.py NCBI_USER GOLD_IDS OUTPUT_FILE
```

with `NCBI_USER` the email you use to log into NCBI, `GOLD_IDS` a text file with a 'Gold Stamp ID', typically an ID from IMG/JGI starting with Gp, the file provided with this archive (`GEMs_metagenomes_ids.txt`) is the third column of Supplemental Table 1 of Nayfach et al 2020 `OUTPUT_FILE` is the name of the file you want the output saved in (the output `gold2sra.json` is the one generated with `GEMs_metagenomes_ids.txt`).


## Acknowlegments
Thanks Maliheh Mehrshad, Julia Nuy, Alejandro Rodriguez Gijón and Sarahi L. Garcia, as well as the whole team at IMG/JGI, and the authors of Nayfach et al 2020 for the 'inspiration' for this...

## REFERENCES

Nayfach, S., Roux, S., Seshadri, R. et al. A genomic catalog of Earth’s microbiomes. Nat Biotechnol (2020). https://doi.org/10.1038/s41587-020-0718-6

## CITE

You can cite this through the DOI : 10.17044/scilifelab.13246817 
