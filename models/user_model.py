from utils.database import db
from base_model import BaseModel
from utils.schema import ma 
from sqlalchemy import func


admin_user_class = db.Table(
    "admin_user_classes",
    db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("class_id", db.Integer(), db.ForeignKey("classes.id"))
)


class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(50))
    created = db.Column(db.DateTime(), server_default=func.now())    
    administred_classes = db.relationship("Class", secondary=admin_user_class, backref="admin_users")

    def __repr__(self):
        return f"<{self.id}, {self.username}>"