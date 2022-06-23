from shutil import copyfile
copyfile("original_sublime_text.exe", "cracked_sublime_text.exe")

with open("cracked_sublime_text.exe", "r+b") as exe:
    exe.seek(0x134A09)
    exe.write(b"\xE9\x83\x00")
