# Advent of cyber 2 | day 4 | Santa's watching 

> Tal Baraz

For me the ip for the machine was:`10.10.115.208` it probably be diffrent for you.

## Question 1
No answer needed

## Question 2
From the examples and what we've read about wfuzz we can write:
```bash
wfuzz -c -z file,big.txt -d "breed=FUZZ" -u http://shibes.xyz/api.php
```
Which is the answer.

## Question 3
after using gobuster with the dirbuster wordlist (lol) like a so:
```bash
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,txt,html -u http://10.10.115.208/
```
we find:
```
/index.html (Status: 200)
/api (Status: 301)
``` 
In `/api` we can find an index with a single file `site-log.php` 
which is the answer to the qeustion

## Question 4
As the question tells us there's a date GET parameter on `http://10.10.115.208/api/site-log.php`
we know the format for the site is `YYYYMMDD`, so we are intrested in the log info for the last 2 months or so.
So we gonna use wfuzz to fuzz the date parameter with the given wordlist
or
we could write a script to generate 1 (which is what I did)
our command will look like this:
```bash
wfuzz -c -z file,wordlist -d "date=FUZZ" -u "http://10.10.115.208/api/site-log.php" | grep -v "0 Ch"
```
added the reverse grep to exclude empty results

we get a potential entry for `20201125`
going to `http://10.10.115.208/api/site-log.php?date=20201125` we can see the flag `THM{D4t3_AP1}`