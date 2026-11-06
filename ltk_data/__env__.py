import os
import pathlib

import utilo

import ltk_data

ROOT = pathlib.Path(ltk_data.__file__).parent
DATA = utilo.join(ROOT, 'data')


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
        utilo.debug(item)
        os.chmod(item, os.stat(item).st_mode & ~0o022)


def update_env(path):
    utilo.exists_assert(path)
    seperator = os.pathsep
    before = os.environ.get('NLTK_DATA', '')
    if path in before:
        utilo.error(f'path {path} already in os.env[NLTK_DATA]')
        return
    if before:
        before += seperator
    current = f'{before}{path}'
    os.environ['NLTK_DATA'] = current


make_private(ROOT)
update_env(DATA)
