import requests


class YADisk:
	URL = 'https://cloud-api.yandex.net'
	TOKEN = 'y0_AgAAAABHDBv9AADLWwAAAAD5jxNLAADuRn6RN1ZPUL1FLQjrbERL6rOj4w'
	headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Authorization': TOKEN
	}

	def create_folder(self, param, folder_name):
		url = f'{self.URL}/v1/disk/resources'
		params = {param: folder_name}
		response = requests.put(url, headers=self.headers, params=params)
		return response

	def delete_folder(self, param, folder_name):
		url = f'{self.URL}/v1/disk/resources'
		params = {param: folder_name}
		response = requests.delete(url, headers=self.headers, params=params)
		return response
