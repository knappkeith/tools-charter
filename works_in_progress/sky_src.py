import os

class Sky_Source(object):
	def __init__(self):
		root_name = 'skyuisp'
		self._set_root_dir(root_name)
		if self.root_path is None:
			print 'Unable to find %s directory in current or parent or grandparent directory!' % root_name
		self._set_config_dir()


	def _set_root_dir(self, search_dir, root_base='./'):
		if search_dir in os.listdir(root_base):
			self.root_path = os.path.join(os.path.abspath('./'), search_dir)
		elif search_dir in os.listdir(os.path.join(root_base,'../')):
			self.root_path = os.path.join(os.path.abspath(os.path.join(root_base,'../')), search_dir)
		elif search_dir in os.listdir(os.path.join(root_base,'../../')):
			self.root_path = os.path.join(os.path.abspath(os.path.join(root_base,'../../')), search_dir)
		else:
			self.root_path = None


	def _set_config_dir(self):
		if self.dir_exists('dest/configs/'):
			self.config = os.path.join(self.root_path, 'dest/configs/')
		else:
			self.config = None
			print 'Unable to set Config Directory'


	def dir_exists(self, directory):
		directory = os.path.expanduser(directory)
		if os.path.exists(directory):
			return True
		else:
			return os.path.exists(os.path.join(self.root_path, directory))


	def file_exists(self, file):
		file = os.path.expanduser(file)
		if os.path.exists(file):
			return True
		else:
			return os.path.exists(os.path.join(self.root_path, file))


	def get_full_path(self, file):
		file = os.path.expanduser(file)
		if os.path.exists(file):
			return os.path.abspath(file)
		elif os.path.exists(os.path.join(self.root_path, file)):
			return os.path.abspath(os.path.join(self.root_path, file))
		else:
			return None


	def create_copy_name(self, og_path):
		og_path = self.get_full_path(og_path)
		if not self.file_exists(og_path):
			print 'Unable to find original file %s!' % og_path
			return None
		og_dir, og_file = os.path.split(og_path)
		og_name, og_ext = os.path.splitext(og_file)
		count = 1
		while os.path.exists(os.path.join(og_dir, '%s-%s%s' % (og_name, count, og_ext))):
			count += 1
		return os.path.join(og_dir, '%s-%s%s' % (og_name, count, og_ext))


	def create_copy_names(self, og_array):
		if type(og_array) is not list:
			og_array = [og_array]
		copies = []
		for path in og_array:
			copy_path = self.create_copy_name(path)
			if copy_path is not None:
				copies.append(copy_path)
		return copies


	def _convert_to_array(self, string):
		if type(string) is not list:
			return [string]
		else:
			return string

	
	def open_copy_files(self, read_files):
		read_files = self._convert_to_array(read_files)
		write_files = self.create_copy_names(read_files)
		self.copy_files_dict = {}
		for file in read_files:
			self.copy_files_dict[file] = self.create_copy_name(file)
		self.open_all_files(read_files, write_files)
		

	def open_all_files(self, fread, fwrite):
		try:
			self.files_read
		except:
			self._create_files_dict(fread, fwrite)
		for file in self.files_read:
			self.files_read[file] = open(file)
		for file in self.files_write:
			self.files_write[file] = open(file, 'w')


	def _create_files_dict(self, read_files, write_files):
		read_files = self._convert_to_array(read_files)
		write_files = self._convert_to_array(write_files)
		self.files_read = {}
		self.files_write = {}
		for read_file in read_files:
			self.files_read[read_file] = None
		for write_file in write_files:
			self.files_write[write_file] = None
		



