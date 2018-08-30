from Pages.RibbonPage import RibbonPage


def login():
    RibbonPage.inst().check_addin()
    RibbonPage.inst().nd_frame_login()