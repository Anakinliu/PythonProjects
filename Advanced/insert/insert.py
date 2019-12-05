from app import *

insert = Blueprint('insert', __name__,
                   template_folder='templates')


@insert.route('/insert')
def insert_index():
    return render_template('insert_student_course.html')


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


@insert.route('/insert/course/')
def insert_course():
    c_id = request.args.get('cId')
    title = request.args.get('title')
    dept_name = request.args.get('deptName')
    cred = int(request.args.get('credit'))
    sql = f'INSERT INTO course' \
          f' VALUES ("{c_id}", "{title}", "{dept_name}", {cred});'
    print(sql)
    if cred <= 0:
        return jsonify({'stat': '学分要大于0'})
    with DB() as db_o:
        check_sql = f"SELECT * FROM course WHERE course_id={c_id}"
        had = db_o.execute(check_sql)
        if had:
            return jsonify({'stat': '课程号冲突'})
        db_o.execute(sql)  # ok=1
    return jsonify({'stat': '插入完成'})


@insert.route('/insert/take/<int:id>')
def insert_take(id):
    print(id)
    c_id = request.args.get('courseID')
    title = request.args.get('title')
    dept_name = request.args.get('deptName')
    sec_id = request.args.get('secID')
    print(c_id, title, dept_name, sec_id)
    get_s_y_sql = f'SELECT semester, YEAR FROM section WHERE course_id={c_id} AND sec_id = {sec_id};'
    with DB() as db_o:
        db_o.execute(get_s_y_sql)
        s_y_result = db_o.fetchall()
    print(s_y_result)
    if len(s_y_result) == 0:
        return jsonify({'stat': '没有开课！'})
    sem = s_y_result[0][0]
    year = int(s_y_result[0][1])
    insert_sql = f'INSERT INTO takes(ID, course_id, sec_id, semester, year) VALUES ({id}, {c_id}, {sec_id}, "{sem}", "{year}");'
    with DB() as db_o:
        dep_sql = f'SELECT course_id FROM takes WHERE id={id};'
        db_o.execute(dep_sql)
        token_course_id = db_o.fetchall()
        print('token: ', token_course_id)
        if token_course_id:
            if c_id in token_course_id[0]:
                return jsonify({'stat': '已经选过了'})
        db_o.execute(insert_sql)
    print(c_id, title, dept_name, sec_id)
    return jsonify({'stat': '插入完成'})