from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import render_template

app = Flask(__name__)


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