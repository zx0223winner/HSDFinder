import os
import sys

root = sys.argv[1]
folder = os.listdir(root)
folder.sort()
result_list = []
for file in sorted(folder):
	file_paths = os.path.join(root, file)
	if not os.path.isdir(file_paths) and file.split('.')[-1] == 'tsv':
		with open (file_paths, 'r') as f:
			lines = f.read().split("\n")
			i = 0
			j = 0
			k = 0
			for line in lines:
				if line != "":
					array =line.split("\t")
					array2 = array[1].split("; ")
					if len(array2) == 2:
						i = i + 1
					elif len(array2) == 3:
						j =j + 1
					elif len(array2) >= 4:
						k = k + 1
		result_list.append(file.split('.')[0] + '\t' + str(i) + '\t' + str(j) + '\t' + str(k))
		#print ("2-group: "+ str(i) + "\n" + "3-group: " + str(j) +'\n' + ">3-group: " + str(k) + '\n')
with open(os.path.join(root, 'result_groups.tsv'), 'w') as out:
    out.write("name\t2-group\t3-group\t>=4-group\n")
    for r in result_list:
    	out.write(r + '\n')