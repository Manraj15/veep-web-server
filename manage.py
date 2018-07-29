from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.add_command
def test():
    # TODO: add tests LUL
    pass

if __name__ == '__main__':
    manager.run()