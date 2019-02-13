import datetime
import peewee
import sys
import pymysql
import inspect
import hashlib

db = peewee.MySQLDatabase("kivy_test", user="root", passwd="mysql")


def register(*args):
    for model in args:
        model.create_table()
        if issubclass(model, ManyToManyModel):
            for field in vars(model).items():
                if hasattr(field[0], "__class__"):
                    if isinstance(field[1], peewee.ManyToManyFieldAccessor):
                        s = getattr(model, field[0]).get_through_model()
                        db.create_tables([s])
                    

            


class PasswordField(peewee.CharField):
    def db_value(self, value):
        sha256 = hashlib.sha256()
        sha256.update(value.encode("utf-8"))
        return sha256.hexdigest()
    


class ManyToManyModel(object):
    pass


class BaseModel(peewee.Model):

    class Meta:
        database = db


class User(BaseModel):
    name = peewee.CharField()
    surname = peewee.CharField()
    email = peewee.CharField()
    password = PasswordField()

    def __str__(self):
        return self.name





class Message(BaseModel):
    text = peewee.CharField()
    send_by = peewee.ForeignKeyField(User)
    date_send = peewee.DateTimeField(default=datetime.datetime.now())

    def __str(self):
        return self.text



class Chat(BaseModel, ManyToManyModel):
    message = peewee.ManyToManyField(Message, backref="chats")
    user = peewee.ManyToManyField(User, backref="users")
    started = peewee.DateTimeField(default=datetime.datetime.now())

    
    def __str__(self):
        return self.tatada



register(User, Message ,Chat)

# u =  User.get_or_none(id=1)
# m = Message.get_or_none(id=1)
# c = Chat.get_or_none(id=1)
# print(c.message)


# u = User(name="asdas", surname="asdasd", email="asdasd")
# u.save()
# m = Message(text="asdasd", send_by=u)
# m.save()




if __name__ == "__main__":

    if "delete" in sys.argv:
        conn = pymysql.connect(host="localhost", user="root", password="mysql")
        conn.cursor().execute("DROP DATABASE " + db.database + ";")
        conn.cursor().execute("CREATE DATABASE " + db.database + ";")

