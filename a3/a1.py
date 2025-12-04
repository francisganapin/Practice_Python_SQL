from dotenv import load_dotenv
import os


load_dotenv()

db_user = os.getenv('DB_HOST')
db_pass = os.getenv('DB_USER')


print(db_user,db_pass)