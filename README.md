peda-heap
=========
## Description
  This is some commands that I was added to peda when playing CTF.
  
  Thanks to [longld](https://github.com/longld) very much for a great template! [PEDA](https://github.com/longld/peda)

## Commands:

### [heap]
  * `heap set_mainarena [new_addr]` -- set main_arena = newvalue
  * `heap all` -- print heap info (mmap + sbrk)
  * `heap freed [main_arena]` -- print freed chunks  (fastbinY + bins)
  * `heap fastbin [main_arena]` -- print freed chunks(fastbinY)
  * `heap bins [main_arena]` -- print freed chunks (bins)
  * `heap trace` -- print (arg + return_value) of malloc,free,realloc
  * `heap checkfree address` -- try free chunk at address and print some info
  * `heap debug + heap restore` -- try restore heap state before it was overlapped 
  
### [IDA]
  * `xdebug` -- execute commands in file peda-cmd.
  * `xstruct struct_name address` -- try parsing info follow structs(Local Types) was reversed by IDA,structs was imported by peda from file **peda-structs**
  
  > **Use:** In IDA shift+F1->LocalTypes Window -> Edit a struct -> copy struct.Create file **peda-structs** and parse content in this       file.Struct format like:
    ```
    struct msg
    {
      __int64 post_id;
      _QWORD *sender;
      char msg[128];
      post *next;
    };
    ```
    
### [PIE]
  * `bp address` -- breakpoint an address with PIE flag
  * `xp address` -- exam an address with PIE flag

## Installation:
    git clone git://github.com/Mipu94/peda-heap.git ~/peda-heap
    echo "source ~/peda-heap/peda.py" >> ~/.gdbinit

## Screenshot
 ![heap all](http://i.imgur.com/jvzXtLy.png)
 ![heap trace](http://i.imgur.com/3uQ4mlb.png)
 ![xstruct msg 0x1e7f0f0](http://i.imgur.com/8vzZ7e2.png)
