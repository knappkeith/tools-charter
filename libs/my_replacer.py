import argparse
import pprint
import os

class My_Replacer(object):
    def __init__(self, replace_array, arg_option={}):
        self.replace_dict = list(replace_array)
        self._arg_parse(arg_option)


    def _arg_parse(self, arg_option):
        try:
            help_description = arg_option['description']
        except KeyError:
            try:
                help_description = arg_option['file']
            except KeyError:
                help_description = '''This is a tool that will replace a line of code in a file.'''
        parser = argparse.ArgumentParser(description=help_description)
        if "".join([self.replace_dict[x]['revert_line'] for x in range(len(self.replace_dict))]) is not "":
            parser.add_argument('--revert', action='store_true', help='to revert the action')
        parser.add_argument('--print', dest='actions', action='store_const',
                   const=self._print_dict, default=self._run_it,
                   help='Print out replace Dictionary')
        self.args = parser.parse_args()
        self.args.actions()


    def _print_dict(self):
        pprint.pprint(self.replace_dict)


    def _run_it(self):
        for change in self.replace_dict:
            fname = self._get_file_name(change['file_path'])
            cname = self._create_copy_name(fname)
            if self.args.revert:
                print_line = "Reverting in %s"
                try:
                    nline = change['revert_line']
                except KeyError:
                    nline = ""
            else:
                print_line = "Replacing in %s"
                nline = change['new_line']
            if nline != "":
                read_file = open(fname)
                write_file = open(cname, 'w')
                for line in read_file:
                    if change['search_line'] in line:
                        print print_line % fname
                        write_file.write(nline + '\n')
                    else:
                        write_file.write(line)
                read_file.close()
                write_file.close()
                os.remove(fname)
                os.rename(cname, fname)
            else:
                print "Skipping Revert because no revert sting for %s" % fname


    def _get_file_name(self, fname):
        fname = str(fname)
        if not self._check_file(fname):
            root = self._get_root_dir()
            fname = os.path.join(root, fname)
            if not self._check_file(fname):
                raise NameError('Unable to find replace file: %s' % fname)
        return fname


    def _create_copy_name(self, og_path):
        og_dir, og_file = os.path.split(og_path)
        og_name, og_ext = os.path.splitext(og_file)
        count = 1
        while os.path.exists(os.path.join(og_dir, '%s-%s%s' % (og_name, count, og_ext))):
            count += 1
        return os.path.join(og_dir, '%s-%s%s' % (og_name, count, og_ext))


    def _get_root_dir(self):
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../"))
        root_dir = os.path.join(root_dir, "skyuisp")
        if os.path.exists(root_dir):
            return root_dir
        else:
            raise NameError("Cannot find Root Source Code Directory!")


    def _check_file(self, fname):
        return os.path.exists(os.path.expanduser(fname))
