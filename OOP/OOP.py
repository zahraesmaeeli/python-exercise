class student:                               #loging
    users=[]
    def __init__(self,name,Email,password):
        self.name=name
        self.Email=Email
        self.password=password
    def __repr__(self):
        return f"{self.name}"
        # print(f"{self.name} Welcome!!")
        # student.users.append(self.name)

zahra=student("zahra","zahraesmaeeli@gmail.com",12345)
print(zahra)




