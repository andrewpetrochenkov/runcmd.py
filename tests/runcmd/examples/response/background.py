#!/usr/bin/env python
import time
import runcmd

r = runcmd.run(["sleep", "5"], background=True)
print("pid: %s" % r.pid)
counter = 0
while r.running:
    print("running %s" % counter)
    counter += 1
    time.sleep(1)
    if counter > 2:
        r.kill()
