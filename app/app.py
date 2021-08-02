from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'hwData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'hw project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tbl_hwImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, hw=result)

app.route('/view/<int:Index>, methods=['GET'])
def record_view(Index))


def hw_import() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'hwData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tbl_hwImport')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


@app.route('/')
def index():
    user = {'Guest'}
    hw_data = hw_import()

    return render_template('index.html', title='Home', user=user, hw_data=hw_import)

@app.route('/api/hw')
def hw() -> str:
    js = json.dumps(hw_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')