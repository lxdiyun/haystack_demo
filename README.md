haystack_demo
=============

Requirements
------------
* [mmseg](https://pypi.python.org/pypi/mmseg/1.3.0)

```shell
./manage.py syndb
```

```python
from myapp import generate
generate.gen_en(2000)
generate.gen_zh(2000)
```

```shell
./manage.py rebuild_index
```
