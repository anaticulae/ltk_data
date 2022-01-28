# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

__version__ = '0.2.3'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# pylint:disable=wrong-import-position
from nltk_data.corpora import *  # isort:skip
from nltk_data.utils import pickler  # isort:skip
from nltk_data.utils import load_pickle  # isort:skip
from nltk_data.path import add_nltk_path  # isort:skip

# nltk requires env setup before first import
NLTK_DATA = os.path.join(ROOT, 'nltk_data')

add_nltk_path(NLTK_DATA)
