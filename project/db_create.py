# project/db_create.py

from views import db
from model import Task
from datetime import date

#create the database and the table
db.create_all()

#insert data
# db.session.add(Task("Finish this tutorial", date(2015, 10, 7), 10, 1))
# db.session.add(Task("Finish Real Python", date(2015, 10, 20), 10, 1))

#commit the changes
db.session.commit()
