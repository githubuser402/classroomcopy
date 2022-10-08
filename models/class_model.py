from utils.database import db
from utils.schema import ma 
from models.base_model import BaseModel
from sqlalchemy import func
from models.task_model import TaskSchema

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

    
class ClassSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "public_id", "description", "created", "tasks")

    id = ma.Number(dump_only=True)
    name = ma.String()
    public_id = ma.String()
    description = ma.String()
    created = ma.DateTime()
    tasks = ma.Nested(TaskSchema)
    