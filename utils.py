"""A few utilities that I have found the need for."""

import os 
import errno

def mkdir_p(path):
    """Same functionality as shell command mkdir -p."""
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

