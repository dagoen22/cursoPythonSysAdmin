#!/usr/bin/env python3

import requests as r
import json

url = 'http://gen-net.herokuapp.com/api/users'

#Lembrando que o r se refere ao modulo requests
res = r.get(url) #Requisição via método get
# print(dir(res)) //ver todos os atributos e metodos disponíveis

# users = res.json()
# for user in users:
#     print(user['name'])

# dados = {
#     "name":"Daniel",
#     "email":"danielasdfgh@4linux.com.br",
#     "password":"!23Mudar"
# }

# res = r.post(url=url,json=dados)
# print(res.json())

# pesquisa = {
#     "id" : "321"
# }

# res = r.get(url + '/321',params=pesquisa)
# print(res.json())

atualizacao = {
    "name" : "Batata Doce"
}

res = r.put(url,atualizacao)
