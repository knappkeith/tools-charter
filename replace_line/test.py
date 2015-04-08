import os
import sys
import argparse
sys.path.append(os.path.abspath('../'))
from libs.sky_src import Sky_Source

def ask_for_value():
    return raw_input('enter')

def convert():
    pass

# Enter a Help Description here
help_description = '''This is a tool that will switch such and such feature on and off'''

# Arguement Parser
parser = argparse.ArgumentParser(description=help_description)
parser.add_argument('--revert', action='store_true', help='to revert the action')
parser.add_argument('-c', '--channel', type=int, default=ask_for_value, help='channel # to get details for')
my_args = parser.parse_args()

# Initialize Source
my_source = Sky_Source()



sys.exit(0)
# THESE NEED TO BE UPDATED TO MAKE WORK
file_name = my_source.get_full_path(os.path.join(my_source.config, 'config-dev-stable.js'))
search_line = """window.config.app.manualNetworkDetailsLaunch"""
new_line = """**/window.config.app.manualNetworkDetailsLaunch = '%s'; // e.g.: '030005', yielding launch type 3 / channel 13""" % my_args.channel
server_line = """window.config.app.manualNetworkDetailsLaunch = '03000d'; // e.g.: '03000d', yielding launch type 3 / channel 13"""
# END OF SETTINGS

write_path = my_source.create_copy_name(file_name)

print file_name
print write_path

# Check to see if arguements were passed and reset 
if len(sys.argv) > 1:
	if sys.argv[1] == 'revert':
		new_line = server_line

read_file = open(file_name)
write_file = open(write_path, 'w')

for line in read_file:
	if search_line in line:
		print 'Found it, REPLACING!!!!'
		write_file.write(new_line + '\n')
	else:
		write_file.write(line)

read_file.close()
write_file.close()
os.remove(file_name)
os.rename(write_path, file_name)


# NEEDS
# 
# 1. Function to comment and uncomment
# 2. Add/Remove a line
# 3. Find a file(s) in the source
# 4. Function to comment uncomment statements