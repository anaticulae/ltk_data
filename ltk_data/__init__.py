# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
from importlib.metadata import version as metaversion

__version__ = metaversion('ltk_data')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# pylint:disable=wrong-import-position
from ltk_data.corpora import *  # isort:skip
from ltk_data.utils import pickler  # isort:skip
from ltk_data.utils import load_pickle  # isort:skip
from ltk_data.utils import picklepath  # isort:skip
from ltk_data.path import add_nltk_path  # isort:skip
from ltk_data.compile import compile_names

# nltk requires env setup before first import
ltk_data = os.path.join(ROOT, 'ltk_data')

add_nltk_path(ltk_data)
compile_names(update=False)
