import os
def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))
