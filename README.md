# PrettyCopy

Copy code blocks without excess indentation. 
Helpful for gists, pasteys and sending via IM.

When you simply copy code blocks and send them via e.g. Skype, you may see that the formatting is ridiculous. Skype uses tabsize of 8 and without a monospace font it takes about the same size as 16 characters, that makes it mostly unreadable and hard to even look through. This is an alternative copy command for you to bind on different key (`CTRL+SHIFT+C` for example) that will replace tabs with spaces as per your `tabsize` setting in SublimeText and then it will remove all indentation to the minimum indentation in the copied selection.

Example:

			One two three
				One one one

				oneone

Becomes

	One two three
	    One one one
	    oneone

### Installation

##### Using [Package Control](https://sublime.wbond.net/)

+ Simply open up the command palette (`CTRL+SHIFT+P` or `CMD+SHIFT+P`).
+ Find `Package Control: Install Package`.
+ Search for `PrettyCopy`

##### Manual

+ Clone to `Packages/` directory

### Binding

You should add the PrettyCopy shortcut to your user keybindings file:

`{ "keys": ["ctrl+shift+c"], "command": "copy_formatted"}`

### Using

Select a block of text and press your keybinding. Then simply paste anywhere like you usually do.


### Contributing

If you find bugs please post them in the issues section and/or submit pull requests.
