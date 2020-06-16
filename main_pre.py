import os

from Folds import Folds
# from bio_conll import BIO_conll
import argparse

from json2conll import Json2conll

parser = argparse.ArgumentParser()
parser.add_argument("-data", "--data", type=str, default="data/ee_dev,data/ee_train")
parser.add_argument("-folds_path", "--folds_path", type=str, default="data/ner_folds,ff")
parser.add_argument("-bio_paths", "--bio_paths", type=str, default="data/ner_folds_biobert,ff")
parser.add_argument("-n_folds", "--n_folds", type=int, default=5)
parser.add_argument('--entity', '-entity', type=str, default='reaction_product')
parser.add_argument('--tagger', '-tagger', type=str, default='averaged_perceptron_tagger')
parser.add_argument('--vocab_file', '-vocab_file', type=str, default='med_mentions_model/vocab.txt')
parser.add_argument('--do_lower_case', '-do_lower_case', type=bool, default=True)

args = parser.parse_args()

dirs = args.data.split(",")
fold_dirs = args.folds_path.split(",")
bio_dirs = args.bio_paths.split(",")
entity = ["disease", "body_location", "severity", "symptom", "treatment", "drug", "course", "modificator"]
tagger = args.tagger
vocab = args.vocab_file
lower_case = args.do_lower_case
# for i in range(len(dirs)):
#     if "train" in dirs[i]:
#         out_file = "data/rel_train.json"
#     else:
#         out_file = "data/rel_test.json"
folds = Folds("data/train", "data", args.n_folds, "data/train.json")
folds.get_folds()

#conll = Json2conll("data/train.json", "train", entity, tagger, vocab, lower_case)
#conll.get_conlls()
#conll = Json2conll("data/rel_test_u.json", "test", entity, tagger, vocab, lower_case)
#conll.get_conlls()
#     bio = BIO_conll(fold_dir,bio_dir)
#     bio.get_bio()
