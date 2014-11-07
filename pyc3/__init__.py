'''
Python wrapper for the C3.js - D3 based reusable chart library. No dependencies other than standard python libraries.
Tested with Python 3.3
'''

__author__ = 'wnilsen'

import json
import tempfile
import webbrowser
import os

_defaultTemplate = '''
<html>
  <head>
    <link href="https://rawgit.com/masayuki0812/c3/master/c3.min.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <div id="chart"></div>

    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script src="https://rawgit.com/masayuki0812/c3/master/c3.min.js"></script>
    <script>
      var chart = c3.generate(
          {config}
      );
    </script>
  </body>
</html>
'''


def generate(config:dict, outputFile=None, show:bool=True, template:str=None):
    '''
    Similar to the c3.generate function of c3.js

    :param config: the dictionary supplied to the C3 generate function see http://c3js.org/examples.html for more
    :param outputFile: optional path to the output file, will use temporary file if not provided.
    :param show: opens the browser with the file:// syntax if true
    :param template: override the default template with this string, see _defaultTemplate in this file for an example

    :return: nothing.
    '''
    if outputFile is None:
        outputFile = tempfile.NamedTemporaryFile(mode='w',suffix='.html',prefix='c3chart',delete=False)
    elif isinstance(outputFile, str):
        outputFile = open(outputFile, 'w')
    if template is None:
        template = _defaultTemplate

    outputFile.write(_defaultTemplate.format(
        config=json.dumps(config)
    ))
    if show:
        webbrowser.open('file://{}'.format(os.path.abspath(outputFile.name)))

    outputFile.close()

