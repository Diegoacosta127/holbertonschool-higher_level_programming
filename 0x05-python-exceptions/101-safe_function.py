#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as ex:
        stderr.write("Exception: {}\n".format(ex))
        return None
