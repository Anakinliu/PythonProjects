from app import *

delete = Blueprint('delete', __name__,
                   template_folder='templates')


@delete.route('/delete/take')
def delete_take():
    id = request.args.get('id').strip()
    # print('id=', id)
    c_id = request.args.get('c_id').strip()
    # print(c_id)
    # sql中grade加引号
    sql = f'DELETE FROM takes WHERE id="{id}" AND course_id = {c_id};'
    with DB() as db_o:
        db_o.execute(sql)
    # print(sql)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # print((result))
    # except:
    #     print('error in delete_take route, rollback...')
    #     db.rollback()
    return redirect(url_for('query.query_course', id=id))


@delete.route('/delete/student')
def delete_student():
    id = request.args.get('id').strip()
    # print('id=', id)
    reload_index = request.args.get('index').strip()
    # print(reload_index)
    # sql中grade加引号
    sql = f'DELETE FROM student WHERE id="{id}";'
    # print(sql)
    with DB() as db_o:
        db_o.execute(sql)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # print((result))
    # except:
    #     print('error in delete_student route, rollback...')
    #     db.rollback()
    return redirect(url_for('query.query_student', index=reload_index))
