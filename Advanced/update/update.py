from app import *

update = Blueprint('update', __name__,
                   template_folder='templates')


@update.route('/update/take')
def update_take():
    # TMD js传+号要特殊处理。。。偷懒
    ok = ['A+', 'A', 'A-',
          'B+', 'B', 'B-',
          'C+', 'C', 'C-']
    id = request.args.get('id').strip()
    # print('id=', id)
    grade = request.args.get('grade').strip()
    grade = ok[int(grade) - 1]
    # print(grade)
    c_id = request.args.get('c_id').strip()
    # print(c_id)
    # sql中grade加引号
    sql = f'UPDATE takes SET grade="{grade}" WHERE id={id} AND course_ID={c_id};'
    # print(sql)
    with DB() as db_o:
        db_o.execute(sql)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     # print((result))
    # except:
    #     print('error in updare_take route, rollback...')
    #     db.rollback()
    return redirect(url_for('query.page_2', id=id))
