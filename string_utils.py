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
#   String utility functions.
#_______________________________________________________________________


from .error_utils import ErrorUtils
#_______________________________________________________________________
class StringUtils:


  #_____________________________________________________________________
  def int_to_hex6(n: int) -> str:
    """
    Converts an integer to a 6-digit hex string.

    Parameters
    n - integer to convert

    Returns
    6-digit hex string representation of the input integer.
    E.g. 255 -> '0000ff'
    16777215 -> 'ffffff'
    0 -> '000000'
    16777216 -> '01000000' (not 6 digits, but 8)
    """
    return f'{n:06x}'

  #_____________________________________________________________________
  def str_hex_to_int(s: str) -> int:
    """
    Parameter
    s - hex integer represented as a string

    Returns
    The int represented by the input string as hex.
    """

    try:
      if (isinstance(s, str)):
        return int(s, base=16)

    except Exception as error:
      err_msg: str =\
        f'{ErrorUtils.ERROR_TYPE}'\
        f'{type(error).__name__}'\
        f'{ErrorUtils.DESC}'\
        f'{ErrorUtils.CONVERSION_ERROR}'\
        f'{ErrorUtils.LINE}'\

      raise ValueError(err_msg)

