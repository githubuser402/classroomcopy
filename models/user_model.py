from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import func

from models.base_model import BaseModel
from models.class_model import ClassSchema
from utils.database import db
from utils.schema import ma

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

student_task = db.Table(
    "student_task",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("student_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("task_id", db.Integer(), db.ForeignKey("tasks.id")),
    db.Column("handed_in", db.Boolean()),
    db.Column("hand_in_time", db.DateTime())
)

student_document = db.Table(
    "student_documents",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("document_id", db.Integer(), db.ForeignKey("documents.id"))
)

admin_document = db.Table(
    "admin_documents",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("document_id", db.Integer(), db.ForeignKey("documents.id"))
)


class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(100))
    slug = db.Column(db.String(20))
    created = db.Column(db.DateTime(), server_default=func.now())    
    verified = db.Column(db.Boolean(), default=False, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True) 
    administred_classes = db.relationship("Class", secondary=admin_user_class, backref="admin_users")
    study_classes = db.relationship("Class", secondary=student_class, backref="students")
    tasks = db.relationship("Task", secondary=student_task, backref="students")
    student_documents = db.relationship("Document", secondary=student_document)
    admin_documents = db.relationship("Document", secondary=admin_document)
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
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
        fileds = ("id", "username", "password", "created", "administred_classes", "study_classes", "email", "verified")

    id = ma.Number(dump_only=True)
    username = ma.String()
    email = ma.String()
    verified = ma.Boolean(dump_only=True)
    password = ma.String()
    created = ma.DateTime()
    administred_classes = ma.Nested(ClassSchema)  