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
#   Error utility functions.
#_______________________________________________________________________

#_____________________________________________________________________
class ErrorUtils:
  """
  Utilities for error messages
  """

  LINE: str =\
    '\n________________________________________________________________'

  ERROR: str =\
    f'{LINE}'\
    '\n UH OH! The program has encountered an error!'\
    f'{LINE}'

  ERROR_TYPE: str =\
    f'{ERROR}'\
    '\n ERROR TYPE   : '

  DESC_LABEL              : str = '\n DESCRIPTION  : '
  PY_ERR_LABEL            : str = '\n PYTHON ERROR : '

  MK_DIR_NO_PARENT_ERR    : str = 'Parent directory not found: '
  FILE_WITH_DIR_NAME_ERR  : str = 'File exists with the same name: '
  WRONG_FILE_TYPE         : str = 'Wrong file type.'
  FILE_DNE                : str = 'File does not exist: '
  WRONG_TYPE              : str = 'Wrong input type: '
  INVALID_VALUE           : str = 'Invaid value: '


  #_____________________________________________________________________
  def raise_exception_with_desc\
    ( err: Exception = Exception()
    , desc: str = ERROR
    ) -> None:
    """
    Raise exception with descriptive message.

    Parameters
      err   : Exception type.
      desc  : Error message.

    Side Effects
      Raises exception

    Returns
      None
    """

    err_type = type(err)

    py_error: str = ''

    if (err.args):
      py_error = str(
        f'\n{ErrorUtils.PY_ERR_LABEL}'
        f'\n   {err.args[0]}'
      )

    err_msg: str = str(
      f'{ErrorUtils.ERROR_TYPE}{err_type.__name__}'
      f'{ErrorUtils.DESC_LABEL}{desc}'
      f'{py_error}'
      f'{ErrorUtils.LINE}'
    )

    raise err_type(err_msg)
