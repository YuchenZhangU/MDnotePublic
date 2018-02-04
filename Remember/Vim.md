## Color

`:set colorscheme SCHEMENAME`

`colorscheme SHCEMENAME` in `.vimrc`

Possible color scheme
http://www.vim.org/scripts/script_search_results.php?keywords=&script_type=color+scheme&order_by=creation_date&direction=descending&search=search


## Tips

10 Vim tricks you should know
Here are 10 Vim tips that I think you should know about.

- The super star and sharp

In normal mode you can use \* and # to search for a word under the cursor.
\* searches forward for the word, while # searches backwards.

- Simple completion in any text

Hit CTRL-N once in insert mode and it will try to complete the current word with the first match in the current file. CTRL-P does the same thing but searches backwards.

- The .

Type . in normal mode to repeat last change, this is super useful when doing receptive changes.

- The % key

You can use the % key to jump to a matching opening or closing parenthesis, square bracket or a curly brace. Insanely useful when programming.

- Indent using == and =

When working with source code it is very nice to work with indented code.

To indent the current line issue == in normal mode. Use Shift-V to go into visual mode, select a couple of lines and do = to indent them.

- Undo and redo

You can use u to undo the last change. CTRL-R redoes a change that has been undone. U returns the current line to its original state.

You can use g- or g+ to go between text-states. To go to a text state 1 minute earlier, you can use:

:eariler 1m
Incremental search
There is a really neat search-option. When you search (for example, using /), the matches will be shown while you type. To turn this option on, type following:

- set incsearch

Highlighting all the search pattern matches
To highlight all the search pattern matches in a file set the following option:

:set hlsearch
To disable the highlighting temporarily, use:

:nohlsearch
Turn off auto-indent when pasting text
Type following command:

:set pastetoggle=<F3>
Now you can use <F3> to toggle between paste mode (and no paste mode).

When in paste-mode auto indent will be turned off. This is very useful when pasting text that’s already indented.

- Don’t repeat yourself — record your actions

To start recording, press qa in the normal mode, this will save your recording in the a register. Now do your actions. After you are done, stop recording by issuing q in normal mode.

To replay your recording issue @a in normal mode.

This is really useful when doing some complex repeating tasks.