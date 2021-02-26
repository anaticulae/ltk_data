# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import nltk_data

CORPORA = os.path.join(nltk_data.ROOT, 'nltk_data/corpora')

NAMES = os.path.join(CORPORA, 'names')
NAMES_MALE = os.path.join(NAMES, 'male')
NAMES_FEMALE = os.path.join(NAMES, 'female')

STOPWORDS = os.path.join(CORPORA, 'stopwords')
