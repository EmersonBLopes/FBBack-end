class User:

    def __init__(self,id,name,email):
        self.__id = id
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

