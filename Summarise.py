import keyboard, json, os
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FILE = "abbreviations.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save(abbrs):
    json.dump(abbrs, open(FILE, "w"), indent=2)
    keyboard.unhook_all()
    for s, f in abbrs.items():
        keyboard.add_abbreviation(s, f)
    status.configure(text=f"Active: {len(abbrs)}")
    refresh()

def refresh():
    for w in list_frame.winfo_children():
        w.destroy()
    for s, f in load().items():
        row = ctk.CTkFrame(list_frame)
        row.pack(fill="x", pady=2)
        ctk.CTkLabel(row, text=f"{s}  →  {f}", font=("Arial", 14)).pack(side="left", padx=10)
        ctk.CTkButton(row, text="✕", width=30, fg_color="transparent",
                      hover_color="darkred", command=lambda s=s: save({k: v for k, v in load().items() if k != s})
                      ).pack(side="right", padx=5)

def add():
    s, f = entry_s.get(), entry_f.get() + str(" ")
    if s and f:
        save({**load(), s: f})
        entry_s.delete(0, "end")
        entry_f.delete(0, "end")

root = ctk.CTk()
root.title("Abbreviation Expander")
root.geometry("400x600")

ctk.CTkLabel(root, text="Abbreviation Expander", font=("Arial", 24, "bold")).pack(pady=(20, 10))

entry_s = ctk.CTkEntry(root, placeholder_text="Shortcut...")
entry_s.pack(pady=5, padx=20, fill="x")
entry_f = ctk.CTkEntry(root, placeholder_text="Full text...")
entry_f.pack(pady=5, padx=20, fill="x")
ctk.CTkButton(root, text="Add", width=120, command=add).pack(pady=10)

list_frame = ctk.CTkScrollableFrame(root, label_text="Abbreviations")
list_frame.pack(pady=10, padx=20, fill="both", expand=True)

status = ctk.CTkLabel(root, text="Active: 0")
status.pack(pady=(5, 0))
ctk.CTkButton(root, text="Clear All", width=120, fg_color="transparent",
              border_width=1, command=lambda: save({})).pack(pady=(5, 20))

save(load())
root.mainloop()