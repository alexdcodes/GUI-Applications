import wx

a = wx.App()
w = wx.Frame(None, title="Note Editor", size=(410, 335))
w.Show()

lB = wx.Button(w, label="Open",
               pos=(225, 5), size=(80,25))

sB = wx.Button(w, label="Save",
               pos=(315, 5), size=(80, 25))

fn = wx.TextCtrl(w, pos=(5, 35), size=(210, 25))

c = wx.TextCtrl(w, pos=(5, 35), size=(390, 260),
                style=wx.TE_MULTILINE | wx.HSCROLL)
a.MainLoop()
