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
    return render_template('index.html', title='Home', user=user, hwData=result)

app.route('/view/<int:hwData_Index>, methods=['GET']
def record_view(hwData_Index):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT' * FROM tbl_hwImport WHERE fldIndex=%s', hwData_fldIndex')
1   result = cursor.fetchall()
    return render_template('view.html', title='View Form', height=result[0])

app.route('/view/<int:Index>, methods=['GET'])
def form_edit_get(hwData_Index):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT' * FROM tbl_hwImport WHERE fldIndex=%s', hwData_fldIndex')
1   result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', height=result[0])

app.route('/view/<int:Index>, methods=['POST'])
def form_update_post(hwData_Index):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldIndex'), request.form.get('fldHeight(Inches)'), request.form.get('fldWeight(Pounds)'), hwData_Index)
    sql_update_query = """UPDATE tbl_hwImport t SET t.fldIndex = %s, t.`fldHeight(Inches)`= %s, t.`fldWeight(Pounds)` = %s """
    cursor.execute(sql_update_query, inputData)
1   mysql.get_db().commit()
    return redirect("/", code=302)

app.route('/hwData/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New HW Form')

app.route('/view/<int:Index>, methods=['POST'])
def form_insert_post(hwData_Index):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldIndex'), request.form.get('fldHeight(Inches)'), request.form.get('fldWeight(Pounds)'))
    sql_insert_query = """INSERT INTO tbl_hwImport (fldIndex,'fldHeight(Inches)','fldWeight(Pounds)') VALUES (%s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
1   mysql.get_db().commit()
    return redirect("/", code=302)

app.route('/view/<int:Index>, methods=['POST'])
def form_delete_post(hwData_Index):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tbl_hwImport WHERE fldIndex =%s"""
    cursor.execute(sql_delete_query, inputData)
1   mysql.get_db().commit()
    return redirect("/", code=302)

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