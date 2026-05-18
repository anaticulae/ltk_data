# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila


def add_nltk_path(path: str):
    utila.exists_assert(path)
    seperator = os.pathsep
    before = os.environ.get('ltk_data', '')
    if before:
        before += seperator
    current = f'{before}{path}'
    os.environ['ltk_data'] = current
