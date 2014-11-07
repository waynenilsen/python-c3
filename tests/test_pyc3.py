__author__ = 'wnilsen'

import pyc3
import unittest

class C3Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_chart(self):
        configurations = [
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