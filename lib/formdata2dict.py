def form_data2dict(form_data):
    data_dict = {}
    data_list = form_data.split("&")
    for data in data_list:
        key_value_list = data.split("=")
        data_dict[key_value_list[0]] = key_value_list[1]
    return data_dict


form_data = "shiftType=7&flag=&stuStatus=1&IsAttend=&shiftID=&shiftName=&classId=&className=&campusid=ee0b9bd9-6fdc-4184-b31d-42a2a49867ee&query=Auto_new_xy_0418102408&sDate=2018-03-21&eDate=2018-04-19&desc=1&sort=Serial&teacherId=&masterUserId=&headMasterId=&PageSize=10&PageIndex=1&TotalCount=2&PageCount=1"
print form_data2dict(form_data)
