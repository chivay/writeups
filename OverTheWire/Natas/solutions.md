## Level 0
Looking at source reveals the password
```
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

## Level 1
Although right-click has been block, `Ctrl + U`(Chromium) should show source.
```
<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```

## Level 2
Although there is nothing on this page, `<img src="files/pixel.png">` reveals directory containing file `users.txt` with password inside.
```
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```

## Level 3
`Not even Google will find it this time...` suggests that we should look at `robots.txt`.
```
User-agent: *
Disallow: /s3cr3t/
```
Once again, password is inside txt file `natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

## Level 4
This time, we're going to need some help from useful extensions. I'm using Postman with Postman interceptor for Chrome to spoof `Referer` variable. Sending request with referest set to `http://natas4.natas.labs.overthewire.org/index.php` will reveal the password.
```
Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
```


## Level 5
Looking up source gives no clues. However, we can see that the cookie named `loggedin` is set to value `0`. Changing it to `1` will log us in.
```
Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

## Level 6
We can look up the PHP source and see that file `includes/secret.inc` is included into the script. Because it's not interpreted by PHP we can directly see it in browser.
```
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```
```
Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```

## Level 7
## Level 8
## Level 9
## Level 10
## Level 11
## Level 12
## Level 13
## Level 14
## Level 15
## Level 16
## Level 17
## Level 18
## Level 19
## Level 20
## Level 21
## Level 22
## Level 23
## Level 24
## Level 25
## Level 26
## Level 27
## Level 28
## Level 29
## Level 30
## Level 31
## Level 32
## Level 33

