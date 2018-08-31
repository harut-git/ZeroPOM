from Pages.AddinsPage import AddinsPage


def login():
    AddinsPage().inst().addin_login()
    AddinsPage().inst().nd_frame_login()