import json
import os

class Personal_Info(object):
	def __init__(self, my_json='~/dev/charter/tools/data/private_info.json'):
		self.pi_path = os.path.abspath(os.path.expanduser(my_json))
		if not os.path.isfile(self.pi_path):
			raise NameError("settings not found " + os.path.abspath(my_json))
		else:
			self._open_json()
			self._read_json()
			self._close_json()

	def _open_json(self):
		self.pi_file = open(self.pi_path)

	def _read_json(self):
		self.pi_str = self.pi_file.read()
		self.pi_data = json.loads(self.pi_str)

	def _close_json(self):
		self.pi_file.close()

	def get_user_name(self, site_name):
		for creds in self.pi_data['credentials']:
			if creds['site'] == site_name:
				return creds['user_name']
		return None

	def get_password(self, site_name):
		for creds in self.pi_data['credentials']:
			if creds['site'] == site_name:
				return creds['password']
		return None

	def return_category(self, category):
		try:
			return self.pi_data[category]
		except KeyError:
			return None

	def add_password(self):
		pass

	def save(self):
		pass
