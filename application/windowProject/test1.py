import wx

app = wx.App()
frame = wx.Frame(None, title = "처음 만드는 윈도우")        # None은 부모의 주소
frame.Show(True)
app.MainLoop()


# 처음 실행하는 파일이 main 파일
# 3대 요소 : 컨트롤(이벤트 소스 /= 파이썬에선 위젯), 레이아웃, 이벤트