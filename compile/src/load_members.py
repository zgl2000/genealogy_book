from dbmanager import DbManager
from member import Member


# 根据 member_id 获取成员对象,
# 优先在词典中查询，若找到，则直接返回，否则根据记录指针进行构造
def get_member_obj(member_dict, member_id, r):
    member_obj = member_dict.get(member_id, None)
    if member_obj is None:
        member_obj = Member(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15])
        member_dict[member_obj.member_id] = member_obj
    #member_obj.print_out()
    return member_obj


# 加载成员对象
def load_members():
    member_dict = {}

    columns = "member_id, father_id, step_father_id, order_seq, step_order_seq, \
               member_name, sex, descent_no, spouse_name, career, description, spouse_description, subtype, pre_member_id, next_member_id, mother_name"

    db_manager = DbManager()
    cur = db_manager.conn.cursor()
    cur_c = db_manager.conn.cursor()
    cur_s = db_manager.conn.cursor()

    cur.execute("SELECT " + columns + " FROM tb_members WHERE descent_no < 30 and descent_no > 0")
    for r in cur:
        member_id = r[0]
        member_obj = get_member_obj(member_dict, member_id, r)

        # 获取其子女对象
        cur_c.execute("SELECT " + columns + " FROM tb_members WHERE father_id = " + str(member_id))
        for c in cur_c:
            child_member_id = c[0]

            child_member_obj = get_member_obj(member_dict, child_member_id, c)

            # 将子女对象添加到生父的子女对象列表中
            member_obj.add_child(child_member_obj)

            # 将子女对象添加到对应的继父的子女对象列表中
            step_father_id = child_member_obj.step_father_id
            if step_father_id is not None:
                cur_s.execute("SELECT " + columns + " FROM tb_members WHERE member_id = " + str(step_father_id))
                s = cur_s.fetchone()
                step_father_obj = get_member_obj(member_dict, step_father_id, s)
                step_father_obj.add_child(child_member_obj)

                # 过继子女为其合法子女
                step_father_obj.add_legal_child(child_member_obj)
            else:
                # 若无过继关系，则其亲生子女则为其合法子女
                member_obj.add_legal_child(child_member_obj)

    cur.close()
    cur_c.close()
    cur_s.close()
    db_manager.close()

    return member_dict


if __name__ == "__main__":
    dicts = load_members()
    for key, obj in dicts.items():
        obj.print_out()
