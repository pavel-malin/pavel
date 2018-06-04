import sys
import signal
from  Xlib.display import Display
from Xlib import X
from Xlib.ext import record
from Xlib.protocol import rq
import threading

globs = {'HotkeyCaught': False}

# todo: взять функции, вычисляющие keysym, из pyxhook
keysym_map = {32: "SPACE", 39: "'", 44:",", 45: "-", 46: ".", 47: "/", 48: "0", 49: "1", 50: "2", 51: "3", 52: "4",
              53: "5", 54: "6", 55: "7", 56: "8", 57: "9", 59: ";", 61: "=", 91: "[", 92: "\\", 93: "]", 96: "`",
              97: "a", 98: "b", 99: "c", 100: "d", 101: "e", 102: "f", 103: "g", 104: "h", 105: "i", 106: "j", 107: "k",
              108: "l", 109: "m", 110: "n", 111: "o", 112: "p", 113: "q", 114: "r", 115: "s", 116: "t", 117: "u",
              118: "v", 119: "w", 120: "x", 121: "y", 122: "z", 65293: "ENTER", 65307: "ESC", 65360: "HOME",
              65361: "ARROW_LEFT", 65362: "ARROW_UP", 65363: "ARROW_RIGHT", 65505: "L_SHIFT", 65506: "R_SHIFT",
              65507: "L_CTRL", 65508: "R_CTRL", 65513: "L_ALT", 65514: "R_ALT", 65515: "SUPER_KEY", 65288: "BACKSPACE",
              65364: "ARROW_DOWN", 65365: "PG_UP", 65366: "PG_DOWN", 65367: "END", 65377: "PRTSCRN", 65535: "DELETE",
              65383: "PRINT?", 65509: "CAPS_LOCK", 65289: "TAB", 65470: "F1", 65471: "F2", 65472: "F3", 65473: "F4",
              65474: "F5", 65475: "F6", 65476: "F7", 65477: "F8", 65478: "F9", 65479: "F10", 65480: "F11", 65481: "F12"}



def catch_control_c(*args):
    pass


signal.signal(signal.SIGINT, catch_control_c) # do not quit when Control-c is pressed


def toggle_hotkey(SetBool=True):
    globs['HotkeyCaught'] = SetBool







# Определить нажатие горячих клавиш глобально в системе


class KeyListener(threading.Thread):
    """
    Использование:
    keylistener  = KeyListener()
    keylistener.addKeyListener("L_CTRL+L_SHIFT+y", callable)
    присвоить все возможности комбинации, нажатия может быть иной

    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.finished = threading.Event()
        self.contextEvenMask = [X.KeyPress, X.MotionNotify]
        # Give these some initial values
        # Hook to our display.
        self.local_dpy = Display()
        self.record_dpy = Display()
        self.pressed = []
        self.listeners = {}


    # ------------------------------------------------------------------------------------------------------------------
    def processevents(self, reply):
        if reply.category != record.FromServer:
            return
        if reply.client_swapped:
            print("* received swapped protocol data, cowardly ignored")
            return
        # Добавил str, иначе получаем ошибку
        if not len(str(reply.data)) or ord(str(reply.data[0])) < 2:
            # not an event
            return
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(data, self.record_dpy.display, None, None)
            keycode = event.detail
            keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
            if keysym in keysym_map:
                character = keysym_to_character(keysym)
                if event.type == X.KeyPress:
                    keylistener.press(character)
                elif event.type == X.KeyRelease:
                    keylistener.release(character)
                # self.KeyUp(hookevent)

     #print "processing events...", event.type
    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        # Check if the extension is present
        if not self.record_dpy.has_extension("RECORD"):
            print("RECORD extension not found")
            sys.exit(1)
        r = self.record_dpy.record_get_version(0, 0)
        print("RECORD extension version %d.%d" % (r.major_version, r.minor_version))
        # Create a recoding context; we only want key event
        self.ctx = self.record_dpy.record_create_context(0, [record.AllClients], [{ 'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': tuple(self.contextEventMask),  # (X.KeyPress, X.ButtonPress),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
                                                                                    }])

        # Enable the context; this only returns after a call to record_disable_context,
        # while calling the callback function in the meantime
        self.record_dpy.record_enable_context(self.ctx, self.processevents)
        # Finally free the context
        self.record_dpy.record_free_context(self.ctx)

    # print('Starting hotkey wotch (thread).')
    # ------------------------------------------------------------------------------------------------------------------
    def cancel(self):
        self.finished.set()
        self.local_dpy.record_context(self.ctx)
        self.local_dpy.flush()

    # print('Ending hotkey watch (theard).')
    # ------------------------------------------------------------------------------------------------------------------
    def press(self, character):
        if len(self.pressed) == 3:
            self.pressed = []
            if character == 'L_CTRL' or character == 'R_CTRL':
                if len(self.pressed) > 0:
                    self.pressed = []
                    self.pressed.append(character)
                elif character == 'c':
                    if len(self.pressed) > 0:
                        if self.pressed[0] == 'L_CTRL' or self.pressed[0] == 'R_CTRL':
                            action = self.listeners.get(tuple(self.pressed), False)
                            # print('Current action:', str(tuple(self.pressed))
                            if action:
                                action()

    # ------------------------------------------------------------------------------------------------------------------
    def release(self, character):
        """

        must be called whenever a key release event has occurred.

        """
        # Не засчитывает отпущенный Control
        # Кириллическую 'C' распознает как латинскую
        if character != 'c':
            self.pressed = []

    # ------------------------------------------------------------------------------------------------------------------
    def addKeyListener(self, hotkeys, callable):
        keys = tuple(hotkeys.split("+"))
        print("Added new keylistener for :", str(keys))
        self.listeners[keys] = callable

    # ------------------------------------------------------------------------------------------------------------------
    def result(self):
        if globs['HotkeyCaught']:
            print('Control-c-c detected!')
            globs['HotkeyCaught'] = False
            return True
        else:
            return False


keylistener = KeyListener()
keylistener.addKeyListener("L_CTRL+c+c", toggle_hotkey)



# Определить название клавиши по ее коду
# Переменная keysym_to_chacter(sym):
def keysym_to_character(sym):
    if sym in keysym_map:
        return keysym_map[sym]
    else:
        return sym

def wait_example():
    from time import sleep
    keylistener.start()
    while not keylistener.result():
        sleep(5)
    keylistener.cancel()


if __name__ == '__main__':
    wait_example()



