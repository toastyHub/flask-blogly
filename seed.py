"""Seed file to make sample data for db."""

from models import db, connect_db, User, Post
from app import app


# Create all tables
db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()

# Add sample users
u1 = User(first_name='Ciara', last_name='Zelaya')
u2 = User(first_name='Daniel', last_name='Morales')
u3 = User(first_name='Chad', last_name='Stone')



db.session.add_all([u1, u2, u3])
db.session.commit()


