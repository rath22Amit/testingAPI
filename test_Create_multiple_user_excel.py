import json,jsonpath,requests,openpyxl
import json_excel_converter
from json_excel_converter import Converter
from json_excel_converter.xlsx import Writer
def test_create_multiple_Students():
    uri='http://thetestingworldapi.com/api/studentsDetails'
    f=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\adduser.json','r')
    wk=openpyxl.load_workbook('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\TestData.xlsx')
    wk2=openpyxl.load_workbook('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\New_Book.xlsx')
    sh=wk['Sheet1']
    rows=sh.max_row
    sh2=wk2.active

    json_req=json.loads(f.read())
    m=[]
    for j in json_req:
        # print(j)
        m.append(j)
        # x=sh2.cell(row=1,column=j)
        # x.value(m[j])
        # wk2.save('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\New_Book.xlsx')
    for k in range(len(m)):
        new_sheet=wk2.active
        c2=new_sheet.cell(row=1,column=k+1)
        c2.value=m[k]
    wk2.save('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\New_Book2.xlsx')
    # print(m)
    # conv=Converter()
    # conv.convert(json_req,Writer(file='C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\New_Book3.xlsx'))
    for i in range(2,rows+1):
        global id
        cell_first_name=sh.cell(row=i,column=1)
        cell_middle_name = sh.cell(row=i, column=2)
        cell_last_name = sh.cell(row=i, column=3)
        cell_dob = sh.cell(row=i, column=4)

        json_req['first_name']=cell_first_name.value
        json_req['middle_name'] = cell_middle_name.value
        json_req['last_name'] = cell_last_name.value
        json_req['date_of_birth'] = cell_dob.value

        response=requests.post(uri,json_req)

        print(response.status_code)
        print(response.text)
        json_response=json.loads(response.text)
        id=jsonpath.jsonpath(json_response,'id')
        print(id[0])
        sheet=wk.active
        c1=sheet.cell(row=i,column=5)
        c1.value=id[0]
        wk.save('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\TestDataupdated.xlsx')

