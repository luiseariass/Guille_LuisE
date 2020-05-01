import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Autentificacion.
url = "https://api.pdffiller.com/v2/oauth/token"

payload = '{"grant_type":"password","client_id":"9fd0316acc5708bd","username":"11-11486@usb.ve","password":"SFLbssW@7DeL6fV","client_secret":"sQMVpPxsAI1atkrroEasVubEgXZ3eVYy"}'
headers = {
    'accept': "application/json; charset=UTF-8",
    'content-type': "application/json"
    }

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:

	access_token=response.json()['access_token']

	#Accediendo a la cantidad de archivos que tengo 
	url = "https://api.pdffiller.com/v2/templates"

	querystring = {"per_page":"15","page":"1","order":"desc","order_by":"id"}

	headers = {
	    'accept': "application/json; charset=UTF-8",
	    'authorization': "Bearer %s" %access_token
	    }

	response = requests.get(url, headers=headers, params=querystring)

	print("La cantidad de archivos en mis pdffiller es %s" %response.json()['total'])

	#Subiendo un archivo desde su path

	url = 'https://api.pdffiller.com/v2/templates'
	headers = {
    	'authorization': "Bearer %s" %access_token
	}

	path=os.path.join(BASE_DIR,'pueba.pdf')
	my_path=open(path,'rb')
	files = {
    	'file': (path, my_path),
	}
	name= "Prueba_Path_%s"%response.json()['total']
	data = {"name":name,"folder_id":0}
	response = requests.post(url, headers=headers, files=files,data=data)


	if response.status_code < 200:
		headers = {
    	'Authorization': "Bearer %s" %access_token,
    	'Content-Type': 'application/json',
		}

		data = '{"document_id":"%s","access":"full","status":"public","filled_forms_count":1}'%response.json()['id']
		response = requests.post('https://api.pdffiller.com/v2/fillable_forms', headers=headers, data=data)
		print(response.json())

		url = "https://api.pdffiller.com/v2/fillable_forms/%s"%response.json()['fillable_form_id']

		headers = {
    	'accept': "application/json",
    	'Authorization': "Bearer %s" %access_token
    	}

		response = requests.request("GET", url, headers=headers)

		print(response.text)


		if response.status_code < 200:
			headers = {
    		'Authorization': "Bearer %s" %access_token,
    		'Content-Type': 'application/json',
			}

			url = 'https://api.pdffiller.com/v2/fillable_forms/%s/filled_forms'%response.json()['fillable_form_id']

			response = requests.get(url, headers=headers)

			print(response)

	else:
		print('Error en el path')
else: 
	print('Error en la autentificacion')