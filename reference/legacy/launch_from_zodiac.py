import os
from sys import argv, exit

ui_dir = 'skyuisp'

# Also add '&state=networkdetails' to the parameters of the URL

# THESE NEED TO BE UPDATED TO MAKE WORK
set_path = 'skyuisp/dest/configs/'
set_name = 'config-dev-stable%s.js'
search_line = """window.config.app.manualNetworkDetailsLaunch"""
new_line = """**/window.config.app.manualNetworkDetailsLaunch = '%s'; // e.g.: '030005', yielding launch type 3 / channel 13""" % raw_input('Enter HEX Value:')
server_line = """window.config.app.manualNetworkDetailsLaunch = '03000d'; // e.g.: '03000d', yielding launch type 3 / channel 13"""
# END OF SETTINGS

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

# Check to see if arguements were passed and reset 
if len(argv) > 1:
	if argv[1] == 'revert':
		new_line = server_line

read_file = open(read_path)
write_file = open(write_path, 'w')

for line in read_file:
	if search_line in line:
		print 'Found it, REPLACING!!!!'
		write_file.write(new_line + '\n')
	else:
		write_file.write(line)

read_file.close()
write_file.close()
os.remove(read_path)
os.rename(write_path, read_path)