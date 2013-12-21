import wx

class gui(wx.Frame):
  def __init__(self, parent, id):
    wx.Frame.__init__(self, parent, id, 'ThreatEngine', size=(300,500))
    panel=wx.Panel(self)
    
    # button=wx.Button(panel,label='Exit',pos=(130,10),size=(60,60))
    # self.Bind(wx.EVT_BUTTON, self.closebutton, button)
    # self.Bind(wx.EVT_CLOSE, self.closewindow)

    status=self.CreateStatusBar()

    menubar=wx.MenuBar()
    first=wx.Menu()
    second=wx.Menu()
    first.Append(wx.NewId(),"New Window","This is a new window")
    first.Append(wx.NewId(),"Open ...","This will open a new window")
    menubar.Append(first,"File")
    menubar.Append(second,"Edit")
    self.SetMenuBar(menubar)

    # box=wx.MessageDialog(None,'Question?','boxtitle',wx.YES_NO)
    # answer=box.ShowModal()
    # box.Destroy()

    # box=wx.TextEntryDialog(None,"Sup?", "title", "default text")
    # if box.ShowModal()==wx.ID_OK:
    #     answer = box.GetValue()

    # box=wx.SingleChoiceDialog(None,'Whats ur fav?','titttle',['tuna','apples','beef'])
    # if box.ShowModal()==wx.ID_OK:
    #   answer=box.GetStringSelection()

    wx.StaticText(panel, -1, "this is static text",pos=(10,10))

    custom=wx.StaticText(panel,-1,"custom baby",(10,30),(260,-1),wx.ALIGN_CENTER)
    custom.SetForegroundColour('white')
    custom.SetBackgroundColour('Black')

    slider=wx.Slider(panel,-1, 50,1,100,pos=(10,50),size=(250,-1),style=wx.SL_AUTOTICKS | wx.SL_LABELS)
    slider.SetTickFreq(5,1)

    spinner=wx.SpinCtrl(panel,-1,"",(20,120),(90,-1))
    spinner.SetRange(1,100)
    spinner.SetValue(10)

    wx.CheckBox(panel,-1,"uno",(20,160),(160,-1))
    wx.CheckBox(panel,-1,"dos",(20,180),(160,-1))
    wx.CheckBox(panel,-1,"three",(20,200),(160,-1))

    myList=['beef','tuna','coconuts','chicken','ceral']
    container=wx.ListBox(panel,-1,(20,220),(80,50),myList,wx.LB_SINGLE)
    container.SetSelection(3)

    # names = ['tim','brad','hank','roger','phil']
    # modal=wx.SingleChoiceDialog(None, "ur name", "caption/title",names)
    # if modal.ShowModal()==wx.ID_OK:
    #   print "hello %s\n" % modal.GetStringSelection()
    # modal.Destroy()

  def closebutton(self, event):
    self.Close(True)

  def closewindow(self, event):
    self.Destroy()


if __name__ == '__main__':
  app=wx.PySimpleApp()
  frame=gui(parent=None, id=-1)
  frame.Show()
  app.MainLoop()