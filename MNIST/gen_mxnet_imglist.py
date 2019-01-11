import os
import sys

input_path = sys.argv[1].rstrip(os.sep)

out_path = sys.argv[2]

filenames = os.listdir(input_path)
with open(out_path, 'w') as f:
    for i, filename in enumerate(filenames):
        filepath = os.sep.join([input_path, filename])
        label = filename[: filename.rfind('.')].split('_')[1]

        line = '{}\t{}\t{}\n'.format(i, label, filepath)
        f.write(line)
