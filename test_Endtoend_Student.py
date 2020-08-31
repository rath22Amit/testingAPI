import json,jsonpath,requests

def test_Create_Student():
    global id
    create_uri='http://thetestingworldapi.com/api/studentsDetails'
    path=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\adduser.json','r')
    json_request=json.loads(path.read())

    response=requests.post(create_uri,json_request)

   # print(response.content)

    json_response=json.loads(response.content)

    id=jsonpath.jsonpath(json_response,'id')
    print(id[0])

def test_Update_Student():
    update_uri='http://thetestingworldapi.com/api/studentsDetails/'+str(id[0])
    print(update_uri)
    path=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\updateuser.json','r')
    json_request=json.loads(path.read())
    json_request['id']=id[0]
    response=requests.put(update_uri,json_request)

    print(response.status_code)

def test_Fetch_Student():
    get_uri=f'http://thetestingworldapi.com/api/studentsDetails/{id[0]}'
    print(get_uri)

    response=requests.get(get_uri)
    print(response.status_code)

