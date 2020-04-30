#Script para ir modulando los api que han ido funcionando 
import requests
import os
import math

#Funcion que de vuelve el token de autentificacion
def auth(client_id,username,password,client_secret):
	url = "https://api.pdffiller.com/v2/oauth/token"
	payload = '{"grant_type":"password","client_id":"%s","username":"%s","password":"%s","client_secret":"%s"}'%(str(client_id),str(username),str(password),str(client_secret))
	headers = {
    'accept': "application/json; charset=UTF-8",
    'content-type': "application/json"
    }

	response = requests.post(url, data=payload, headers=headers)
	print (response)
	if (response.status_code == 200):
		return response.json()['access_token']
	else: 
		print('No pudimos autenticar')

#Cantidad de archivo en una carpeta en especifico

