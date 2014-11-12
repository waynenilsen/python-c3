__author__ = 'wnilsen'

import pyc3
import unittest
import pandas
import numpy

class C3Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_chart(self):
        configurations = [
            {
                "data": {
                    "x": 'x',
                    "columns": [
                        ['x', '2013-10-31', '2013-12-31', '2014-01-31', '2014-02-28'],
                        ['sample', 30, 100, 400, 150],
                    ]
                },
                "axis": {
                    "x": {
                        "type": 'timeseries',
                        "tick": {
                            "fit": False,
                            "format": "%e %b %y",
                            "count": 7
                        }
                    }
                }
            },
            {
                "data": {
                    "columns": pandas.DataFrame(numpy.random.randn(300, 4), columns=list('ABCD')),
                    "xs": {
                        'A': 'B',
                        'C': 'D'
                    },
                    'type': 'scatter'
                },
                'axis': {
                    'x': {
                        'tick': {
                            'fit': False
                        }
                    }
                }
            },
            {
            "data": {
                "columns": [
                    ['data1', 100, 200, 1000, 900, 500]
                ]
            },
            "grid": {
                    "x": {
                        "lines": [{"value": 2}, {"value": 4, "class": 'grid4', "text": 'LABEL 4'}]
                    },
                    "y": {
                        "lines": [{"value": 500}, {"value": 800, "class": 'grid800', "text": 'LABEL 800'}]
                    }
                }
            },
            {
                "data": {
                    "columns": [
                        ['data1', 30, 200, 100, 400, 150, 250],
                        ['data2', 50, 20, 10, 40, 15, 25]
                    ]
                }
            },
            {
                "data": {
                    "columns": [
                        ['data1', -30, 200, 200, 400, -150, 250],
                        ['data2', 130, 100, -100, 200, -150, 50],
                        ['data3', -230, 200, 200, -300, 250, 250]
                    ],
                    "type": 'bar',
                    "groups": [
                        ['data1', 'data2']
                    ]
                },
                "grid": {
                    "y": {
                        "lines": [{"value":0}]
                    }
                }
            }
        ]

        for c in configurations:
            pyc3.generate(config=c)
            # pyc3.generate(config=configurations[1])