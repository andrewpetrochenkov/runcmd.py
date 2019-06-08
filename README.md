<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/runcmd.svg?longCache=True)](https://pypi.org/project/runcmd/)
[![](https://img.shields.io/pypi/v/runcmd.svg?maxAge=3600)](https://pypi.org/project/runcmd/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/runcmd.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/runcmd.py/)

#### Installation
```bash
$ [sudo] pip install runcmd
```

#### Classes
class|`__doc__`
-|-
`runcmd.Process` |Process class

#### Functions
function|`__doc__`
-|-
`runcmd.run(args, cwd=None, background=False)` |run command and return Process object

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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>