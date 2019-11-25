from app import *

insert = Blueprint('insert', __name__,
                   template_folder='templates')


@insert.route('/insert')
def insert_index():
    return render_template('insert_student.html')


@insert.route('/insert/student/')
def insert_student():
    id = request.args.get('id')
    name = request.args.get('name')
    dept_name = request.args.get('deptName')
    # id = request.form['id']
    # name = request.form['name']
    # dept_name = request.form['deptName']
    tot_cred = 0
    sql = f'INSERT INTO student VALUES ("{id}", "{name}", "{dept_name}", {tot_cred});'
    print(sql)
    if len(id) > 5:
        return jsonify({'stat': '学号超过5位'})
    with DB() as db_o:
        check_sql = f"SELECT * FROM student WHERE id={id}"
        had = db_o.execute(check_sql)
        if had:
            return jsonify({'stat': '学号冲突'})
        db_o.execute(sql)  # ok=1
    return jsonify({'stat': '插入完成'})
