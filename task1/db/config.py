# для postgresql
#
# POSTGRES_USER = "kolya"
# POSTGRES_PASSWORD = "123"
# POSTGRES_SERVER = "localhost"
# POSTGRES_PORT = "5432"
# POSTGRES_DB = "B1"

# SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:" \
#                           f"{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:" \
#                           f"{POSTGRES_PORT}/{POSTGRES_DB}"


""" Путь к подключению СУБД """
SQLALCHEMY_DATABASE_URL = f"sqlite+pysqlite:///../b1.db"

