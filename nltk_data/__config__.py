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
# nltk requires env setup before first import
NLTK_DATA = os.path.join(nltk_data.ROOT, 'nltk_data')
assert os.path.exists(NLTK_DATA)
os.environ['NLTK_DATA'] = NLTK_DATA
