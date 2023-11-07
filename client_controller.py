import pandas as pd
import openpyxl
class Client:

    def __init__(self):

        self.__users_list = ["Joaozinho","Pedrinho","Mariasinha"]
    
    def get_users(self):
        return self.__users_list;

    def add_user(self,new_user):
        df = pd.DataFrame([new_user.get_name()],index=[new_user.get_id()]) 
        df.to_excel("database.xlsx","usuarios",index=True, header=False)
        print(df)
