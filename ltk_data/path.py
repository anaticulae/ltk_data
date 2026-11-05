# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import pathlib

import utilo


def add_nltk_path(path: str):
    utilo.exists_assert(path)
    make_private(path)
    seperator = os.pathsep
    before = os.environ.get('NLTK_DATA', '')
    if before:
        before += seperator
    current = f'{before}{path}'
    os.environ['NLTK_DATA'] = current


READ_WRITE_EXECUTE = 0o700
READ_WRITE = 0o600


def make_private(path):
    """Do not allow other user to change content which is pickeld later.

    NLTK
        UserWarning: NLTK will not authorize the non-private download directory

    In short, ~0o022 means preserve all existing permissions except
    group-write and others-write.

    Original:  0o777
    Mask:     ~0o022
    Result:    0o755
    """
    root = pathlib.Path(path)
    for item in root.rglob("*"):
        if item.is_file():
            item.chmod(READ_WRITE)
            continue
        os.chmod(path, os.stat(path).st_mode & ~0o022)
    os.chmod(path, os.stat(path).st_mode & ~0o022)
