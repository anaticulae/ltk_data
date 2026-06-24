# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import pickle  # nosec

import utilo


def pickler(source: str):
    utilo.log(f'load: {source}')
    loaded = load_dict(source, lower=True)
    dumped = pickle.dumps(loaded, protocol=4)
    outpath = picklepath(source)
    utilo.log(f'dump: {outpath}')
    utilo.file_replace_binary(outpath, dumped)


def load_pickle(path: str):
    path = picklepath(path)
    loaded = utilo.file_read_binary(path)
    loaded = pickle.loads(loaded)  # nosec
    return loaded


def picklepath(path: str):
    directory, name = os.path.split(path)
    if not name.endswith('pickle'):
        name = f'{name}.pickle'
        path = utilo.join(directory, name)
    return path


def load_dict(path, lower: bool = False) -> set:
    assert utilo.exists(path), str(path)
    loaded = utilo.file_read(path).splitlines()
    result = set(item.lower() if lower else item for item in loaded)
    return result
