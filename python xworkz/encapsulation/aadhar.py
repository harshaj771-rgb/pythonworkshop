class Aadhar:
    def __init__(self, name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina


    def display_user(self):
        print(self.name)
        print(self.aadhar_number)
        print(self.dob)
        print(self._finger_print)
        print(self.__retina)




aadha=Aadhar("xyz",9136782385,"1-mar-2004",True,True)
aadha.display_user()

