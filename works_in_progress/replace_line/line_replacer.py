import argparse

class My_Replacer(object):
    def __init__(self, replace_array, arg_option=None):
        self.replace_dict = list(replace_array)
        self._arg_parse(arg_option)
        
        for i in replace_array:
            for j in i:
                print j, i[j]


    def _arg_parse(self, arg_option):
        help_description = '''This is a tool that will switch such and such feature on and off'''
        parser = argparse.ArgumentParser(description=help_description)
        if self.replace_dict[0]['revertline'] != "":
            parser.add_argument('--revert', action='store_true', help='to revert the action')
        self.args = parser.parse_args()
