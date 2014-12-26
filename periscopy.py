from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


appv = Flask(__name__)
appv.config['SQLALCHEMY_DATABASE_URI'] = 'vertica+pyodbc://dbadmin:dbadmin@vertica_deploy_test_db'
appv.debug = True
dbv = SQLAlchemy(appv)

class TodoVertica(dbv.Model):
    id = dbv.Column(dbv.Integer, dbv.Sequence('myseq'), primary_key=True )
    title = dbv.Column(dbv.VARCHAR, unique=False)
    is_completed = dbv.Column(dbv.Boolean)

    def __init__(self, title):
        self.title = title
        self.is_completed = False


meta = dbv.MetaData()
desc = dbv.Table('vv_claim_program_cd_descriptions', meta, autoload=True, autoload_with=dbv.engine)
print([c.name for c in desc.columns])


@appv.route('/')
def index():
    todos = TodoVertica.query.all()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    #app.run()
    appv.run()

#app.debug = True