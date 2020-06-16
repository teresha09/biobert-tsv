import shutil
import os

for i in range(3):
    for filename in os.listdir("data/main{}".format(i)):
        shutil.copyfile(os.path.join("data/main{}".format(i), filename),
                        "data/train/{}_{}".format(i,filename))
