#!/usr/bin/env python
import runcmd

runcmd.run(["ls"]).exc()  # ok

try:
    runcmd.run(["mkdir", "/"]).exc()
except OSError:  # mkdir: /: Is a directory
    pass
