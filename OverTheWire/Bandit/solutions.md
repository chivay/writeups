## Level 0
This level is really simple. We just login and read password from a file.
```bash
bandit0@melinda:~$ ls
readme
bandit0@melinda:~$ cat readme 
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

## Level 1
The trick here is to avoid using `-` directly since by default it is equivalent to reading from `STDIN`, so we explicitly ask `cat` to read a file from current directory.
```
bandit1@melinda:~$ ls
-
bandit1@melinda:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

## Level 2
Just hit `Tab` and we're done.
```
bandit2@melinda:~$ ls
spaces in this filename
bandit2@melinda:~$ cat spaces\ in\ this\ filename 
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## Level 3
```
bandit3@melinda:~$ ls
inhere
bandit3@melinda:~$ cd inhere/
bandit3@melinda:~/inhere$ ls
bandit3@melinda:~/inhere$
```
Since `ls` gave no output we can assume that the file is hidden.
```
bandit3@melinda:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Nov 14  2014 .
drwxr-xr-x 3 root    root    4096 Nov 14  2014 ..
-rw-r----- 1 bandit4 bandit3   33 Nov 14  2014 .hidden
bandit3@melinda:~/inhere$ cat .hidden   
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

## Level 4
```
bandit4@melinda:~$ ls
inhere
bandit4@melinda:~$ cd inhere/
bandit4@melinda:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```
Seems the is a few files to check. Let's try to find out something about them.
```
bandit4@melinda:~/inhere$ file *
file: Cannot open `ile00' (No such file or directory).
file: Cannot open `ile01' (No such file or directory).
...
```
Turns out that `file` tries to parse our filenames some parameters. We can get around that using `--` which tells `file` that there are no other parameters to parse.
```
bandit4@melinda:~/inhere$ file -- *
-file00: data
-file01: data
-file02: data
-file03: data
-file04: data
-file05: data
-file06: data
-file07: ASCII text
-file08: data
-file09: data
bandit4@melinda:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```
