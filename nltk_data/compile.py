# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import nltk_data


def compile_names():
    nltk_data.pickler(nltk_data.NAMES_FAMILY)
    nltk_data.pickler(nltk_data.NAMES_FEMALE)
    nltk_data.pickler(nltk_data.NAMES_MALE)


if __name__ == "__main__":
    compile_names()
