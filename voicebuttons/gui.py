# from https://stackoverflow.TRAY_ICONcom/questions/46417383/python-3-and-wx-to-create-system-tray-icon
import wx.adv
import sys


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        self.TRAY_TOOLTIP = 'VoiceButtons'
        self.TRAY_ICON = './res/icon.png'
    

        super(TaskBarIcon, self).__init__()
        icon = wx.Icon(wx.Bitmap(self.TRAY_ICON, wx.BITMAP_TYPE_ANY))

        self.SetIcon(icon,self.TRAY_TOOLTIP)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
     
    def CreatePopupMenu(self):
        menu = wx.Menu()
        #create_menu_item(menu, 'Say Hello', self.on_hello)
        #menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, self.TRAY_TOOLTIP)

    def on_left_down(self, event):
        pass

    #def on_hello(self, event):
    #    print ('Hello, world!')

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()
        sys.exit(0)
    


class VoiceButtonApp(wx.App):

    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

    def do_the_work(self, value):

        # Create an event loop and make it active.  If you are
        # only going to temporarily have a nested event loop then
        # you should get a reference to the old one and set it as
        # the active event loop when you are done with this one...
        evtloop = wx.GUIEventLoop()
        old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)

        # This outer loop determines when to exit the application,
        # for this example we let the main frame reset this flag
        # when it closes.
        #while self.keepGoing:
            # At this point in the outer loop you could do
            # whatever you implemented your own MainLoop for.  It
            # should be quick and non-blocking, otherwise your GUI
            # will freeze.  

            # call_your_code_here()


            # This inner loop will process any GUI events
            # until there are no more waiting.
        while evtloop.Pending():
            evtloop.Dispatch()

            # Send idle events to idle handlers.  You may want to
            # throttle this back a bit somehow so there is not too
            # much CPU time spent in the idle handlers.  For this
            # example, I'll just snooze a little...
        evtloop.ProcessIdle()

        wx.EventLoop.SetActive(old)


def main():
    app = VoiceButtonApp(False)
    app.MainLoop()


if __name__ == '__main__':
    main()