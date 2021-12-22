#!/usr/bin/bash
def remove_char_at(str, n):
    if 0 <= n and len(str) > n:
        str = str[:n] + str[n + 1:]
    return str
