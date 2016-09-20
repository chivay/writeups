## Level 0
This level is really simple. We just log in and read password from a file.
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
Seems there are a few files to check. Let's try to find out something about them.
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

## Level 5
```
bandit5@melinda:~$ ls
inhere
bandit5@melinda:~$ cd inhere/ 
bandit5@melinda:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
```
We're not going to go through all those directories by hand. The hint we're given is quite useful.
File, we're looking for has exactly 1033 bytes.
```
bandit5@melinda:~/inhere$ find -size 1033c
./maybehere07/.file2
bandit5@melinda:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        bandit5@melinda:~/inhere$ 
```

## Level 6
This time we're going to use `find` again. Redirecting `stderr` to `/dev/null` will get rid of ugly error messages.
```
bandit6@melinda:~$ find / -user bandit7 -group bandit6 2> /dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@melinda:~$ cat /var/lib/dpkg/info/bandit7.password 
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## Level 7
To search for our next password, the almighty `grep` will come in handy.
```
bandit7@melinda:~$ ls
data.txt
bandit7@melinda:~$ grep millionth data.txt 
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## Level 8
Here, we have to use a standard combination of 2 programs: `sort` and `uniq`. By default `uniq` gets rid of duplicated lines. Passing additional argument `-u` will print only unique lines.
```
bandit8@melinda:~$ ls
data.txt
bandit8@melinda:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## Level 9
Simple, but useful `string` will extract readable lines, `grep` will filter those with `=` at the beginning of line.
```
bandit9@melinda:~$ strings data.txt | grep ^=
========== password
========== ism
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

## Level 10
```
bandit10@melinda:~$ base64 -d data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## Level 11
```
bandit11@melinda:~$ cat data.txt | tr A-Za-z N-ZA-Mn-za-m
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## Level 12
This is one of the most daunting and boring levels, so brace yourselves.
First, we need to reverse hexdump of file.
```
bandit12@melinda:~$ mkdir /tmp/butter
bandit12@melinda:~$ xxd -r data.txt > /tmp/butter/dump.bin
bandit12@melinda:~$ cd /tmp/butter
```
```
bandit12@melinda:/tmp/butter$ file dump.bin 
dump.bin: gzip compressed data, was "data2.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
bandit12@melinda:/tmp/butter$ mv dump.bin data.gz
bandit12@melinda:/tmp/butter$ gunzip data.gz
```
```
bandit12@melinda:/tmp/butter$ ls
data
bandit12@melinda:/tmp/butter$ file data 
data: bzip2 compressed data, block size = 900k
bandit12@melinda:/tmp/butter$ bunzip2 data
bunzip2: Can't guess original name for data -- using data.out
```
```
bandit12@melinda:/tmp/butter$ file data.out 
data.out: gzip compressed data, was "data4.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
bandit12@melinda:/tmp/butter$ mv data.out data.gz
bandit12@melinda:/tmp/butter$ gunzip data.gz
```
```
bandit12@melinda:/tmp/butter$ file data 
data: POSIX tar archive (GNU)
bandit12@melinda:/tmp/butter$ tar -xvf data
data5.bin
bandit12@melinda:/tmp/butter$ tar -xvf data5.bin
data6.bin
```
```
bandit12@melinda:/tmp/butter$ file data6.bin 
data6.bin: bzip2 compressed data, block size = 900k
bandit12@melinda:/tmp/butter$ bunzip2 data6.bin
bunzip2: Can't guess original name for data6.bin -- using data6.bin.out
```
```
bandit12@melinda:/tmp/butter$ file data6.bin.out 
data6.bin.out: POSIX tar archive (GNU)
bandit12@melinda:/tmp/butter$ tar -xvf data6.bin.out
data8.bin
```
```
bandit12@melinda:/tmp/butter$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
bandit12@melinda:/tmp/butter$ mv data8.bin data8.gz
bandit12@melinda:/tmp/butter$ gunzip data8.gz 
```
```
bandit12@melinda:/tmp/butter$ cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
Of course, if we knew the way compression was chained, we could alternatively do
```
bandit12@melinda:/tmp/butter$ zcat dump.bin | bzcat | zcat | tar -xO | tar -xO | bzcat | tar -xO | zcat
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```
