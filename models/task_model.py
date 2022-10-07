from utils.database import db
from utils.schema import ma 
from base_model import BaseModel
from sqlalchemy import func

class Task(db.Model, BaseModel):
    __tablename__ = "tasks"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200))
    public_id = db.Column(db.String(10))
    class_id = db.Column(db.Integer(), db.ForeignKey("class.id"))

    def __repr__(self):
        return f"<{self.id}, {self.title[:25]}>"
