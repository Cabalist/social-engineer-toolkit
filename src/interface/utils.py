# coding=utf-8
import cmd



class SubCmd(cmd.Cmd, object):
    def __init__(self, prompt, *args, **kwargs):
        super(SubCmd, self).__init__(*args, **kwargs)
        self.prompt = "{}:{}>".format(prompt[:-1], self.__class__.__name__)

    def do_exit(self, args):
        return True

    do_EOF = do_exit
    do_99 = do_exit


class YesNoCmd(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(YesNoCmd, self).__init__(prompt, *args, **kwargs)

    def onecmd(self, line):
        valid = {"yes": True, "y": True, "ye": True,
                 "no": False, "n": False}

        if line.lower() in valid:
            line = line.lower()
            if valid[line]:
                line = "yes"
            else:
                line = "no"

        return super(YesNoCmd, self).onecmd(line)

    def do_exit(self, args):
        print("You must make a choice: yes or no")

    do_EOF = do_exit
