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
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"이름:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer6.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_txtName = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_txtName, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer6)
        self.m_panel2.Layout()
        bSizer6.Fit(self.m_panel2)
        bSizer3.Add(self.m_panel2, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"나이:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer7.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_txtAge = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_txtAge, 0, wx.ALL, 5)

        self.m_btnOk = wx.Button(self.m_panel3, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_btnOk, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer7)
        self.m_panel3.Layout()
        bSizer7.Fit(self.m_panel3)
        bSizer3.Add(self.m_panel3, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staResult = wx.StaticText(self.m_panel4, wx.ID_ANY, u"결과 보기", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staResult.Wrap(-1)
        bSizer8.Add(self.m_staResult, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer8)
        self.m_panel4.Layout()
        bSizer8.Fit(self.m_panel4)
        bSizer3.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_btnOk.Bind(wx.EVT_BUTTON, self.onOk)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onOk(self, event):
        name = self.m_txtName.GetValue()
        age = self.m_txtAge.GetValue()

        self.m_staResult.SetLabel("결과 보기: "+name+":"+age)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()