#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will force DVR 'Reccordings' to be populated by a flat file."
replace = [{
    'file_path' : 'dest/configs/api_endpoints.js',
    'search_line' : """    getRecordings:""",
    'new_line' : """    getRecordings: "../data/dvr/recordings_api.json",//GET""",
    'revert_line' : """    getRecordings: "%server%/pub/dvredge/devices/%deviceid%/recordings?statusfilter=1|2&token=%token%",//GET"""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})