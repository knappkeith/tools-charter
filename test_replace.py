from replace_line.line_replacer import My_Replacer

replace = [{
    'file_path' : '/dest/config/api_endpoints.js',
    'search_line' : """    getRecordings:""",
    'new_line' : """    getRecordings: "../data/dvr/recordings_api.json",//GET""",
    'revertline' : """    getRecordings: "%server%/pub/dvredge/devices/%deviceid%/recordings?statusfilter=1|2&token=%token%",//GET"""
}, {
    'file_path' : '/dest/config/avconfig.js',
    'search_line' : """            useCannedVideo:""",
    'new_line' : """            useCannedVideo: true, //this will override all other trailer settings and use the local canned video specified in the cannedVideoUrl below""",
    'revertline' : """            useCannedVideo: false, //this will override all other trailer settings and use the local canned video specified in the cannedVideoUrl below"""
}]

My_Replacer(replace)
