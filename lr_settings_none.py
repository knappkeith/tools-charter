#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will force the setting to be read from a flat file that will make the Box appear to be in initial state."
replace = [{
    'file_path' : 'dest/configs/api_endpoints.js',
    'search_line' : """    networkSettings:""",
    'new_line' : """    networkSettings: "../data/api/settings/newSTBSettings.json",""",
    'revert_line' : """    networkSettings: "%server%/pub/networksettingsedge/v1/settings/deviceid/STB%deviceid%?","""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})