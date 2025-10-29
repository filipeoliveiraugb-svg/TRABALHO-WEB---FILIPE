from django.shortcuts import render
import requests

def home(request):
 if request.method == "GET":
  url = "http://127.0.0.1:8001/API/medicamentos"
  response = requests.get(url)
  if response.status_code == 200:
   medicamentos=response.json()
  else : 
   medicamentos=[ ]
  return render(request,'Empresa.html',{'medicamentos':medicamentos})
  