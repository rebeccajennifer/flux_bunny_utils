#______________________________________________________________________
#______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#______________________________________________________________________
#______________________________________________________________________
#
#----------------------------------------------------------------------
#   Copyright 2025, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#----------------------------------------------------------------------
#
#______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#______________________________________________________________________
#   DESCRIPTION
#   Tests for dictionary utility functions.
#______________________________________________________________________

import pytest

from flux_bunny_utils.dict_utils import DictUtils


#_______________________________________________________________________
class TestConst:
  """
  Contains constants used in tests.
  """

#_______________________________________________________________________
def test_rm_key_wrong_type():

  with pytest.raises(Exception):
    DictUtils.rm_key(1, 4)

#_______________________________________________________________________
def test_rm_key():

  d_in : dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
  d_out: dict = {'a': [1, 2, 3], 'c': [7, 8, 9]}

  d_test: dict = DictUtils.rm_key(d_in, 'b')

  assert d_out == d_test

#_______________________________________________________________________
def test_get_key_of_max():

  pair_a  : tuple = ('a', [1, 2, 3])
  pair_b  : tuple = ('b', [4, 5, 6])
  pair_c  : tuple = ('c', [7, 8, 9])
  d_in    : dict  = dict([pair_a, pair_b, pair_c])

  pair_max  : tuple = pair_c
  pair_test : tuple = DictUtils.get_key_of_max(d_in)

  assert pair_test == pair_max

#_______________________________________________________________________
def test_get_key_of_min():

  pair_a  : tuple = ('a', [1, 2, 3])
  pair_b  : tuple = ('b', [4, 5, 6])
  pair_c  : tuple = ('c', [7, 8, 9])
  d_in    : dict  = dict([pair_a, pair_b, pair_c])

  pair_max  : tuple = pair_a
  pair_test : tuple = DictUtils.get_key_of_min(d_in)

  assert pair_test == pair_max

#_______________________________________________________________________
def test_get_key_of_max_min_err():
  with pytest.raises(Exception):
    DictUtils.get_key_of_max(1)

  with pytest.raises(Exception):
    DictUtils.get_key_of_min(1)