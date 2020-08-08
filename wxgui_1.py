import wx

def xbc(event):
    print ("I like you are learning")


a = wx.App()

w = wx.Frame(None, title="Who is Online?",
             size=(200, 100))
button = wx.Button(w, label="Send Online Notice")
button.Bind(wx.EVT_BUTTON, xbc)

w.Show()
a.MainLoop()
