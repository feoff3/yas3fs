#!/usr/bin/env python

"""
Some win-related helper functions
"""

import os
import win32file
import msvcrt

def win_open(filename):
    """win analogue for open(filename, 'rb+') compatible with share delete behavor"""
    # get an handle using win32 API, specifyng the SHARED access!
    handle = win32file.CreateFile(filename,
                                win32file.GENERIC_READ|win32file.GENERIC_WRITE,
                                win32file.FILE_SHARE_DELETE |
                                win32file.FILE_SHARE_READ |
                                win32file.FILE_SHARE_WRITE,
                                None,
                                win32file.OPEN_ALWAYS,
                                0,
                                None)
    # detach the handle
    detached_handle = handle.Detach()
    # get a file descriptor associated to the handle\
    file_descriptor = msvcrt.open_osfhandle(
        detached_handle, os.O_RDWR)
    # open the file descriptor
    return os.fdopen(file_descriptor , "rb+")
