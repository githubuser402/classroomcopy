from utils.database import db
from utils.schema import ma 
from base_model import BaseModel
from sqlalchemy import func


class Class(db.Model, BaseModel):
    __tablename__ = "classes"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    public_id = db.Column(db.String(10))
    description = db.Column(db.Text())
    created = db.Column(db.DateTime(), server_default=func.now())
    tasks = db.relationship("Task", backref="class")

    def __repr__(self):
        return f"<{self.id}, {self.name}>"