from Bio.Cluster import kcluster
from Bio.Cluster import clustercentroids
import numpy as np
from Bio import SeqIO
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import _pickle as cPickle
#read sequences from a file
#Done : SRS011405.fna, SRS014459.fna, SRS018606.fna, SRS042628.fna,SRS1041129.fna"
sequences = SeqIO.parse("./Microbiome_Data_Diabetes/HMP2_J66974_1_ST_T0_B0_0120_ZVBQY1N-6025_APATM.raw.fastq/HMP2_J66974_1_ST_T0_B0_0120_ZVBQY1N-6025_APATM_R2.fastq", "fastq")
sequence_list = []
for sequence in sequences:
    try:
        sequence_list.append(str(sequence.seq)[0:100])
    except:
        pass



with open('mapped_sequences.txt','w') as file:
    for sequence in sequence_list:
        file.write(str(sequence)+"\n")

matrix = np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequence_list])


clusterid, error, nfound = kcluster(matrix, nclusters=100)

with open('clusterid.txt','w') as file:
    for id in clusterid:
        file.write(str(id)+"\n")

items_in_cluster_dict = {}

for n in clusterid:
    if n not in items_in_cluster_dict:
        items_in_cluster_dict[n] = 1
    else:
        items_in_cluster_dict[n] += 1

with open('saved_dictionary.pkl', 'wb') as f:
    cPickle.dump(items_in_cluster_dict, f)

print("Finished Clustering Microbes")
