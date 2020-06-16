f = open("data/train.tsv")
text_file = open("data/test_texts", "a+")
labels_file = open("data/test_labels.txt", "a+")
words = ""
labels = ""
for line in f:
    if line != "\n":
        if line.split("\t")[0] in ['', ' ']:
            print(line)
        words += line.split("\t")[0] + " "
        labels += line.split("\t")[1][:-1] + " "
    else:
        words = words[:-1] + "\n"
        labels = labels[:-1] + "\n"
        text_file.write(words)
        labels_file.write(labels)
        words = ""
        labels = ""
