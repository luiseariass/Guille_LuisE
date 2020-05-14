#Script para ir modulando los api que han ido funcionando 
import requests
import os
import math
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from datetime import date

#Funcion que de vuelve el token de autentificacion
def auth(client_id,username,password,client_secret):
	url = "https://api.pdffiller.com/v2/oauth/token"
	payload = '{"grant_type":"password","client_id":"%s","username":"%s","password":"%s","client_secret":"%s"}'%(str(client_id),str(username),str(password),str(client_secret))
	headers = {
    'accept': "application/json; charset=UTF-8",
    'content-type': "application/json"
    }

	response = requests.post(url, data=payload, headers=headers)
	print(' ------------------------------------')
	print('|                  auth              |')
	print(' ------------------------------------')
	print(response.json())
	if (response.status_code == 200):
		return response.json()['access_token']
	else: 
		print('No pudimos autenticar')


#Retrieves a list of uploaded documents.
def retrieves_a_list_of_uploaded_templates(access_token,folder_id,date_to,date_from='01/01/2020'):
	import requests

	headers = {
	    'accept': 'application/json',
	    'authorization': "Bearer %s" %access_token,
	}

	params = (
	    ('folder_id', str(folder_id)),
	    ('date_from', str(date_from)),
	    ('date_to', str(date_to)),
	    ('per_page', '2'),
	    ('page', '1'),
	    ('order', 'desc'),
	    ('order_by', 'id'),
	)

	response = requests.get('https://api.pdffiller.com/v2/templates', headers=headers, params=params)
	print(' --------------------------------------')
	print('|retrieves_a_list_of_uploaded_templates|')
	print(' --------------------------------------')
	print(response.json())
	return [response.json()['items'],response.json()['total']]	

#Subir un archivo desde una url
def upload_document_url(access_token,folder_id,url,name):
	import requests

	headers = {
	    'accept': 'application/json',
	    'authorization': "Bearer %s" %access_token,
	    'content-type': 'application/json',
	}

	params = (
	    ('with_tags', 'true'),
	)

	data = '{"folder_id":%d,"file":"%s","name":"%s"}'%(folder_id,url,name)
	response = requests.post('https://api.pdffiller.com/v2/templates', headers=headers, params=params, data=data)
	print(' --------------------------------------')
	print('|        upload_document_url          |')
	print(' --------------------------------------')
	print(response.json())
	
	return response.json()['id']

#Subir archivo desde un path
def upload_document_path(access_token,path,name,folder_id):
	url = 'https://api.pdffiller.com/v2/templates'
	headers = {
    	'authorization': "Bearer %s" %access_token
	}

	my_path=open(path,'rb')
	files = {
    	'file': (path, my_path),
	}
	data = {"name":name,"folder_id":folder_id}

	params = (
	    ('with_tags', 'true'),
	)
	response = requests.post(url, headers=headers, files=files,data=data,params=params)
	print(' --------------------------------------')
	print('|        upload_document_path         |')
	print(' --------------------------------------')
	print(response.json())
	if (response.status_code == 200):
		return response.json()['id']
	else: 
		print('No se pudo subir el archivo')

#Previews a document template.
def previews_document_template (access_token,document_id,pages='2',scale='100',max_width = '500',max_height='500'):
	import requests

	headers = {
	    'accept': 'application/json',
	    'authorization': "Bearer %s" %access_token,
	}

	params = '{"pages":"%s","scale":"%s","max_width":"%s","max_height":"%s"}'%(pages,scale,max_width,max_height)
	url = 'https://api.pdffiller.com/v2/templates/%s/previews'%document_id
	response = requests.get(url, headers=headers, params=params)
	print(' --------------------------------------')
	print('|     previews_document_template      |')
	print(' --------------------------------------')
	print(response.json())

#Copy any document: name the new document and select a destination folder.
def copy_documents (access_token,template_id,folder_id=0,name='copia'):
	import requests

	headers = {
	    'accept': 'application/json',
	    'authorization': "Bearer %s" %access_token,
	    'content-type': 'application/json',
	}

	data = '{"folder_id":0,"action":"copy","name":"%s"}' %(name)

	url= f'https://api.pdffiller.com/v2/templates/{template_id}%20'
	print(url)

	response = requests.post(url, headers=headers, data=data)
	print(' --------------------------------------')
	print('|           copy_document             |')
	print(' --------------------------------------')

	print(response.json())

#Share your document via URL
def share_the_document_via_link (access_token,template_id):
	import requests

	url = "https://api.pdffiller.com/v2/templates/%s/share"%template_id

	payload = "{\"accessType\":\"1\"}"
	headers = {
	    'accept': "application/json",
	    'authorization': "Bearer %s" %access_token,
	    'content-type': "application/json"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)	

#Retrieves information about a created document template.
def information_about_created_template(access_token,template_id):
	import requests

	url = "https://api.pdffiller.com/v2/templates/%s"%(template_id)

	headers = {
	    'accept': "application/json",
	    'authorization': "Bearer %s" %access_token
	    }

	response = requests.request("GET", url, headers=headers)

	print(response.text)

def updates_template_information(access_token,template_id,folder_id=0,name='prueba'):
	import requests

	headers = {
    'accept': 'application/json',
    'authorization': "Bearer %s" %access_token,
    'content-type': 'application/json',
	}

	data = '{"name":"%s","folder_id":%s}'%(name,folder_id)

	url = "https://api.pdffiller.com/v2/templates/%s"%template_id

	response = requests.post(url, headers=headers, data=data)
	print(response.json())

def deletes_document_template_item (access_token,template_id): 	
	import requests

	headers = {
    'accept': 'application/json',
    'authorization': "Bearer %s" %access_token,
	}
	url = "https://api.pdffiller.com/v2/templates/%s"%(template_id)
	response = requests.get(url, headers=headers)
	print('-------------------------')
	print ('|deletes_document_template_item|')
	print('-----------------')
	print(response.json())	

access_token= auth("9fd0316acc5708bd","11-11486@usb.ve","SFLbssW@7DeL6fV","sQMVpPxsAI1atkrroEasVubEgXZ3eVYy")
[documents,total] = retrieves_a_list_of_uploaded_templates(access_token,0,date.today().strftime("%m/%d/%Y"))
document_id_url = upload_document_url(access_token,0,"https://www.irs.gov/pub/irs-pdf/fw9.pdf","Sample_url")
document_id_path = upload_document_path(access_token,os.path.join(BASE_DIR,'pueba.pdf'),"Sample_Path",0)  

#previews_document_template (access_token,document_id_url)
#previews_document_template (access_token,document_id_path)
copy_documents(access_token,document_id_path)
share_the_document_via_link(access_token,document_id_path)
information_about_created_template(access_token,document_id_path)
updates_template_information(access_token,document_id_path)
deletes_document_template_item(access_token,document_id_path)