"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

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
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
def connect_db(app):
    """Connect to database"""
    
    db.app = app
    db.init_app(app)