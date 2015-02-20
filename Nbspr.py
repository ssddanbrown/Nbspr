import sublime, sublime_plugin

class NbsprCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel();
		for selection in selections:
			if not selection.empty():
				# Get selected text
				text = self.view.substr(selection)
				# Replace any spaces with &nbsp;
				text = text.replace(' ', '&nbsp;')
				# Replace the selection with new text
				self.view.replace(edit, selection, text)