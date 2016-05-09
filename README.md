# django-mypy

A simple django project to show use of mypy

* Create virtualenv with python 3

    ```
    $ virtualenv .env --python python3
    $ . ./.env/bin/activate
    ```

* Install latest version of [mypy](https://github.com/python/mypy)
from github

    ```
    $ git clone https://github.com/python/mypy
    $ git submodule update --init typeshed
    $ python setup.py install
    ```


* ```$ pip install Django==1.9.5```

* Run mypy on the example django project

    ```
    $ MYPYPATH=`pwd`/stubs mypy polls/views.py
    polls/views.py: note: In function "detail":
    polls/views.py:23: error: Incompatible return value type: expected django.http.response.HttpResponse, got builtins.str
    ```

#### Disclaimer

**WIP**
