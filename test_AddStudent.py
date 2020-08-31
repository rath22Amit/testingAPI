import json,jsonpath,requests

def test_AddStudent():
    url='http://thetestingworldapi.com/api/studentsDetails'
    path=open('C:\\Users\\acer\Desktop\\python program\\APITest\\StudentManagementSystem\\adduser.json')
    json_input=json.loads(path.read())

    response=requests.post(url,json_input)

    print(response.headers)

    assert response.status_code==201

