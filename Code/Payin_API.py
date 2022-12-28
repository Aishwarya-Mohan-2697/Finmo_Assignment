'''
    Payin_API class contains methods to create and retrieve Payins.
    Pre-requisite : Customer and Wallet must be created prior to running these tests.
    Datafiles : Create_Payin.json -> Contains required info to create a Payin
                Input_values.json -> Contains commonly used inputs like headers
'''
import requests
import json
import os
from datetime import datetime
create_payin_details = os.path.abspath(os.path.join(os.curdir,"Datafiles","Create_Payin.json"))
input_details = os.path.abspath(os.path.join(os.curdir,"Datafiles","Input_values.json"))

class Payin_API():
    def retrieve_all_payins(self):
        current_date = datetime.today().strftime('%Y-%m-%d')
        url = "https://api.finmo.net/v1/payin?status=PENDING&created_at="+current_date
        headers = self.obtain_header_info()
        payload={}
        response = requests.get(url, headers=headers, data=payload)
        binary = response.content
        output = json.loads(binary)
        status_code = output["status_code"]
        return status_code

    def create_payin(self):
        url = "https://api.finmo.net/v1/payin"
        headers = self.obtain_header_info()
        file_object = open(create_payin_details,"r")
        payload = json.load(file_object)
        payload = json.dumps(payload)
        response = requests.request("POST",url,headers=headers, data=payload)
        binary = response.content
        output = json.loads(binary)
        payin_id = output["data"]["payin_id"]
        status_code = output["status_code"]
        return payin_id, status_code

    def retrieve_payin_based_on_payin_id(self, payin_id):
        headers = self.obtain_header_info()
        url = "https://api.finmo.net/v1/payin/"+payin_id
        payload={}
        response = requests.get(retrieve_url, headers=headers, data=payload)
        binary = response.content
        output = json.loads(binary)
        status_code = output["status_code"]
        print(output)
        return output
        # return status_code

    def obtain_header_info(self):
        file_object = open(input_details,"r")
        content = json.load(file_object)
        header_info = content
        header_info = header_info["headers"]
        return header_info

