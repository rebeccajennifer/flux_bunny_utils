#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2025, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#   DESCRIPTION
#   Dictionary utility functions.
#_______________________________________________________________________

from .error_utils import ErrorUtils

class DictUtils:

  #_____________________________________________________________________
  def rm_key(d: dict, key):
    """
    Returns a dictionary containing all items except the one with the
    given key.

    Parameters
      d   : Dictionary to filter.
      key : Key to remove from the returned dictionary.

    Returns
      dict : A dictionary with all key-value pairs from `d` except the
      one matching `key`.
    """

    try:
      return {k: v for k, v in d.items() if k != key}

    except Exception as err:

      desc: str       = ErrorUtils.WRONG_TYPE + str(type(d))
      ErrorUtils.raise_exception_with_desc(err, desc)

  #_____________________________________________________________________
  def get_key_of_max(d: dict) -> tuple:
    """
    Returns the key-value pair associated with the largest value in the
    dictionary.

    Parameters
      d : Dictionary
    """

    try:
      return max(d.items(), key=lambda x: x[1])

    except Exception as err:
      desc: str       = ErrorUtils.WRONG_TYPE + str(type(d))
      ErrorUtils.raise_exception_with_desc(err, desc)

  #_____________________________________________________________________
  def get_key_of_min(d: dict) -> tuple:
    """
    Returns the key-value pair associated with the smallest value in the
    dictionary.

    Parameters
      d : Dictionary
    """

    try:
      return min(d.items(), key=lambda x: x[1])

    except Exception as err:
      desc: str       = ErrorUtils.WRONG_TYPE + str(type(d))
      ErrorUtils.raise_exception_with_desc(err, desc)




