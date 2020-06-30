<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/runcmd.svg?maxAge=3600)](https://pypi.org/project/runcmd/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/runcmd.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/runcmd.py/actions)

### Installation
```bash
$ [sudo] pip install runcmd
```

#### Examples
```python
>>> import runcmd
>>> r = runcmd.run(["echo", "hello world"])
>>> r.code  # exit status code
0
>>> r.out  # stdout
'hello world'
>>> r.err  # stderr
''
>>> r.pid  # process pid
1234
```

`background=True`
```python
>>> r = runcmd.run(["sleep","5"],background=True)
>>> while r.running:  # True if process is running and not "zombie process"
>>>     print("running")
```
`kill(signal=None)` - kill process
```python
>>> r.kill(-9)
```

`exc()` - raise exception if code is not `0`
```python
>>> runcmd.run(["ls"]).exc()              # code 0, ok
>>> runcmd.run(["mkdir", "/"]).exc()      # code 1, raise OSError
...
OSError: exited with code 1
mkdir: /: Is a directory
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>