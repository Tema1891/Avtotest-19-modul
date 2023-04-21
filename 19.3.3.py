import requests
import json
status = 'available'
headers = {"accept": 'application/json',
           "Content-type": "application/json",
           "auth_key": "15b2a066c353d88c6843d3b4302229ce91ceee0f207a143269d61aa9"}

data = {

        "id": 0,
        "username": "Tema",
        "firstName": "Tema",
        "lastName": "Frolov",
        "email": "frollov.a@mail.ru",
        "password": "Netnett1manstar?",
        "phone": "89009947551",
        "userStatus": 0
    }
data1 = {
  "_id": "",
  "age": "2",
  "animal_type": "dog",
  "created_at": "1682023952.1524951",
  "id": "8ecb43db-dc23-4abe-8fd7-b3f217fe8667",
  "name": "Шарик",
  "pet_photo": "",
  "user_id": "15b2a066c353d88c6843d3b4302229ce91ceee0f207a143269d61aa9"
}
data2 = {
    'name': 'test',
    'animal_type': 'test',
    'age': '111'
}
# res = requests.get(f'http://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={"accept":'application/json'})
# if 'application/json' in res.headers['Content-Type']:
#     res.json()
# else:
#     res.text
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(type(res.json()))
#
# res1 = requests.post(f'https://petstore.swagger.io/v2/user', headers=headers, data=json.dumps(data))
# res2= requests.post(f'https://petfriends.skillfactory.ru/api/create_pet_simple',headers=headers,json=data2 )
# res3 = requests.put(f'https://petfriends.skillfactory.ru/api/pets/1504d7df-fb00-4393-9d64-1062ed2278d6', headers=headers, json=data2)
res4 = requests.delete(f'https://petfriends.skillfactory.ru/api/pets/0a81dfa1-6b69-4c22-a123-70f8d453ef27',headers=headers)
print(res4.status_code)
print(res4.text)

