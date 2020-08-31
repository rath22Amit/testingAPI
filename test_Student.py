import json,jsonpath,requests
global id

def test_add_New_Student():

#*********************Creating a New Student************************************

    uri='http://thetestingworldapi.com/api/studentsDetails'
    file_path=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\adduser.json','r')
    json_req=json.loads(file_path.read())

    response=requests.post(uri,json_req)

    print(response.content)

    json_res=json.loads(response.content)

    id=jsonpath.jsonpath(json_res,'id')

    print(id[0])


#************************Updating the Student Information****************************

    uri3=f'http://thetestingworldapi.com/api/studentsDetails/{id[0]}'
    file_path2=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\updateuser.json','r')
    json_req3=json.loads(file_path2.read())

    response3=requests.put(uri3,json_req3)

    print(response3.text)

    #json_res3=json.loads(response3.content)




#***********************Fetching the Student Information****************************

    uri2=f'http://thetestingworldapi.com/api/studentsDetails/{id[0]}'
    print(uri2)
    response2=requests.get(uri2)
    print(response2.content)

    json_res2=json.loads(response2.content)
    id2=jsonpath.jsonpath(json_res2,'data.id')
    print(response2.content)





