import os
import shutil

new_names = []
with open('sky_names.txt', 'r') as f:
	for line in f:
		new_names.append(line.rstrip())
f.close()
for i in range(0, 36):
	shutil.copy(os.getcwd() + '\\sky_mp_village_ft.iwi', os.getcwd() + f'\\sky_mp_village_ft{i}.iwi')

f_list = os.listdir(os.getcwd())
f_list.pop(f_list.index('rename.py'))
f_list.pop(f_list.index('sky_mp_village_ft.iwi'))
f_list.pop(f_list.index('sky_names.txt'))
for c, x in enumerate(f_list):
	os.rename(x, new_names[c])