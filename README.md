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
buid database
```shell
./manage.py syncdb
```

generate random data
```python
from myapp import generate
generate.gen_en(2000)
generate.gen_zh(2000)
```

build index manually
```shell
./manage.py rebuild_index
```
