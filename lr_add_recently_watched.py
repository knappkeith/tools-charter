#! /usr/bin/env python
from libs.my_replacer import My_Replacer

script_desc = "This will force 'Recently Watched' to be populated by a flat file."
replace = [{
    'file_path' : 'dest/configs/api_endpoints.js',
    'search_line' : """    getRecentlyWatched :""",
    'new_line' : """    getRecentlyWatched : "../data/sampledata/canned_recentlyWatched.json",""",
    'revert_line' : """    getRecentlyWatched : "%server%/pub/viewinghistoryedge/v1/viewinghistory","""
}]

My_Replacer(replace, {"description":script_desc, "file":__file__})
