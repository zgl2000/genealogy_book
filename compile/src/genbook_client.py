from load_members import load_members
import genealogy_book

def gen_book():
    first_member_id = 1 
    file_name = "data/family_book.md"
    genealogy_book.gen_book(member_dict, first_member_id, file_name)

if __name__ == "__main__":
    member_dict = load_members()
    gen_book()
