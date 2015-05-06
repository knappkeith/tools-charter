#! /usr/bin/env python
from libs.my_replacer import My_Replacer
import os
import shutil

script_desc = "This will force Entitlements to be populated by a flat file."
replace = [{
    'file_path' : 'dest/configs/api_endpoints.js',
    'search_line' : """    entitlements:""",
    'new_line' : """    entitlements: "../data/entitlements_fake_all.json?",""",
    'revert_line' : """    entitlements: "%server%/pub/lrmedge/v1/rights/entitlements","""
}]

# Copy Fake Entitlements file

my_replacer = My_Replacer(replace, {"description":script_desc, "file":__file__})

# Copy Fake Entitlements file to correct directory
entitle = os.path.abspath(os.path.join(os.path.dirname(__file__),"data/entitlements_fake_all.json"))
scr_root = my_replacer._get_root_dir()
new_entitle = os.path.join(scr_root,"dest/data/entitlements_fake_all.json")
shutil.copyfile(entitle, new_entitle)
print "Copied Entitlements File"