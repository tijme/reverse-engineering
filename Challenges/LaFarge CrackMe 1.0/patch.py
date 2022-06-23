from shutil import copyfile
copyfile("crackme.exe", "patched.exe")

with open("patched.exe", "r+b") as exe:
    exe.seek(0x407)
    exe.write(b"\x74")
    exe.seek(0x428)
    exe.write(b"\x74")