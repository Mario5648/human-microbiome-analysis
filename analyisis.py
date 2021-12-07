from Bio.Blast import NCBIWWW
from Bio import SeqIO
import re


#activate conda 'conda activate qiime2-bioinformatics-project'


sequences = SeqIO.parse("./Microbiome_Dataset_Healthy/SRS011405.fna", "fasta")

count = 1
for sequence in sequences:
    try:
        print(f"Searching Sequence : {count}")
        #print(sequence)
        #print(sequence.seq)
        #result_handle = NCBIWWW.qblast("blastn", "nt", sequence.format("fasta"))
        result_handle = NCBIWWW.qblast("blastn", "nt", sequence.seq)
        print("Recieved Results")
        xml_results = result_handle.read()
        #print(xml_results)
        hit_def = re.search(r'.*<Hit_def>(.*)<\/Hit_def>',xml_results)
        hit_accession = re.search(r'.*<Hit_accession>(.*)<\/Hit_accession>',xml_results)
        organism_type = hit_def.group(1)
        accession_num = hit_accession.group(1)
        print('Found Organism')
        with open('organism_type.csv','a') as file:
            print('Reading File')
            file.write(str(organism_type)+','+str(accession_num)+"\n")
            print('Wrote to File!')
        count += 1
    except:
        print('Failed to search!')
