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


def compile_names(update: bool = False):
    if todo(update=update):
        utilo.log('compile names')
    else:
        utilo.debug('nothing to compile')
    for path in todo(update=update):
        ltk_data.pickler(path)


def todo(update: bool = False):
    """\
    >>> next(todo(update=True))
    '.../ltk_data/corpora/names/family'
    """
    for item in (
            ltk_data.NAMES_FAMILY,
            ltk_data.NAMES_FEMALE,
            ltk_data.NAMES_MALE,
    ):
        if not update and utilo.exists(ltk_data.picklepath(item)):
            continue
        yield item
