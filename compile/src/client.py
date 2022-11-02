from load_members import load_members
import family_tree_orgcharts
import family_tree_networkx
import family_tree_pygraphviz

import genealogy_book
import circular_tree


def gen_circular_tree():
    first_member_id = 1
    circular_tree.gen_graph(member_dict, first_member_id)


def gen_book():
    first_member_id = 1 
    file_name = "data/family_book.md"
    genealogy_book.gen_book(member_dict, first_member_id, file_name)


def gen_org_tree():
    first_member_id = 2896
    if first_member_id == 1:
        file_name = "../data/orgchart_tree.html"
    else:
        file_name = "../data/orgchart_tmp.html"
    family_tree_orgcharts.draw_tree(member_dict, first_member_id, file_name)


def gen_networkx_tree():
    first_member_id = 40
    if first_member_id == 1:
        file_name = "data/networkx_tree.svg"
    else:
        file_name = "data/networkx_tmp.svg"
    family_tree_networkx.draw_tree(member_dict, first_member_id, file_name)


def gen_graphyviz_tree():
    first_member_id = 2896 #2594
    if first_member_id == 1:
        file_name = "data/graphyviz_tree.svg"
    else:
        file_name = "data/graphviz_tmp.svg"
    title_name = '右为长，粉红色为女性'
    family_tree_pygraphviz.draw_tree(member_dict, first_member_id, file_name, title_name)


if __name__ == "__main__":
    member_dict = load_members()

    #gen_networkx_tree()
    #gen_graphyviz_tree()
    #gen_org_tree()
    gen_book()
    #gen_circular_tree()
