import os
import json
class CreateJsonFile:
    def __init__(self):
        pass
    def read_input_csv_data(self):
        ''' this function is used to read the input csv data'''
        f = open("data.csv", "r")
        data=f.readlines()
        return data
    def convert_data_to_dict(self,data):
        ''' this function is used to convert the data from raw data to dict'''
        res=[]
        col_list=[]
        for key,row in enumerate(data):
            if key==0:
                col_list=row.split(',')
            else:
                row_data_list=row.split(',')
                row_res={}
                for cnt, value in enumerate(row_data_list):
                    if col_list[cnt].replace('\n' ,'')=="Floor Level":
                        row_res[col_list[cnt].replace('\n' ,'')]=int(value.replace('\n' ,''))
                    else:
                        row_res[col_list[cnt].replace('\n', '')] = value.replace('\n', '')
                res.append(row_res)
        return res
    def write_json_data(self,res_dict):
        ''' this function is used to write the json data'''
        with open('result.json', 'w') as fp:
            json.dump(res_dict, fp,indent=4)

    def run(self):
        ''' this is to run the main function to run the class'''
        raw_data=self.read_input_csv_data()
        res_dict=self.convert_data_to_dict(raw_data)
        self.write_json_data(res_dict)
r=CreateJsonFile()
r.run()