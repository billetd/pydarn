"""
    Author:
        Keith Kotyk
        Marina Schmidt
"""
import logging
pydarn_logger = logging.getLogger('pydarn')


class CursorError(Exception):
    """
    Raise if the cursor is not correctly set

    Parameter
    ---------
    cursor : int
        Current position in the data buffer
    expected_value : int
        What you expected the value of the cursor to be.
        Default 0.
    message : str
        Another type of message that might give more information
        on the cursor error.
        Default empty.
    """
    def __init__(self, cursor: int, expected_value=0, message=''):
        self.cursor
        if message == '':
            self.message = "Error: Cursor is at {cursor} and"\
                    "it needs to be {expected}".format(cursor=cursor,
                                                       expected=expected_value)
        else:
            self.message = message
        super().__init__(self.message)
        pydarn_logger.error(self.message)


class EmptyFileError(Exception):
    """
    Raised if a file is empty.

    Parameter
    --------
    filename : str
        The name of the file that is empty.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.message = "Error: {} is empty or"\
            " please check this is the correct file".format(filename)
        super().__init__(self.message)
        pydarn_logger.error(self.message)


class DmapDataTypeError(Exception):
    """
    Raised if the data type is not correct.

    Parameter
    ---------
    filename : str
        name of the file that the DMAP data is coming from.
    data_name : str
        parameter field name in the DMAP record
    data_type : str
        data type of the field name.
    cursor : int
        current position in the data buffer
    """
    def __init__(self, filename: str, data_name: str,
                 data_type: str, cursor: int):
        self.filename = filename
        self.message = "Error: Dmap data type {data_type} for {name}"\
            " at cursor = {cursor} does not exist in dmap data types."\
            "filename: {filename}".format(name=data_name,
                                          data_type=data_type,
                                          filename=filename,
                                          cursor=cursor)
        super().__init__(self.message)
        pydarn_logger.error(self.message)


class NegativeByteError(Exception):
    """
    Raised if an element has < 0 bytes.

    Parameter
    ---------
    filename : str
        The file name of the DMAP data
    element_info : str
        String containing element name.
    """
    def __init__(self, filename: str, element_info: str, cursor: int):
        self.filename = filename
        self.message = "Error: {filename} contains an {element} < 0"\
            " at cursor = {cursor}.".format(filename=filename,
                                            element=element_info,
                                            cursor=cursor)
        super().__init__(self.message)
        pydarn_logger.error(self.message)


class ZeroByteError(Exception):
    """
    Raised if an element has == 0 bytes.

    Parameter
    ---------
    filename : str
        Name of the file that contains the DMAP data
    element_info : str
        String containing element name.
    cursor : int
        Current position in the dmap buffer
    """
    def __init__(self, filename: str, element_info: str, cursor: int):
        self.filename = filename
        self.message = "Error: {filename} contains an {element} == 0"\
            " at cursor = {cursor}.".format(filename=filename,
                                            element=element_info,
                                            cursor=cursor)
        super().__init__(self.message)
        pydarn_logger.error(self.message)


class MismatchByteError(Exception):
    """
    Raised if an element is > another element.

    Parameter
    ---------
    filename : str
        Name of the file that contains the DMAP data
    element_info : str
        String containing element info on the two elements being compared.
    cursor : int
        Current position in the dmap buffer.
    """
    def __init__(self, filename: str, element_info: str, cursor: int):
        self.filename = filename
        self.message = "Error: {filename} contains an {element}"\
            " at cursor = {cursor}.".format(filename=filename,
                                            element=element_info,
                                            cursor=cursor)
        super().__init__(self.message)
        pydarn_logger.error(self.message)


# TODO: may need to delete later if not used in DmapWrite?
class DmapDataError(Exception):
    """Raised if there is an error in parsing of data

    Parameter
    ---------
    filename : str
        Name of the file that contains the DMAP data
    message : str
        Message containing information on the Error
    """
    def __init__(self, filename: str, message: str):
        self.filename = filename
        self.message = "Error: {filename} is data,"\
            " is corrupt because: {msg}".format(filename=filename,
                                                msg=message)
        super().__init__(self.message)
        pydarn_logger.error("DmapDataError: {} is corrupt {}".format(filename,
                                                                     message))