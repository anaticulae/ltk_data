# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import ltk_data

CORPORA = os.path.join(ltk_data.ROOT, 'ltk_data/corpora')

NAMES = os.path.join(CORPORA, 'names')
NAMES_MALE = os.path.join(NAMES, 'male')
NAMES_FEMALE = os.path.join(NAMES, 'female')
NAMES_FAMILY = os.path.join(NAMES, 'family')

STOPWORDS = os.path.join(CORPORA, 'stopwords')
