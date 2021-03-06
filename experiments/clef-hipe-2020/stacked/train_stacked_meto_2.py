from pathlib import Path
from typing import List

import torch

import flair.datasets
from flair.data import Corpus
from flair.embeddings import (
    TokenEmbeddings,
    WordEmbeddings,
    StackedEmbeddings,
    FlairEmbeddings,
    TransformerWordEmbeddings
)

# 1. get the corpus
corpus: Corpus = flair.datasets.ColumnCorpus(data_folder=Path("../../preprocessed-v1.2/de/"),
                                             train_file="train_meto.txt",
                                             dev_file="dev_meto.txt",
                                             test_file="dev_meto.txt",
                                             column_format={0: "token", 1: "ner"},
                                             tag_to_bioes="ner",
                                             skip_first_line=True)
print(corpus)

# 2. what tag do we want to predict?
tag_type = "ner"

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dictionary.idx2item)

# initialize embeddings
embedding_types: List[TokenEmbeddings] = [
    WordEmbeddings("de-wiki"),
    FlairEmbeddings("de-impresso-hipe-v1-forward", lowercased_lm=True),
    FlairEmbeddings("de-impresso-hipe-v1-backward", lowercased_lm=True),
    #TransformerWordEmbeddings("/mnt/clef-hipe-parser-master/transformers/examples/token-classification/german-large-2", layers="all", use_scalar_mix=True)
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(
    hidden_size=256,
    embeddings=embeddings,
    tag_dictionary=tag_dictionary,
    tag_type=tag_type,
    use_crf=True,
)

# initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(model=tagger, corpus=corpus, use_tensorboard=True)

trainer.train(
    "resources/taggers/baseline-de-stacked-we-fl-meto-3",
    mini_batch_size=16,
    patience=5,
    max_epochs=200,
)
