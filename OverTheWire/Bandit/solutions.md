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

## Level 13
The only thing we've got to do is to log in using private key.
```
bandit13@melinda:~$ ls
sshkey.private
bandit13@melinda:~$ ssh bandit14@localhost -i sshkey.private 
...
bandit14@melinda:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

## Level 14
Submitting password to port 30000? Seems easy.
```
bandit14@melinda:~$ nc localhost 30000 <<< "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e"
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

## Level 15
Now we have to handle SSL to get the password. Although `netcat` doesn't support SSL, we can use `ncat` from Nmap package.
```
bandit15@melinda:~$ ncat --ssl localhost 30001
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd
```

## Level 16
Let's start with scanning for open ports.
```
bandit16@melinda:~$ nmap localhost -p 31000-32000 -sV

Starting Nmap 6.40 ( http://nmap.org ) at 2016-09-20 21:41 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00056s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE VERSION
31046/tcp open  echo
31518/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
31691/tcp open  echo
31790/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
31960/tcp open  echo
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Nmap done: 1 IP address (1 host up) scanned in 41.24 seconds
```
Seems that there are only 5 open ports. Three of them are echo our input. The other 2 are more interesting. Let's talk to them with SSL.

```
bandit16@melinda:~$ ncat --ssl localhost 31790
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

## Level 17
Last time, we've got a private key, so begin by logging in using this identity. SSH is probably going to complain about file permissions, so `chmod` private key to something like `600`.
```
bandit17@melinda:~$ diff passwords.old passwords.new
42c42
< BS8bqB1kqkinKJjuxL6k072Qq9NRwQpR
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

## Level 18
Although someone was really nice and modified our `.bashrc`, we can still ask SSH to run some command for us
```
ssh bandit18@bandit.labs.overthewire.org "cat readme"

This is the OverTheWire game server. More information on http://www.overthewire.org/wargames

Please note that wargame usernames are no longer level<X>, but wargamename<X>
e.g. vortex4, semtex2, ...

Note: at this moment, blacksun is not available.

bandit18@bandit.labs.overthewire.org's password: 
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## Level 19
```
bandit19@melinda:~$ ls -l
total 8
-rwsr-x--- 1 bandit20 bandit19 7370 Nov 14  2014 bandit20-do
```
We can see that this executable has permission `s`. Thus, we'll be able to read file normally inaccessible.
```
bandit19@melinda:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
bandit19@melinda:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## Level 20
This is the first time we're going to use two terminals at the same time.
Let's start the server on the first one
```
bandit20@melinda:~$ nc -l -p 12345 <<< "GbKksEFF4yrVs6il55v6gwY5aVje5f0j"
```
And connect to it on the other one
```
bandit20@melinda:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@melinda:~$ ./suconnect 12345
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
```
We should see password to the next level: `gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr`

## Level 21
Let's read the crontab.
```
bandit21@melinda:~$ cat /etc/cron.d/cronjob_bandit22
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```
And see what script is cron executing.
```
bandit21@melinda:~$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```
`cat` will do the job.
```
bandit21@melinda:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

## Level 22
We're starting just like we did before.
```
bandit22@melinda:~$ cat /etc/cron.d/cronjob_bandit23
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@melinda:~$ cat /usr/bin/cronjob_bandit23.sh 
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
Script is writing password to some place in `/tmp`. We have to make out where.
```
bandit22@melinda:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1 
8ca319486bfbbc3663ea0fbe81326349
bandit22@melinda:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
``

## Level 23
```
bandit23@melinda:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit23@melinda:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 "./$i"
	rm -f "./$i"
    fi
done
```
As we can see, cron is running scripts and then deleting them. So we have to make him read the password for us. We're going to grab it with netcat.
In `/var/spool/bandit24` create small script looking somewhat like this:
```
#!/bin/bash
nc localhost 12345 < /etc/bandit_pass/bandit24
```
Don't forget to make it executable!
Start listening on other terminal
```
bandit23@melinda:~$ nc -l -p 12345
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

## Level 24
This time, we're going to build a pretty nice one-liner to solve this task.
Let's begin by creating a list of pincodes with `seq -w 9999`, then prepend all lines with password to this level with `sed 's/^/UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ /'` and pipe it to server using `nc localhost 30002`. To extract the password, append `sort | uniq`.

```
bandit24@melinda$ seq -w 9999 | sed 's/^/UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ /' | nc localhost 30002 | sort | uniq

Correct!
Exiting.
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
Wrong! Please enter the correct pincode. Try again.
```

# Level 25
Logging in should be fairly easy, because we were given the private key to log in.
```
bandit25@melinda:~$ ls
bandit26.sshkey
```
However, when trying to log in, `bandit26` is printed and we get disconnected.
Let's check `/etc/passwd` to find out which shell is `bandit26` using and analyze it.
```
bandit25@melinda:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@melinda:~$ cat /usr/bin/showtext
#!/bin/sh

more ~/text.txt
exit 0
```
To avoid exiting `more`, resize terminal to just a few lines. Reading man pages, reveals that `v` key will launch deafult text editor(vim). To read password type `:e /etc/bandit_pass/bandit26`. The password is `5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z`.

FIN

