
#Retrieves a list of uploaded documents.
def retrieves_a_list_of_uploaded_templates(access_token,folder_id,date_to,date_from='01/01/2020'):
	import requests

	headers = {'accept': 'application/json','authorization': "Bearer %s" %access_token,}
	print('aghhhh')
	response=requests.get('https://api.pdffiller.com/v2/templates', headers=headers, params=params)
