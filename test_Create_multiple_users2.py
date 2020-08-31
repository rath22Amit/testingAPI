import jsonpath,json,requests,openpyxl

def test_Create_multiple2():
    uri="http://thetestingworldapi.com/api/studentsDetails"
    f=open('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\adduser.json','r')

    wk=openpyxl.load_workbook('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\TestData.xlsx')
    sh=wk['Sheet1']

    rows=sh.max_row
    json_req=json.loads(f.read())

#*****************************************Reading the data from the workbook************************************

    for i in range(2,rows+1):
        cell_first_name=sh.cell(row=i,column=1)
        cell_middle_name=sh.cell(row=i,column=2)
        cell_last_name = sh.cell(row=i, column=3)
        cell_dob = sh.cell(row=i, column=4)

        json_req['first_name']=cell_first_name.value
        json_req['middle_name'] = cell_first_name.value
        json_req['last_name'] = cell_first_name.value
        json_req['date_of_birth'] = cell_first_name.value

#********************************************Running the POST Request************************************
        json_response=requests.post(uri,json_req)


        print(json_response.content)
        res_json=json.loads(json_response.content)
        id=jsonpath.jsonpath(res_json,'id')

        sheet=wk.active
        c1=sheet.cell(row=i,column=5)
        c1.value=id[0]

        wk.save('C:\\Users\\acer\\Desktop\\python program\\APITest\\StudentManagementSystem\\TestDataUpdated.xlsx')




