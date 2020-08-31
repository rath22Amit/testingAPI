import json,jsonpath,requests

url='https://reqres.in/api/users'

file_path=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\request.json','r')

def test_user1():
    json_req=file_path.read()
    response1=requests.post(url,json_req)
    assert response1.status_code==201
   # print(response1.content)

def test_user2():
    json_req = file_path.read()
    response2 = requests.post(url, json_req)
    assert response2.status_code == 201
