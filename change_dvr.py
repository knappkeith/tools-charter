import os
from sys import argv, exit

ui_dir = 'skyuisp'
set_path = 'skyuisp/dest/configs/'
set_name = 'api_endpoints%s.js'
search_line = """    getRecordings:"""
local_line = """    getRecordings: "../data/dvr/recordings_api.json",//GET"""
server_line = """    getRecordings: "%server%/pub/dvredge/devices/%deviceid%/recordings?statusfilter=1|2&token=%token%",//GET"""

# Find Path for /skyuisp/dest/config/api_endpoints.js
# First look in current directory
if ui_dir in os.listdir('./'):
	set_path = os.path.join(os.path.abspath('./'),set_path)
elif ui_dir in os.listdir('../'):
	set_path = os.path.join(os.path.abspath('../'),set_path)
else:
	print 'Unable to find %s directory in current or parent directory!' % ui_dir
	exit(0)


read_path = os.path.join(set_path, set_name % '')
write_path = os.path.join(set_path, set_name % '-1')

org_line = """    getRecordings:"""
new_line = """    getRecordings: "../data/dvr/recordings_api.json",//GET"""

# Check to see if arguements were passed and reset 
if len(argv) > 1:
	if argv[1] == 'revert':
		new_line = """    getRecordings: "%server%/pub/dvredge/devices/%deviceid%/recordings?statusfilter=1|2&token=%token%",//GET"""
	else:
		new_line = """    getRecordings: "../data/dvr/recordings_api.json",//GET"""

read_file = open(read_path)
write_file = open(write_path, 'w')

for line in read_file:
	if org_line in line:
		print 'Found it, REPLACING!!!!'
		write_file.write(new_line + '\n')
	else:
		write_file.write(line)

read_file.close()
write_file.close()
os.remove(read_path)
os.rename(write_path, read_path)