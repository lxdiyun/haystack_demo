haystack_demo
=============

Requirements
------------
* [mmseg](https://pypi.python.org/pypi/mmseg/1.3.0)
* [jieba] (https://github.com/fxsjy/jieba)
* [xapian](http://xapian.org/)
* [django-haystack](http://haystacksearch.org/)
* [xapian_backend](https://github.com/notanumber/xapian-haystack)
* [whoosh](https://pypi.python.org/pypi/Whoosh/)
* [dajax](http://www.dajaxproject.com/)

Setup 
-----
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
