import sublime, sublime_plugin

class NbsprCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel();
		# Get total count of spaces to decide replacement order.
		nbspCount = 0
		spaceCount = 0
		for selection in selections:
			nbspCount += self.view.substr(selection).count('&nbsp;')
			spaceCount += self.view.substr(selection).count(' ')
			
		# Perform replacements
		if nbspCount == 0:
			self.replaceSelections(edit, selections, ' ', '&nbsp;')
		elif spaceCount == 0:
			self.replaceSelections(edit, selections, '&nbsp;', ' ')
		elif nbspCount < spaceCount:
			self.replaceSelections(edit, selections, '&nbsp;', ' ')
		else:
			self.replaceSelections(edit, selections, ' ', '&nbsp;')

	def replaceSelections(self, edit, selections, search, replacement):
		for selection in selections:
			if not selection.empty():
				# Get selected text
				text = self.view.substr(selection)
				# Replace any spaces with &nbsp;
				text = text.replace(search, replacement)
				# Replace the selection with new text
				self.view.replace(edit, selection, text)