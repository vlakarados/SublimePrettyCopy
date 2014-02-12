import sublime, sublime_plugin, textwrap

class Copy_formattedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("-- -- -- -- -- -- -- -- --")
        selected = self.view.substr(self.view.sel()[0])
        selected = self.tabs_to_spaces(selected, self.view.settings().get('tab_size'))
        listing = selected.split('\n')

        # remove empty lines
        # usually the last line or the first
        # if user selects a block and places the cursor above or below it
        for line in listing:
            if len(line) == 0:
                listing.remove(line)

        minindent = self.min_indent_in_list(listing)
        print("Minimum indent is " + str(minindent))
        
        # remove minindent from the beginning of all strings
        stripped = self.remove_indents(listing, minindent)
        multiline = '\n'.join(stripped)
        sublime.set_clipboard(multiline)
        sublime.status_message('Copying with pretty format')

    def min_indent(self, s):
        return 0 if s.isspace() else len(s) - len(s.lstrip())

    def tabs_to_spaces(self, s, tabsize=4):
        return s.expandtabs(tabsize)

    def min_indent_in_list(self, l):
        min = None
        for line in l:
            if min is None or min > self.min_indent(line):
                min = self.min_indent(line)
        return min

    def remove_indents(self, l, n):
        new_lines = []
        for line in l:
            new_lines.append(line[n:])
        return new_lines


