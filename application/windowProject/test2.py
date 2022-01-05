import wx

class MemoFrame(wx.Frame):       ## wx.Frame을 상속받는다.
    def __init__(self):
        super().__init__(None, title="메모장 프로그램", size = (800, 600))
        self.design()

    def design(self):
        # 메뉴: 고정식 메뉴(pull down), 이동식 메뉴(pop up, 마우스 우클릭)
        # MenuBar, Menu, MenuItem
        menubar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuEdit = wx.Menu()

        mnuFile_new = wx.MenuItem(mnuFile, wx.ID_NEW, "New", "New Document")     # ID_NEW 아이디
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, "Open", "파일 열기")       # 첫번째 인자: 부모 / 붙여서 사용한다.
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, "Exit", "프로그램 종료")

        mnuFile.Append(mnuFile_new)
        mnuFile.Append(mnuFile_open)
        mnuFile.Append(mnuFile_exit)

        menubar.Append(mnuFile, "파일")
        menubar.Append(mnuEdit, "편집")

        self.SetMenuBar(menubar)

        self.txtArea = wx.TextCtrl(self, style = wx.TE_MULTILINE)

        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.onNew, mnuFile_new)       # 이벤트 소스
        self.Bind(wx.EVT_MENU, self.onExit, mnuFile_exit)
        self.Bind(wx.EVT_MENU, self.onOpen, mnuFile_open)



        #self.Move(100, 100)         창 위치
        self.Center()

    def onNew(self, evt):          # 이벤트 핸들러 (self외, 인자 하나 더 있어야 함) : 이름앞에 on은 암묵적 합의
        self.txtArea.SetLabelText("새 문서를 선택하였습니다.")

    def onExit(self, evt):
        self.Close(True)

    def onOpen(self, evt):
        #f = open("C:\\datastudy\\pythonwork\\ai\\data\\manhattan.csv")

        dlg = wx.FileDialog(self, "파일 불러오기", "c:\\", "", "*.*", style = wx.ID_OPEN)   # 부모, 타이틀, 기본경로, 파일형식, 불러오기/저장하기

        if dlg.ShowModal() == wx.ID_OK:
            selectedFile =  dlg.GetPaths()[0]

        f = open(selectedFile, "r")
        data = f.read()
        self.txtArea.SetLabelText(data)
        f.close()

        # data = f.read()
        # self.txtArea.SetLabelText(data)
        # f.close()

if __name__ == "__main__":    # # 이 파일이 메인으로 실행될 때만 아래 코드(윈도우 뜨게) 실행함
    app = wx.App()
    frame = MemoFrame()
    frame.Show(True)
    app.MainLoop()
