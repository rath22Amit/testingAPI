import json,jsonpath,requests

def test_get_Student_info():
    url='http://thetestingworldapi.com/api/studentsDetails/61019'
    response=requests.get(url)
    print(response.content)