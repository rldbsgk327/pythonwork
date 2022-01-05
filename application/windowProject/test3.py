import wx

#class LoginFrame(wx.Frame):
class LoginFrame(wx.Dialog):
    def __init__(self, parent):              # 모듈로 사용할 경우(test4에서 사용), 인자 넣어야 함 : parent
        super().__init__(parent, title="로그인", size = (300, 200))    # 모듈로 사용하지 않을 경우, parent -> None
        self.design()

    def design(self):
        self.panel = wx.Panel(self)       # 패널 붙히니 색 달라짐

        wx.StaticText(self.panel, label = "ID: ", pos = (10, 5))    # StaticText: 출력만, 입력x
        wx.StaticText(self.panel, label="Pass: ", pos=(10, 40))

        self.m_id = wx.TextCtrl(self.panel, pos = (60, 5), size = (200, -1))           # 패널에 텍스트 박스 붙힌다 /  높이 기본값: -1
        self.m_pw = wx.TextCtrl(self.panel, pos = (60, 40))

        btn1 = wx.Button(self.panel, label = "로그인", pos = (10, 100))
        btn2 = wx.ToggleButton(self.panel, label = "토글 버튼", pos = (100, 100))
        btn3 = wx.Button(self.panel, label = "종료", pos = (190, 100))

        # btn1.Bind(wx.EVT_BUTTON, self.onBtn1)
        # btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onBtn2)
        # btn3.Bind(wx.EVT_BUTTON, self.onBtn3)                # 첫 인자: 이벤트가 발생하는 위치 -> 버튼

        # 한 함수에 다 넣는 방법
        btn1.Bind(wx.EVT_BUTTON, self.onHandler)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onHandler)
        btn3.Bind(wx.EVT_BUTTON, self.onHandler)

        btn1.id, btn2.id, btn3.id = 1, 2, 3                 # 버튼마다 id 부여

    def onHandler(self, evt):
        #print(evt.GetEventObject().id)                      # 버튼 누를때마다, id가 콘솔에 출력
        if evt.GetEventObject().id == 1:
            id = self.m_id.GetValue()
            pw = self.m_pw.GetValue()

            if id =="tiger" and pw== "1111" :
                msg = "로그인이 되었습니다."
            else:
                msg = "로그인이 거부되었습니다."

            wx.MessageDialog(self, msg, "로그인", wx.OK).ShowModal()
        elif evt.GetEventObject().id == 2:
            if evt.GetEventObject().GetValue():
                self.panel.SetBackgroundColour((wx.Colour(255, 0, 0)))
                self.panel.Refresh()         # 갱신
            else:
                self.panel.SetBackgroundColour((wx.Colour(255, 255, 255)))
                self.panel.Refresh()
        else:
            self.Close(True)




    # 따로따로 한 것
    # def onBtn1(self, evt):
    #     id = self.m_id.GetValue()
    #     pw = self.m_pw.GetValue()
    #
    #     if id =="tiger" and pw== "1111" :
    #         msg = "로그인이 되었습니다."
    #     else:
    #         msg = "로그인이 거부되었습니다."
    #
    #     wx.MessageDialog(self, msg, "로그인", wx.OK).ShowModal()      # 대화창 띄우기
    #
    # def onBtn2(self, evt):
    #     #print(evt.GetEventObject())        # 이벤트가 어디서 발생했는지 주소 알려줌 -> 토글버튼
    #     #print(evt.GetEventObject().GetValue())
    #     if evt.GetEventObject().GetValue():
    #         self.panel.SetBackgroundColour((wx.Colour(255, 0, 0)))
    #         self.panel.Refresh()         # 갱신
    #     else:
    #         self.panel.SetBackgroundColour((wx.Colour(255, 255, 255)))
    #         self.panel.Refresh()
    #
    # def onBtn3(self, evt):
    #     self.Close(True)

if __name__ == "__main__":
    app = wx.App()
    frame = LoginFrame(None)       # 위 클래스를 모듈로 쓸 경우, 인자 None, 아닐 땐 비워놓기
    frame.Show(True)
    app.MainLoop()