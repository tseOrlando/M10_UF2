from connection import *

from create_table import create_table
from create import create
from delete import delete
from read import read
from update import update

from connection import psycopg2

try:

    create_table()
    create("3", "sel", "adADWcaDCV", "30", "M", 30)
    read()

    update("3", "F")
    read()

    delete("3")
    read()

except(Exception, psycopg2.Error) as e:
    print(f"err {e}")

finally:
    send.close()