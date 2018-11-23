#!/usr/bin/env python
import runcmd

r = runcmd.run(["echo", "hello world"])
print(r)
print("code = %s" % r.code)
print("out = %s" % r.out)
print("err = %s" % r.err)

out = runcmd.run(["echo", "hello world"]).exc().out
