class Application:
    def __init__(self,application_Name,Catogory,company,app_size,no_of_users,rating):
        self.application_Name=application_Name
        self.Catogory=Catogory
        self.company = company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.rating=rating


    def sign_up(self):
        print(f"you signed up!,{self.application_Name}")

    def sign_up(self):
        print(f"welcome to appliaction,{self.application_Name}")

    def logout(self):
        print("thank  you for visting the application")

    def info(self):
        print(self.application_Name)
        print(self.Catogory)
        print(self.company)
        print(self.app_size)
        print(self.no_of_users)
        print(self.rating)

app = Application("Instagram","social media","Meta",6257,100,7.1)
app.sign_up()

app.info()