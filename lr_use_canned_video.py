#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will use the canned video for all video streams."
replace = [{
    'file_path' : 'dest/configs/avconfig.js',
    'search_line' : """            useCannedVideo:""",
    'new_line' : """            useCannedVideo: true,""",
    'revert_line' : """            useCannedVideo: false,"""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})
