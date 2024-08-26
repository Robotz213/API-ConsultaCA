from app import db
from app import app
from app.models.ca import CaTable
from app.models.users import Users

from app.misc.gen_seed import generate_id

with app.app_context():
    
    db.create_all()
    
    usr = Users.query.filter(Users.username == "root").first()
    if not usr:
        
        pw = generate_id()
        user = Users(
            username = "root",
            senhacrip = pw
        )
        
        db.session.add(user)
        db.session.commit()
        
        print(f" * Password: {pw}")
        