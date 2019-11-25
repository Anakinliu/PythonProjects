from app import *

query = Blueprint('query', __name__,
                  template_folder='templates')


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
