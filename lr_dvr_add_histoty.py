#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will force DVR 'History' to be populated by a flat file."
replace = [{
    'file_path' : 'dest/configs/api_endpoints.js',
    'search_line' : """    getRecordingHistory:""",
    'new_line' : """    getRecordingHistory: "../data/dvr/recording_history.json",//GET""",
    'revert_line' : """    getRecordingHistory: "%server%/pub/dvredge/devices/%deviceid%/recordings?statusfilter=1|2|4|5|6|7|8|10|11|12|13|14&token=%token%",//GET"""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})