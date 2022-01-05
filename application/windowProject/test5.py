import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Controls", size = (400, 600))
        self.design()

    def design(self):
        self.panel = wx.Panel(self)        # self : panel변수를 함수 내에서만 아니라, 클래스 내 어디서든지 쓰기 위해 / 해당 함수말고 다른 함수에서도 쓸 계획이 있다.

        wx.StaticText(self.panel, label = "******************다양한 컨트롤(위젯)*******************", pos = (20, 5))

        #### TextCtrl
        wx.StaticText(self.panel, label = "너의 이름은", pos=(20,70))
        self.txtName = wx.TextCtrl(self.panel, value = "이름을 입력하세요", pos = (100, 70))
        self.txtName.Bind(wx.EVT_TEXT, self.onText)           # 문자인 키보드 누를 때
        self.txtName.Bind(wx.EVT_KEY_DOWN, self.onKeydown)     # 키보드 아무거나 누를때마다 동작

        #### Checkbox
        self.ckMarried = wx.CheckBox(self.panel, label = "결혼은?",  pos=(20,120))
        self.ckMarried.Bind(wx.EVT_CHECKBOX, self.onCheck)

        #### RadioBox
        cboData= ["빨강", "초록", "파랑", "노랑"]
        self.rbcolor = wx.RadioBox(self.panel, label = "좋아하는 색상은?", pos=(20,170), choices =cboData)
        self.rbcolor.Bind(wx.EVT_RADIOBOX, self.onRadio)

        #### Combobox
        self.cboColor = wx.ComboBox(self.panel, pos=(20,260), choices =cboData)
        self.cboColor.Bind(wx.EVT_COMBOBOX, self.onCombo)

        #### 결과값 확인
        self.txtShow = wx.TextCtrl(self.panel, pos=(30, 370), size = (320,150), style = wx.TE_MULTILINE |wx.TE_READONLY)  # 출력만


    def onText(self, e):
        #self.txtShow.AppendText("TextCtrl에서 이벤트 발생: {}\n".format(self.txtName.GetValue()))    # GetString : 어떤 문자열이 입력됐는지 알려줌
        self.txtShow.AppendText("TextCtrl에서 이벤트 발생: {}\n".format(e.GetString()))

    def onCheck(self, e):
        self.txtShow.AppendText("CheckBox에서 이벤트 발생: {}\n".format(e.IsChecked()))

    def onRadio(self, e):
        self.txtShow.AppendText("RadioBox에서 이벤트 발생: {}, {}\n".format(e.GetInt(), e.GetString()))

    def onCombo(self, e):
        self.txtShow.AppendText("ComboBox에서 이벤트 발생: {}, {}\n".format(e.GetInt(), e.GetString()))

    def onKeydown(self, e):
        if e.GetKeyCode() == wx.WXK_ESCAPE:          # GetKeyCode : 키보드 누를때마다 키보드의 아스키토드 값
            self.txtName.Clear()                     # esc 누르면 값 지워지게

        e.Skip()     #onKeydown 이벤트가 끝나야 TextCtrl에 걸린 다른 이벤트 실행 하므로

        #self.txtShow.AppendText("TextCtrl에서 이벤트 발생: {}, {}\n".format(e.GetInt(), e.GetString()))


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()