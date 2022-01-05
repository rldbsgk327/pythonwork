# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(526, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"거래처명 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer10.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_txtName = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_txtName, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"전화 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer10.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_txtTel = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_txtTel, 0, wx.ALL, 5)

        self.m_btnInsert = wx.Button(self.m_panel5, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_btnInsert, 0, wx.ALL, 5)

        self.m_panel5.SetSizer(bSizer10)
        self.m_panel5.Layout()
        bSizer10.Fit(self.m_panel5)
        bSizer9.Add(self.m_panel5, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_lstView = wx.ListCtrl(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer12.Add(self.m_lstView, 1, wx.ALL | wx.EXPAND, 5)

        # ListCtrl의 필드명 작성
        self.m_lstView.InsertColumn(0, "거래처 이름", width=200)
        self.m_lstView.InsertColumn(1, "전화번호", width=200)

        self.m_panel6.SetSizer(bSizer12)
        self.m_panel6.Layout()
        bSizer12.Fit(self.m_panel6)
        bSizer9.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"거래처 수 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer11.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_lblCount = wx.StaticText(self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_lblCount.Wrap(-1)
        bSizer11.Add(self.m_lblCount, 0, wx.ALL, 5)

        self.m_panel7.SetSizer(bSizer11)
        self.m_panel7.Layout()
        bSizer11.Fit(self.m_panel7)
        bSizer9.Add(self.m_panel7, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_btnInsert.Bind(wx.EVT_BUTTON, self.onInsert)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onInsert(self, event):
        name = self.m_txtName.GetValue()
        tel = self.m_txtTel.GetValue()

        i = self.m_lstView.InsertItem(1000, 0)     # 리스트에 입력가능한 데이터 갯수 1000개, 시작위치 0
        self.m_lstView.SetItem(i, 0, name)
        self.m_lstView.SetItem(i, 1, tel)

        self.m_lblCount.SetLabelText(str(self.m_lstView.GetItemCount()))

        self.m_txtName.SetValue("")   # 버튼 누르면 써져있던거 지우기
        self.m_txtTel.SetValue("")

        self.m_txtName.SetFocus()   # 버튼 누르면 커서 txtName에 옮기기

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()