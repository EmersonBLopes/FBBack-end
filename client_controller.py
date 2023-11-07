import pandas as pd
import openpyxl
class Client:

    #def __init__(self):


    def get_users(self):

        data_frame = pd.read_excel("database.xlsx","usuarios")
        return data_frame.to_json(orient="records")

    def add_user(self,new_user):
        df = pd.DataFrame([[new_user.get_id(),new_user.get_name()]],columns=["ID","name"]) 
        print(df)
        df.to_excel("database.xlsx","usuarios",index=False)
