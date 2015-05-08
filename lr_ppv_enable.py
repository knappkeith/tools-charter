#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will tell the APP that Pay Per View is enabled."
replace = [{
    'file_path' : 'dest/configs/avconfig.js',
    'search_line' : """        disablePPV:""",
    'new_line' : """        disablePPV: false,""",
    'revert_line' : """        disablePPV: true,"""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})