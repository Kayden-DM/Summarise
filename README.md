## Abbreviation Expander
A desktop text expander built with CustomTkinter and the keyboard module. It lets the user define shortcut abbreviations that automatically expand into full text anywhere on the system.

## Features
Add Abbreviations — Enter a shortcut and its full text, then click Add to save and activate it.

Global Expansion — Uses keyboard.add_abbreviation() so shortcuts expand system-wide, not just inside the app.

Persistent Storage — Abbreviations are saved to abbreviations.json and reloaded on startup.

Live List — A scrollable list shows every saved shortcut and its expansion.

Remove Entries — Each row has a ✕ button to delete that abbreviation.

Clear All — Removes every abbreviation and saves the empty list.

Active Counter — Displays how many abbreviations are currently active.

Dark Mode UI — CustomTkinter dark appearance with a blue accent theme.

## Technologies Used
text
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Desktop GUI |
| `keyboard` | Registers global abbreviations |
| `json` | Saves and loads abbreviations |
| `os.path.exists()` | Checks whether the save file exists |
| `dict` | Stores shortcuts mapped to full text |
| `dict comprehension` | Filters out a removed shortcut |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install the required packages by running pip install customtkinter keyboard.

Save the code as abbreviation_expander.py.

Open a terminal in the folder containing the file.

Run python abbreviation_expander.py (on some systems you may need to run it as administrator for the keyboard hook to work).

Type a shortcut and its full text, click Add, then use the shortcut in any text field to expand it.

## Improvements
Close files properly — load() and save() call open() without a with block, so file handles are left open; wrapping them in with open(...) as f: ensures they're closed correctly.

Fix the trailing space logic — entry_f.get() + str(" ") always appends a space even if the full text already ends with one, which can produce double spaces; checking with if not f.endswith(" ") before appending would prevent that.

