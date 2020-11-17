import sys, os
from Bio import Entrez
from os.path import join as pjoin
from xml.etree import ElementTree as ET
import sys
import json

script, username, gems_sup_file, outfile = sys.argv

#gems_sup_file = "GEMs_metagenomes_ids.txt"
#outfile = "gold2sra.json"

def parse_exp_summary(sra_summary):
    xxml = sra_summary['ExpXml']
    try :
        sra_id =ET.fromstring(sra_summary[0]['Runs']).attrib['acc']
    except :
        sra_id =ET.fromstring("<Data>" + sra_summary['Runs']+ "</Data>")[0].attrib['acc']

    dat = ET.fromstring("<Data>" + xxml + "</Data>")
    srr = [child.attrib['acc'] for child in dat if child.tag == "Sample"][0]

    return (srr, sra_id)



Entrez.email = username

query = '({orgs}) AND "strategy wgs"[Properties] AND "platform illumina"[Properties]'

sra_ids = Entrez.read(Entrez.esearch(db="biosample", term = 'DOE Joint Genome Institute' , retmax=300000))['IdList']
def print_run(x,i):
    print("Querying ids", i, "to", i+10000 ,"out of", len(sra_ids))
    return x
summary = sum([print_run(Entrez.read(Entrez.esummary(db="biosample", id = ",".join(sra_ids[i:i+10000]), retmax=10000))['DocumentSummarySet']['DocumentSummary'],i) for i in range(0,len(sra_ids), 10000)], [])

gold2sra = {[f for f in entry['Identifiers'].split(";") if "DOE" in f][0].strip().split()[-1] : [f for f in entry['Identifiers'].split(";") if "SRA" in f][0].strip().split()[-1] for entry in summary if "DOE" in entry['Identifiers'] and "SRA" in entry['Identifiers']}

with open(gems_sup_file) as handle:
    samples = {l.strip() for l in handle}

matching_samples = {k : v for k, v in gold2sra.items() if k in samples}

query2 = " OR ".join(matching_samples.values())
sra_ids2 = Entrez.read(Entrez.esearch(db="SRA", term = query2 , retmax=300000))['IdList']
summary2 = Entrez.read(Entrez.esummary(db="SRA", id = ",".join(sra_ids2), retmax = 10000))
srs2srr = dict([parse_exp_summary(s) for s in summary2])
gold2sra = {k : srs2srr[v] for k,v in matching_samples.items() if v in srs2srr}

with open(outfile,"w") as handle:
    json.dump(gold2sra,handle, indent=4, sort_keys=True)

"for f in `ls fna/`; do echo $f ; unpigz -c fna/$f | sed 's/>.*\(_[0-9]*\)/>'${f%%.fna.gz}'\1/'  | pigz -c >> GEMs.fna; done"
