import os
from sys import argv, exit

ui_dir = 'skyuisp'

# THESE NEED TO BE UPDATED TO MAKE WORK
set_path = 'skyuisp/dest/configs/'
set_name = 'avconfig%s.js'
search_line = """            useCannedVideo:"""
new_line = """            useCannedVideo: true, //this will override all other trailer settings and use the local canned video specified in the cannedVideoUrl below"""
server_line = """            useCannedVideo: false, //this will override all other trailer settings and use the local canned video specified in the cannedVideoUrl below"""
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