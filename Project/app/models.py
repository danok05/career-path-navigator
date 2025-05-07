from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    skills = db.Column(db.Text)

    work_history = db.relationship('WorkHistory', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class WorkHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_title = db.Column(db.String(120))
    company = db.Column(db.String(120))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)


class JobProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    required_hard_skills = db.Column(db.Text)
    required_soft_skills = db.Column(db.Text)
    seniority_level = db.Column(db.String(30))


class RoadmapStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_job_id = db.Column(db.Integer, db.ForeignKey('job_profile.id'), nullable=False)
    to_job_id = db.Column(db.Integer, db.ForeignKey('job_profile.id'), nullable=False)
    action_items = db.Column(db.Text)