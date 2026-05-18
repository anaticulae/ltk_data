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
    'ltk_data',
    'ltk_data.chunkers.maxent_ne_chunker',
    'ltk_data.chunkers.maxent_ne_chunker.PY3',
    'ltk_data.corpora',
    'ltk_data.corpora.crubadan',
    'ltk_data.corpora.names',
    'ltk_data.corpora.stopwords',
    'ltk_data.corpora.words',
    'ltk_data.misc.perluniprops',
    'ltk_data.taggers.averaged_perceptron_tagger',
    'ltk_data.taggers.maxent_treebank_pos_tagger',
    'ltk_data.taggers.maxent_treebank_pos_tagger.PY3',
    'ltk_data.tokenizers.punkt',
    'ltk_data.tokenizers.punkt.PY3',
]

if __name__ == "__main__":
    utila.install(
        __file__,
        include_package_data=True,
    )
    import ltk_data.compile
    ltk_data.compile.compile_names()
