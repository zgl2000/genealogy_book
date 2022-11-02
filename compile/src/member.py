
# 成员对象，包含三部分信息：
# 1. 自身信息
# 2. 其父信息（包含继父信息）
# 3. 子女列表


class Member:
    def __init__(self, member_id, father_id, step_father_id, order_seq, step_order_seq, member_name, sex,
                 descent_no, spouse_name, career, description, spouse_description, subtype, pre_member_id, next_member_id, mother_name):
        self.member_id = member_id
        self.father_id = father_id
        self.step_father_id = step_father_id
        self.order_seq = order_seq if order_seq is not None else 0
        self.step_order_seq = step_order_seq if step_order_seq is not None else 0

        # 当成员名字大于4个字(不含括号部分)或首字非张时，保留全名，否则把张姓去掉
        #self.member_name = member_name if len(member_name) > 3 or member_name[0] != '张' else member_name[1:]
        self.member_name = member_name if len(member_name) > 3 and '(' not in member_name or member_name[0] != '张' else member_name[1:]

        self.sex = sex
        self.descent_no = descent_no
        self.spouse_name = spouse_name

        self.career = career
        self.description = description
        self.spouse_description = spouse_description
        self.subtype = subtype

        # 存储当前成员的前驱和后继成员ID，前驱后继仅针对于上世未详的成员
        self.pre_member_id  = pre_member_id
        self.next_member_id = next_member_id

        # 存储母亲信息
        self.mother_name = mother_name

        # 存储其子女对象（亲生+过继+义子）
        self.child_list = []

        # 法律上的子女
        self.legal_child_list = []

    def add_child(self, child_obj):
        self.child_list.append(child_obj)

    def add_legal_child(self, childobj):
        self.legal_child_list.append(childobj)

    # 打印输出成员对象
    def print_out(self):
        print(self.member_id, self.member_name,self.descent_no),
        for child in sorted(self.child_list, key=lambda c: c.order_seq):
            print(child.member_name),
        print("\n")


class MemberNode:
    def __init__(self,member_id, member_name, sex, descent_no,spouse_name, className):
        self.member_id = member_id
        self.member_name = member_name
        self.sex = sex
        self.descent_no = descent_no
        self.spouse_name = spouse_name
        self.className = className
        self.children = [] # 变量名必须为 children， 否则无法展示

    def add_child(self, child_obj):
        self.children.append(child_obj)


if __name__ == "__main__":
    member_obj = Member(1, 2, None, 1, None, 'a', 1, 10, '', '', '', '', '温庄')
    member_obj.print_out()
