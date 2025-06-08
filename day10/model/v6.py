import os

os.environ['SECRET_KEY'] = 's3cr3t'

print("Secret key is",os.getenv("SECRET_KEY"))