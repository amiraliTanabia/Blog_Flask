class Employee:
    def __init__(self, name, lname, pay):
        self.name = name
        self.lname = lname
        self.pay = pay

    raise_mnt = 1.05
    @property
    def Fullname(self):
        return f'{self.name} {self.lname}'
    @property
    def email(self):
        return '{}.{}@Employee.com'.format(self.name, self.lname)

    def applye_raise(self):
        self.pay = int(self.pay * Employee.raise_mnt)
d = Employee('fff', '55' , 44)
print(dict(d))
