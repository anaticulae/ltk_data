# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import importlib.metadata
import os

import utilo

__version__ = importlib.metadata.version('ltk_data')

ROOT = os.path.abspath(utilo.join(os.path.dirname(__file__), '..'))

# pylint:disable=wrong-import-position
from ltk_data.data.corpora import *  # isort:skip
from ltk_data.utils import pickler  # isort:skip
from ltk_data.utils import load_pickle  # isort:skip
from ltk_data.utils import picklepath  # isort:skip
from ltk_data.path import add_nltk_path  # isort:skip
from ltk_data.compile import compile_names

# nltk requires env setup before first import
LTK_DATA = utilo.join(ROOT, 'ltk_data/data')

add_nltk_path(LTK_DATA)

CORPORA = utilo.join(LTK_DATA, 'corpora')

STOPWORDS = utilo.join(CORPORA, 'stopwords')

NAMES = utilo.join(CORPORA, 'names')
NAMES_FAMILY = utilo.join(NAMES, 'family')
NAMES_FEMALE = utilo.join(NAMES, 'female')
NAMES_MALE = utilo.join(NAMES, 'male')

compile_names(update=False)

NAME_FAMILY = load_pickle(NAMES_FAMILY)
NAME_FEMALE = load_pickle(NAMES_FEMALE)
NAME_MALE = load_pickle(NAMES_MALE)
