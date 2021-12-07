import _pickle as cPickle
import matplotlib.pyplot as plt
from Bio.Blast import NCBIWWW
import re
with open('./diabetes_results/saved_dictionary.pkl', 'rb') as f:
    items_in_cluster_dict = cPickle.load(f)

#find the cluster that contains the most
print(items_in_cluster_dict[max(items_in_cluster_dict, key=items_in_cluster_dict.get)])
#print(items_in_cluster_dict)

cluster = []
amount_in_cluster = []

items_in_cluster_dict = dict(sorted(items_in_cluster_dict.items(), key=lambda item: item[1]))

for key in items_in_cluster_dict:
    cluster.append(key)
    amount_in_cluster.append(items_in_cluster_dict[key])


cluster = cluster[::-1]
amount_in_cluster = amount_in_cluster[::-1]
print(amount_in_cluster[0:10])

top_ten = 3
while top_ten < 10:
    index = 1

    # find a sequence index that belongs in the cluster
    with open('./diabetes_results/clusterid.txt','r') as f:
        index = 1
        for group in f.readlines():
            if str(group).strip('\n') == str(cluster[top_ten]).strip('\n'):
                break
            index += 1

    #find the sequence that belongs in the cluster using the index
    with open('./diabetes_results/mapped_sequences.txt','r') as f:
        sequences = list(f.readlines())
        print(sequences[index].strip('\n'))




    print('identifying sequence')
    result_handle = NCBIWWW.qblast("blastn", "nt", sequences[index])
    print("Recieved Results")
    xml_results = result_handle.read()
    #print(xml_results)
    hit_def = re.search(r'.*<Hit_def>(.*)<\/Hit_def>',xml_results)
    hit_accession = re.search(r'.*<Hit_accession>(.*)<\/Hit_accession>',xml_results)
    organism_type = hit_def.group(1)
    accession_num = hit_accession.group(1)

    print(f'Organism : {organism_type}')

    with open('./diabetes_results/top_ten_3.txt','a') as file:
        file.write(str(organism_type)+","+str(amount_in_cluster[top_ten])+","+str(sequences[index])+"\n")

    top_ten +=1



plt.bar(cluster[0:10],amount_in_cluster[0:10])
plt.show()
