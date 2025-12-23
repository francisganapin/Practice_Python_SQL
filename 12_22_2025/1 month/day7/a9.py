class User:
    def permission(self):
        return['read']

class Admin(User):
    def permission(self):
        return super().permission() + ['delete']

class Editor(User):
    def permission(self):
        return super().permission() + ['edit']
    

class SuperUser(Admin,Editor):
    def permission(self):
        return super().permission() + ['super']
    

print(SuperUser.__mro__)


s = SuperUser()
print(s.permission())