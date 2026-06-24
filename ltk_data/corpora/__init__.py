# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import ltk_data

CORPORA = utilo.join(ltk_data.ROOT, 'ltk_data/corpora')

NAMES = utilo.join(CORPORA, 'names')
NAMES_MALE = utilo.join(NAMES, 'male')
NAMES_FEMALE = utilo.join(NAMES, 'female')
NAMES_FAMILY = utilo.join(NAMES, 'family')

STOPWORDS = utilo.join(CORPORA, 'stopwords')
