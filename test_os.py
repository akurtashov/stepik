import os
DIR = r'main'
EXT = 'py'

def get_ext(file_name):
    return file_name.split('.')[-1]

result_dirs = []
for root, dirs, files in os.walk(DIR):
    # print(root, dirs, files)
    for f in files:
        if get_ext(f) == EXT:
            if root not in result_dirs:
                result_dirs.append(root)
result_dirs.sort()
print(result_dirs)
with open('out.txt','w') as o_f:
    for d in result_dirs:
        o_f.write(d+'\n')

