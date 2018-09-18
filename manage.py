from app import create_app
from flask_script import Manager, Server

'''
creating app instance
'''
app= create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    '''
    run test for the whole application
    '''

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict (app=app)
    pass

if __name__ == '__main__':
    manager.run()