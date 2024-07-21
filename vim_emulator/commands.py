"""
Author: <Chuanyu> (skewcy@gmail.com)
operators.py (c) 2024
Desc: description
Created:  2024-07-21T17:28:49.755Z
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vim_emulator import VimEmulator

match_table = {}


def motion_l(vim: VimEmulator) -> bool:
    vim.cursor.x = min(vim.cursor.x + 1, vim.buffer.width - 1)
    return True


match_table["l"] = motion_l


def motion_k(vim: VimEmulator) -> bool:
    vim.cursor.y = max(0, vim.cursor.y - 1)
    return True


match_table["k"] = motion_k


def motion_j(vim: VimEmulator) -> bool:
    vim.cursor.y = min(vim.cursor.y + 1, vim.buffer.length - 1)
    return True


match_table["j"] = motion_j


def motion_h(vim: VimEmulator) -> bool:
    vim.cursor.x = max(0, vim.cursor.x - 1)
    return True


match_table["h"] = motion_h
