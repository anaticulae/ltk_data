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
import ltk_data.lookup


def test_nltk_config():
    assert os.path.exists(os.environ['ltk_data'])
    assert os.path.exists(ltk_data.STOPWORDS)


def test_ntlk_import():
    """Ensure that first source of ltk_data lookup is set by ltk_data."""
    import nltk
    firstpath = nltk.data.path[0]
    assert firstpath.endswith('ltk_data')


def test_ntlk_lookup():
    assert len(ltk_data.lookup.NAME_FAMILY) >= 18
