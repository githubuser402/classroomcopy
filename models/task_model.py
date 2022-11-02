from sqlalchemy import func

from models.base_model import BaseModel
from models.document_model import DocumentSchema
from utils.database import db
from utils.schema import ma


class Task(db.Model, BaseModel):
    __tablename__ = "tasks"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200))
    public_id = db.Column(db.String(10))
    class_id = db.Column(db.Integer(), db.ForeignKey("classes.id"))
    created = db.Column(db.DateTime(), server_default=func.now())
    hand_in_by = db.Column(db.DateTime())
    documents = db.relationship("Document")


    def __repr__(self):
        return f"<{self.id}, {self.title[:25]}>"


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "public_id", "class_id", "created", "documents", "hand_in_by")

    id = ma.Number(dump_only=True)
    title = ma.String()
    public_id = ma.String()
    class_id = ma.String()
    created = ma.DateTime()
    documents = ma.Nested(DocumentSchema, many=True, only=["path",])
    hand_in_by = ma.String()