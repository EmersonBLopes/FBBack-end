class User:

    def __init__(self,id,first_name,last_name,email):
        self.__id = id
        self.__name = first_name
        self.__last_name = last_name
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name
    
    def get_email(self):
        return self.__email
