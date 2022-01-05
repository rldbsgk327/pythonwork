"""
Dialog(대화상자)
------------------
1. 종류
    1) Built-in Dialog
        - Common Dialog(공통 대화상자)

    2) User Define Dialog

2. 실행 방식
    1) Modal (현재 실행중인 Dialog를 종료하기 전까지 Main 윈도우, 다른 기능들을 쓸 수 없다.)
    2) Modaless

"""


import wx
from test3 import LoginFrame

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="대화상자", size = (800, 600))
        self.design()

    def design(self):
        menubar = wx.MenuBar()
        menu = wx.Menu()

        item1 = wx.MenuItem(menu, 100, "MessageDialog", "메세지 대화상자 보이기")     # 아이디 지정시 100 이상 값이 좋다.
        item2 = wx.MenuItem(menu, 101, "ColorDialog", "색상 대화상자 보이기")
        item3 = wx.MenuItem(menu, 102, "FileDialog", "파일 대화상자 보이기")
        item4 = wx.MenuItem(menu, 103, "LoginDialog", "로그인 대화상자 보이기")

        menu.Append(item1)
        menu.Append(item2)
        menu.Append(item3)
        menu.Append(item4)

        menubar.Append(menu, "다이얼로그")
        self.SetMenuBar(menubar)
        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.onMessage, id = 100)
        self.Bind(wx.EVT_MENU, self.onColour, item2)
        self.Bind(wx.EVT_MENU, self.onFile, item3)
        self.Bind(wx.EVT_MENU, self.onLogin, item4)


    def onMessage(self, evt):
        self.SetStatusText("메세지 대화 상자")    # 출력만
        dlg = wx.MessageDialog(self, "오늘 하루도 열심히...", "메세지 박스", wx.OK | wx.ICON_WARNING)   # OK : True or False  / ICON_WARNING : 경고표시 아이콘
        dlg.ShowModal()

    def onColour(self, evt):
        self.SetStatusText("색상 대화 상자")          # 윈도우 밑에 상태표시줄에 출력
        dlg = wx.ColourDialog(self)


        if dlg.ShowModal() == wx.ID_OK:
            color = dlg.GetColourData()
            self.SetStatusText("당신이 선택한 색상은" + str(color.GetColour().Get()))


    def onFile(self, evt):
        self.SetStatusText("파일 대화 상자")
        dlg = wx.FileDialog(self, "파일 불러오기", "c:\\", "", "*.*", style = wx.ID_OPEN)   # 부모, 타이틀, 기본경로, 파일형식, 불러오기/저장하기

        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText("당신이 선택한 파일은" + dlg.GetPaths()[0])


    def onLogin(self, evt):
        self.SetStatusText("로그인 대화 상자")
        dlg = LoginFrame(self)
        dlg.ShowModal()










if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()