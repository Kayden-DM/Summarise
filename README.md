Abbreviation Expander
A GUI Python app built with CustomTkinter and the keyboard library that registers global text abbreviations — type a shortcut anywhere on your system and it expands into the full text you defined.

Concepts Used
keyboard.add_abbreviation() — registers a global hotstring that fires system-wide, replacing the shortcut with the full text as you type.

keyboard.unhook_all() — clears all previously registered hooks before re-registering, so the running state always matches the saved data.

JSON Persistence — load() and save() read and write abbreviations.json, restoring abbreviations on startup.

Features
Global Expansion — shortcuts work in any application, not just inside the app window.

Add & Remove Entries — enter a shortcut and full text to add; click ✕ next to any row to delete it.

Live Status — the status label shows how many abbreviations are currently active.

Clear All — wipes every entry and unregisters all hooks in one action.

Dark Mode UI — CustomTkinter interface with a blue accent theme.

Improvements
Handle Invalid JSON on Load — json.load will crash the app if abbreviations.json is corrupted or empty; wrap it in a try/except and fall back to {}.

Close the File Handles — load() and save() open files without closing them; use a with block to avoid leaving handles open.

Validate the Shortcut — add() accepts any string, including spaces or empty-adjacent values; strip input and reject shortcuts containing whitespace, which keyboard.add_abbreviation can't reliably match.

Clean Shutdown — call keyboard.unhook_all() on window close (root.protocol("WM_DELETE_WINDOW", ...)) so hooks don't linger after the app exits.
