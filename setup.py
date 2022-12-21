#!/usr/bin/env python
# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

PACKAGES = [
    'nltk_data',
    'nltk_data.chunkers.maxent_ne_chunker',
    'nltk_data.chunkers.maxent_ne_chunker.PY3',
    'nltk_data.corpora',
    'nltk_data.corpora.crubadan',
    'nltk_data.corpora.names',
    'nltk_data.corpora.stopwords',
    'nltk_data.corpora.words',
    'nltk_data.misc.perluniprops',
    'nltk_data.taggers.averaged_perceptron_tagger',
    'nltk_data.taggers.maxent_treebank_pos_tagger',
    'nltk_data.taggers.maxent_treebank_pos_tagger.PY3',
    'nltk_data.tokenizers.punkt',
    'nltk_data.tokenizers.punkt.PY3',
]

if __name__ == "__main__":
    utila.install(
        __file__,
        include_package_data=True,
    )
    import nltk_data.compile
    nltk_data.compile.compile_names()
