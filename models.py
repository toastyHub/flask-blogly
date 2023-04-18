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
    
    posts = db.relationship("Post",
                            backref="user",
                            cascade="all, delete-orphan")
    
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
    

class PostTag(db.Model):
    """Post tag model."""
    
    __tablename__ = "posts_tags"
    post_id = db.Column(db.Integer,
                        db.ForeignKey("posts.id"),
                        primary_key=True)
    
    tag_id = db.Column(db.Integer,
                       db.ForeignKey("tags.id"),
                       primary_key=True)



class Tag(db.Model):
    """Tag model"""
    
    __tablename__ = "tags"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False,
                     unique=True)
    
    posts = db.relationship('Post',
                            secondary="posts_tags",
                            backref="tags")
    


                                          
    
    
def connect_db(app):
    """Connect to database"""
    
    db.app = app
    db.init_app(app)