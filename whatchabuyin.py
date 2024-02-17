import __main__
class hooked:
    def __init__():
        return 
    def __init_subclass__(self):
        lambda: __main__.repl_hooks.my_displayhook(self, self)
        return 
class try_hook(hooked):
    def __init__(self):
        (lambda: super(try_hook, self).__init__())()
    def __init_subclass__(self):
        (lambda: super(try_hook, self).__init__())()
class cast(try_hook):
    def __init__(self):
        (lambda: super(cast, self).__init__())()
try:
    if __name__ == "__main__":
        reel = try_hook()
        pull = cast()
    else:
        hooked
except:
    print("wiggle")
    
