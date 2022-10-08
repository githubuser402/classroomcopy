from utils.database import db
from models.base_model import BaseModel
from utils.schema import ma 
from sqlalchemy import func
from models.class_model import ClassSchema
from passlib.hash import pbkdf2_sha256 as sha256

admin_user_class = db.Table(
    "admin_user_classes",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("class_id", db.Integer(), db.ForeignKey("classes.id"))
)

student_class = db.Table(
    "student_class",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("class_id", db.Integer(), db.ForeignKey("classes.id"))
)


class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    created = db.Column(db.DateTime(), server_default=func.now())    
    administred_classes = db.relationship("Class", secondary=admin_user_class, backref="admin_users")
    study_classes = db.relationship("Class", secondary=student_class, backref="students")

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(hash, password):
        return sha256.verify(password, hash)

    def __repr__(self):
        return f"<{self.id}, {self.username}>"


class UserSchema(ma.Schema):
    class Meta:
        fileds = ("id", "username", "password", "created", "administred_classes", "study_classes")

    id = ma.Number(dump_only=True)
    username = ma.String()
    password = ma.String()
    created = ma.DateTime()
    administred_classes = ma.Nested(ClassSchema)  