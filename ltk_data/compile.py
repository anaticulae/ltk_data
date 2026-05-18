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


def compile_names():
    utilo.log('compile names')
    ltk_data.pickler(ltk_data.NAMES_FAMILY)
    ltk_data.pickler(ltk_data.NAMES_FEMALE)
    ltk_data.pickler(ltk_data.NAMES_MALE)


if __name__ == "__main__":
    compile_names()
