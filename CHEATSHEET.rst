My Cheatsheet
=============

Assembly x86
------------

**ES:EDI EDI DI** (destination index register)

Used for string, memory array copying and setting and for far pointer addressing with ES.

**DS:ESI EDI SI** (source index register)

Used for string and memory array copying.

**SS:EBP EBP BP** (stack Base pointer register)

Holds the base address of the stack.
                
**SS:ESP ESP SP** (stack pointer register)

Holds the top address of the stack.

**CS:EIP EIP IP** (index pointer)

Holds the offset of the next instruction (read only). 


IDA PRO
-------

**Shortcuts**

.. raw:: html

    <kbd>Esc</kbd> Previous window.
    <br>
    <kbd>Ctrl</kbd>+<kdb>Enter</kdb> Next window.
    <br>
    <kbd>Shift</kbd>+<kbd>F12</kbd> Show strings window.
    <br>
    <kbd>Shift</kbd>+<kbd>F12</kbd> Show strings window.
    <br>
    <kbd>Alt</kbd>+<kbd>T</kbd> Full text search.
    <br>
    <kbd>Spacebar</kbd> Switch between Hex & Graph view.
    <br>
    <kbd>;</kbd> Enter comment.
    <br><br>
    
**Miscellaneous**

* Solarized dark color scheme (`link <https://github.com/gynophage/solarized_ida>`_)


OllyDbg
-------

**Shortcuts**

.. raw:: html

    <kbd>F2</kbd> Toggle a breakpoint.
    <br>
    <kbd>Ctrl</kbd>+<kbd>B</kbd> Binary string search.
    <br>
    <kbd>Ctrl</kbd>+<kbd>R</kbd> Find reference to selected block.
    <br><br>
