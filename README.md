# CLEF-HIPE

This repository contains code and models to solve the [HIPE](https://impresso.github.io/CLEF-HIPE-2020/)
(Identifying Historical People, Places and other Entities) evaluation compaign from the [Impresso Project](https://impresso-project.ch/).

It also includes code and models from the following papers:

* [Triple E - Effective Ensembling of Embeddings and Language Models for NER of Historical German](http://ceur-ws.org/Vol-2696/paper_173.pdf)

We are heavily working on better models for historic texts, so please star or watch this repository!

# Triple E - Effective Ensembling of Embeddings and Language Models for NER of Historical German

In this section we give a brief overview of how to reproduce the results from our paper.

As we heavily use Flair and Transformers for our experiments, you should find the relevant scripts in the
`experiments/clef-hipe-2020` folder:

* `word-embeddings`: includes scripts for the experiments with different word embeddings
* `flair-embeddings`: includes scripts for the experiments with different Flair embeddings
* `stacked`: combines word, Flair and Transformer-based embeddings

# Changelog

* 30.11.2020: Initial version of this repository

# Citation

You can use the following BibTeX entry for citation:

```bibtex
@inproceedings{DBLP:conf/clef/SchweterM20,
  author    = {Stefan Schweter and
               Luisa M{\"{a}}rz},
  editor    = {Linda Cappellato and
               Carsten Eickhoff and
               Nicola Ferro and
               Aur{\'{e}}lie N{\'{e}}v{\'{e}}ol},
  title     = {Triple {E} - Effective Ensembling of Embeddings and Language Models
               for {NER} of Historical German},
  booktitle = {Working Notes of {CLEF} 2020 - Conference and Labs of the Evaluation
               Forum, Thessaloniki, Greece, September 22-25, 2020},
  series    = {{CEUR} Workshop Proceedings},
  volume    = {2696},
  publisher = {CEUR-WS.org},
  year      = {2020},
  url       = {http://ceur-ws.org/Vol-2696/paper\_173.pdf},
  timestamp = {Tue, 27 Oct 2020 17:12:48 +0100},
  biburl    = {https://dblp.org/rec/conf/clef/SchweterM20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```