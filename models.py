"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

USER_IMG_DEFAULT = "https://www.freeiconspng.com/uploads/computer-user-icon-24.png"

class User(db.Model):
    """User model"""
    
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String,
                           nullable=False)
    
    last_name = db.Column(db.String,
                           nullable=False)
    
    image_url = db.Column(db.String,
                          nullable=False,
                          default=USER_IMG_DEFAULT)
    
    @property
    def get_full_name(self):
        """Return full name"""
        return f"{self.first_name} {self.last_name}"



class Post(db.Model):
    """Post model"""
    
    __tablename__ = "posts"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.String,
                      nullable=False)
    
    content = db.Column(db.Text,
                        nullable=False)
    
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default = datetime.datetime.now)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    
    
    
def connect_db(app):
    """Connect to database"""
    
    db.app = app
    db.init_app(app)