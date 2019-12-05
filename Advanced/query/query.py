from app import *

query = Blueprint('query', __name__,
                  template_folder='templates')


@query.route('/query/the/student/<int:id>')
def query_the_student(id):
    sql = f'SELECT * FROM student WHERE id={id};'
    print(sql)
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()
    return render_template('query_student.html',
                           ten_table=result,
                           curent_index=0)


@query.route('/query/student/')
@query.route('/query/student/<int:index>')
def query_student(index=1):
    if index < 1:
        index = 1
    print(index)
    sql = f'SELECT * FROM student ORDER BY id LIMIT 10 offset {(index - 1) * 10};'
    print(sql)
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()
    # try:
    #     cursor.execute(sql)
    #     result = cursor.fetchall()  # 元组
    #     print(result)
    # except:
    #     print('error in page_1 route')

    return render_template('query_student.html',
                           ten_table=result,
                           curent_index=index)


@query.route('/query/course/<int:id>')
def query_course(id):
    sql = f'SELECT course_id, title, dept_name, semester, YEAR, credits, grade FROM takes NATURAL JOIN course WHERE id={id}  ORDER BY course_id ASC;'
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()

    return render_template('query_course.html',
                           result_table=result,
                           id=id)


@query.route('/query/all_dept_name')
def query_all_dept_name():
    sql = 'SELECT dept_name FROM department;'
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()
    return jsonify(result)


@query.route('/query/dept_course/<deptName>')
def query_dept_course(deptName):
    dept_name = deptName
    sql = f'SELECT course_id, title FROM course WHERE dept_name = "{dept_name}" ;'
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()
    return jsonify(result)


@query.route('/query/course_id_by_title_and_dept_name/')
def course_id_by_title_and_dept_name():
    title = request.args.get("title")
    dept_name = request.args.get("deptName")
    sql = f'SELECT course_id FROM course WHERE title = "{title}" and dept_name="{dept_name}";'
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()
    print(f'result: {result}')

    return jsonify(result)


@query.route('/query/rank')
@query.route('/query/rank/')
def query_rank():
    sql = 'SELECT s.id, s.name, g.总学分 FROM student AS s NATURAL JOIN  ' \
          '(SELECT t.id, sum(c.credits) 总学分 FROM takes t NATURAL JOIN course c GROUP BY t.id) AS g' \
          ' ORDER BY g.总学分 DESC LIMIT 100 offset 0;'
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()

    return render_template('query_rank.html',
                           hundred_table=result)


@query.route('/query/sec_id/<int:course_id>')
def query_sec_id(course_id):
    print('course_id:' + str(course_id))
    sql = f'SELECT sec_id FROM SECTION WHERE course_id={course_id};'
    with DB() as db_o:
        db_o.execute(sql)
        result = db_o.fetchall()
    return jsonify(result)

