# django-mypy

A simple django project to show use of mypy

* Create virtualenv with python 3

* Install latest version of [mypy](https://github.com/python/mypy)
from github

```
$ pip install Django==1.9.5

$ MYPYPATH=`pwd`/stubs mypy polls/views.py
polls/views.py: note: In function "detail":
polls/views.py:23: error: Incompatible return value type: expected django.http.response.HttpResponse, got builtins.str
```

#### Disclaimer

WIP - use with care
