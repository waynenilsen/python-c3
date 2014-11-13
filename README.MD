python-[c3](c3js.org)
==
python-c3 is a file based python wrapper for the [c3](https://github.com/masayuki0812/c3) javascript plotting library.

usage:
```python
import pyc3
pyc3.generate({
    "data": {
        "columns": [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 50, 20, 10, 40, 15, 25]
        ]
    }
})
```

Lots of examples of appropriate dictionaries to provide are found [on the c3 examples page](http://c3js.org/examples.html)

Future improvements include

* explicit custom css
* [dynamic api](http://c3js.org/examples.html#api) support ... somehow, would likely require ajax
* possible flask-based server version
* possible image output via [spynner](https://github.com/makinacorpus/spynner) as in [this](http://stackoverflow.com/a/3370724/2075745)

Completed improvements

* pandas support
* custom full template