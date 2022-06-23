from shutil import copyfile
copyfile("crackme.exe", "patched.exe")

with open("patched.exe", "r+b") as exe:
    exe.seek(0x1018)
    exe.write(b"\x70")

    exe.seek(0x101D)
    exe.write(b"\x70")