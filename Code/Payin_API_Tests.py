'''
    Payin_API_Tests class contains methods/tests to create and retrieve Payins (calls methods from Payin_API class).
    Pre-requisite : Customer and Wallet must be created prior to running these tests.
    Enhancements to be done : 1. When a Payin is created, the status is "PENDING". In order to complete it, Simulating the Payin has to be done, which is currently not implemeneted here.
                   2. Logging and parsing of output to a log file
'''
from Payin_API import Payin_API
import os
result_file = os.path.abspath(os.path.join(os.curdir,"Logs","result.json"))

class Payin_API_Test():
    def retrieve_API_test(self, payin_id):
        output = Payin_API().retrieve_payin_based_on_payin_id(payin_id)
        status_code = output["status_code"]
        print(status_code)
        if status_code != 200:
            return "FAIL", "Invalid Payin id"
        else:
            payin_info = output["data"][0]["status"]
            print(payin_info)
            ### send the output to json file###
            return "PASS", "Payin details for payin_id: "+payin_id+"obtained successfully"
        
    def create_API_test(self):
        payin_id, status_code = Payin_API().create_payin()
        if status_code == 201:
            return "Successfully created a Payin", payin_id, status_code
        else:
            return "Unable to create a Payin. Ensure all details are updated for customer","",status_code

    def main():
        payin_id, status_code = Payin_API_Test().create_API_test()
        status, message = Payin_API_Test().retrieve_API_test(payin_id)
        print(message)

Payin_API_Test().main()