from mongoengine import *

# Connect to the database called 'some_database_name'. If it doesn't exist, create the database.
db_connection = connect('some_database_name')

# Clear the database
db_connection.drop_database('some_database_name')


class User(Document):  # Every object stored in Mongodb is of the type "Document"
    name = StringField(max_length=10)
    age = IntField(default=18)


# Creates an object called data0/1 of User type with name and age specified
data0 = User(name="Ernst", age=25)
data1 = User(name="Rutherford")

# Saves (creates) the object data0/1 in Mongodb
data0.save()
data1.save()

# Accessing the list of User objects saved in Mongodb
for each_data in User.objects:
    print(each_data.name, each_data.age)

# Updating objects

# Returns a list of users with name=Ernst from which we select the first user
updated_user = User.objects(name="Ernst").first()
updated_user.name = "Amanda"  # Change Ernst to Amanda
updated_user.save()   # Save after updating an object

print("Users after updating database:")
for each_data in User.objects:
    print(each_data.name, each_data.age)
