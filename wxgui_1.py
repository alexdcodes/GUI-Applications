import wx

def xbc(event):
    print ("I like you are learning")


a = wx.App()

w = wx.Frame(None, title="Who is Scheduled?",
             size=(200, 100))
button = wx.Button(w, label="Send Schedule")
button.Bind(wx.EVT_BUTTON, xbc)

w.Show()
a.MainLoop()
