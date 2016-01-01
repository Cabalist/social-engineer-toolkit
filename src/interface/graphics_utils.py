# coding=utf-8
import random

from graphics import binary, cavs, fsociety, set1, set2, set3, set4, set5, set6, set7, skull, tardis, trusted_sec_badge


def random_graphic():
    return random.choice([binary, cavs, fsociety, set1, set2, set3, set4, set5, set6, set7, skull, tardis, trusted_sec_badge])()
