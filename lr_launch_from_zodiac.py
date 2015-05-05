#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will ask for a HEX code that will cause App to launch from that channel, make sure to add '&state=networkdetails' to your URL parameters."
replace = [{
    'file_path' : 'dest/configs/config-dev-stable.js',
    'search_line' : """window.config.app.manualNetworkDetailsLaunch""",
    'new_line' : """**/window.config.app.manualNetworkDetailsLaunch = '%s';,""" % raw_input('Enter HEX Value:'),
    'revert_line' : """window.config.app.manualNetworkDetailsLaunch = '03000d';"""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})