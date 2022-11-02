from sqlalchemy import func

from models.base_model import BaseModel
from utils.database import db
from utils.schema import ma


class Document(db.Model, BaseModel):
    __tablename__ = "documents"

    id = db.Column(db.Integer(), primary_key=True)
    path = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    task_id = db.Column(db.Integer(), db.ForeignKey("tasks.id"))


class DocumentSchema(ma.Schema):
    class Meta:
        fields = ("id", "path", "user_id", "task_id")

    id = ma.Number(dump_only=True)
    path = ma.String()
    user_id = ma.Number(dump_only=True)
    task_id = ma.Number(dump_only=True)