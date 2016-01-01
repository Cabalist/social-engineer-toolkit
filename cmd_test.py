# coding=utf-8
import cmd


class SubCmd(cmd.Cmd, object):
    def __init__(self, prompt, *args, **kwargs):
        super(SubCmd, self).__init__(*args, **kwargs)
        self.prompt = "{}:{}>".format(prompt[:-1], self.__class__.__name__)

    def do_exit(self, args):
        return True

    do_EOF = do_exit


class AutoLaunch(cmd.Cmd, object):
    def __init__(self, *args, **kwargs):
        super(AutoLaunch, self).__init__(*args, **kwargs)
        self.intro = "Welcome to SET y'all!"
        self.prompt = "SET>"

    def do_a(self, args):
        """Option A allows you to do something and another thing."""
        print("You picked option 1.")
        OptionA(self.prompt).cmdloop()

    def do_b(self, args):
        print("Option 2 is now your choice.")
        OptionB(self.prompt).cmdloop()

    def do_exit(self, args):
        print("Exiting gracefully")
        return True

    do_EOF = do_exit


class OptionA(SubCmd):
    def __init__(self, *args, **kwargs):
        super(OptionA, self).__init__(*args, **kwargs)
        self.intro = "Welcome To Option A\nType `exit` to get back to the last menu..."

    def do_thing(self, args):
        print("I did the thing")

    def do_other_thing(self, args):
        print("I did the OTHER thing")

    def do_godeep(self, args):
        print("Going DEEP")
        OptionDeep(self.prompt).cmdloop()


class OptionB(SubCmd):
    def __init__(self, *args, **kwargs):
        super(OptionB, self).__init__(*args, **kwargs)

        self.intro = "Welcome To Option B\nType `exit` to get back to the last menu..."

    def do_thing(self, args):
        print("I did the B thing")

    def do_other_thing(self, args):
        print("I did the OTHER B thing")


class OptionDeep(cmd.Cmd, object):
    def __init__(self, *args, **kwargs):
        super(OptionDeep, self).__init__(*args, **kwargs)
        self.intro = "Welcome To Option Deep\nType `exit` to get back to the last menu..."

    def do_thing(self, args):
        print("I did the deep thing")

    def do_other_thing(self, args):
        print("I did the OTHER DEEP thing")


if __name__ == "__main__":
    try:
        AutoLaunch().cmdloop()
    except KeyboardInterrupt:
        print("Welp that is enough of that.")
    finally:
        print()
        print("All my cleanup!")
