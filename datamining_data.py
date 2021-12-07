import matplotlib.pyplot as plt


healthy_subject = {'subject_1':{},'subject_2':{},'subject_3':{},'subject_4':{},'subject_5':{}}
obese_subject = {'subject_1':{},'subject_2':{},'subject_3':{}}
diabetic_subject = {'subject_1':{},'subject_2':{}}

#healthy patients
index = 1
for subject in healthy_subject:
    with open(f'./healthy_results/{subject}/top_ten_{index}.txt') as file:
        for line in file.readlines():
            information_list = line.split(',')                   #Amount Found,DNA Sequence
            healthy_subject[subject][str(information_list[0])] = [str(information_list[1]),str(information_list[2].strip('\n'))]
    index +=1


#obese patients
index = 1
for subject in obese_subject:
    with open(f'./obese_results/{subject}/top_ten_{index}.txt') as file:
        for line in file.readlines():
            information_list = line.split(',')                   #Amount Found,DNA Sequence
            obese_subject[subject][str(information_list[0])] = [str(information_list[1]),str(information_list[2].strip('\n'))]
    index +=1

#diabetic patient
index = 1
for subject in diabetic_subject:
    with open(f'./diabetes_results/{subject}/top_ten_{index}.txt') as file:
        for line in file.readlines():
            information_list = line.split(',')                   #Amount Found,DNA Sequence
            diabetic_subject[subject][str(information_list[0])] = [str(information_list[1]),str(information_list[2].strip('\n'))]
    index +=1

'''

healthy_graph_info = {}
for subject in healthy_subject:
    for microbe in healthy_subject[subject]:
        if microbe not in healthy_graph_info:
            healthy_graph_info[microbe] = int(healthy_subject[subject][microbe][0])
        else:
            healthy_graph_info[microbe] += int(healthy_subject[subject][microbe][0])

sorted_healthy_graph_info = dict(sorted(healthy_graph_info.items(), key=lambda item: item[1]))


healthy_top_ten=[]
for index, key in enumerate(sorted_healthy_graph_info):
    if int(index) < 10:
        healthy_top_ten.append('#CC5C33')
    else:
        healthy_top_ten.append('#33A3CC')

plt.rcParams.update({'font.size': 7})
plt.title('Top 10 Microbes from three Healthy Individuals')
plt.ylabel('Microbes')
plt.xlabel('Amount of Microbes Identified')
plt.barh(list(sorted_healthy_graph_info.keys()),list(sorted_healthy_graph_info.values()), color=healthy_top_ten[::-1])
plt.show()
'''

'''
obese_graph_info = {}
for subject in obese_subject:
    for microbe in obese_subject[subject]:
        if microbe not in obese_graph_info:
            obese_graph_info[microbe] = int(obese_subject[subject][microbe][0])
        else:
            obese_graph_info[microbe] += int(obese_subject[subject][microbe][0])

sorted_obese_graph_info = dict(sorted(obese_graph_info.items(), key=lambda item: item[1]))


obese_top_ten=[]
for index, key in enumerate(sorted_obese_graph_info):
    if int(index) < 10:
        obese_top_ten.append('#CC5C33')
    else:
        obese_top_ten.append('#33A3CC')

plt.rcParams.update({'font.size': 7})
plt.title('Top 10 Microbes from three Obese Individuals')
plt.ylabel('Microbes')
plt.xlabel('Amount of Microbes Identified')
plt.barh(list(sorted_obese_graph_info.keys()),list(sorted_obese_graph_info.values()), color=obese_top_ten[::-1])
plt.show()
'''

diabetes_graph_info = {}
for subject in diabetic_subject:
    for microbe in diabetic_subject[subject]:
        if microbe not in diabetes_graph_info:
            diabetes_graph_info[microbe] = int(diabetic_subject[subject][microbe][0])
        else:
            diabetes_graph_info[microbe] += int(diabetic_subject[subject][microbe][0])

sorted_diabetes_graph_info = dict(sorted(diabetes_graph_info.items(), key=lambda item: item[1]))


diabetes_top_ten=[]
for index, key in enumerate(sorted_diabetes_graph_info):
    if int(index) < 10:
        diabetes_top_ten.append('#CC5C33')
    else:
        diabetes_top_ten.append('#33A3CC')

plt.rcParams.update({'font.size': 7})
plt.title('Top 10 Microbes from three Diabetic Individuals')
plt.ylabel('Microbes')
plt.xlabel('Amount of Microbes Identified')
plt.barh(list(sorted_diabetes_graph_info.keys()),list(sorted_diabetes_graph_info.values()), color=diabetes_top_ten[::-1])
plt.show()
