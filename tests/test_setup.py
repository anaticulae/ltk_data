# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import nltk_data
import nltk_data.lookup


def test_nltk_config():
    assert os.path.exists(os.environ['NLTK_DATA'])
    assert os.path.exists(nltk_data.STOPWORDS)


def test_ntlk_import():
    """Ensure that first source of nltk_data lookup is set by nltk_data."""
    import nltk
    firstpath = nltk.data.path[0]
    assert firstpath.endswith('nltk_data')


def test_ntlk_lookup():
    assert len(nltk_data.lookup.NAME_FAMILY) >= 18
