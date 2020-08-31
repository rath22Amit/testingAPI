import requests
import json
import jsonpath

url='https://reqres.in/api/users'

def test_create_user():

    path=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\request.json','r')

    json_input=path.read()

    req_json=json.loads(json_input)

    print((req_json))
    response=requests.post(url,req_json)

    print(response.content)

    path.close()

    assert response.status_code == 201
    print("Passed")

    #Fetch_Information from header
    print(response.headers)

    print(response.headers.get('Content-Length'))

    #fetch_Information from response
    json_response=json.loads(response.text)
    name=jsonpath.jsonpath(json_response,'name')
    print(name[0])