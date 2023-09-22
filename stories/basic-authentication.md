### Timeline
In the beginning, there was nothing. Then, there was a TCP connection initiated by my browser at IP `192.168.64.6` on port `56666` to connect to Jeff's server at IP `45.79.89.123`. Because the intention of the TCP connection was to later send an HTTP request, all the TCP packets talks to the default HTTP port `80` on Jeff's server. 
![[Pasted image 20230921222251.png]]
![[Pasted image 20230921222329.png]]

All seemed well until my browser asked to see some secretive content on Jeff's server by sending an HTTP GET request to the URL `http://cs338.jeffondich.com/basicauth/`.
Because no credential is provided, the browser received a `401` response code, indicating that the client is not authorized to access the wanted resource (https://datatracker.ietf.org/doc/html/rfc7231#section-6.1). 

![[Pasted image 20230921223606.png]]
But the server did more than just denial, it also specified how to unlock its secrecy. In server's HTTP response header, there was a field named `WWW-Authenticate` that tells the client what type of authentication is needed. In this case, the value `Basic` referred to the 'Basic' HTTP Authentication Scheme specified in RFC 7617 (https://datatracker.ietf.org/doc/html/rfc7617#page-3).
What's also included in the field is the required parameter `realm`. According to the RFC 7617, a realm, also known as a protected space, is defined by the canonical root URI that can partition the access right of protected resources on the server. In our case, we were trying to access the realm under `http://cs338.jeffondich.com/basicauth/` with realm name `Protected Area`.

![[Pasted image 20230921224646.png]]
After acknowledging receiving this information with a TCP packet in `ACK` flag, the browser client prompt user a window to input user-id and password to satisfy the 'Basic' authentication scheme. This authentication scheme requires the client to do the following:
```
1.  obtains the user-id and password from the user,

2.  constructs the user-pass by concatenating the user-id, a single
    colon (":") character, and the password,

3.  encodes the user-pass into an octet sequence (see below for a
    discussion of character encoding schemes),

4.  and obtains the basic-credentials by encoding this octet sequence
    using Base64.
```
As the RFC described, the browser will get user-id and password from the prompt window inputs, concatenate them with `:` , encode them with Base64, and send them in the next HTTP request header.

![[Pasted image 20230921225856.png]]
From this example, we can see that the next HTTP request header included a `Authorization` field. It confirmed that it's following the `Basic` authentication scheme, and attached the Base64 string `Y3MzMzg6cGFzc3dvcmQ=`, which decoded to the user-id:password. It's worth noticing that Base64 is an encoding not encryption, meaning that user-id and password are basically sent through the internet in plaintext. Any eavesdropper tapping into the network can easily acquire this pair of user-pass. This is why the Security Considerations section of RFC 7617 highlighted that the 'Basic' HTTP authentication scheme SHOULD NOT be used to protect anything sensitive or valuable.
We can deduce from this that in our interaction with `http://cs338.jeffondich.com/basicauth/`, the password's correctness is checked by the server. If client can already determine the correctness of the password, it won't need to send the password as plaintext to the server. This is further proven when we input the wrong password of which we shall see the reason later. From now on, our story can diverge a little.
#### If the user inputs the correct user-id and password
In this case, we got the access to the protected resource. The server sent the content we want with a `200` success status code. We now see that the content we want is an HTML document with some basic layouts and links.
![[Pasted image 20230921231556.png]]
![[Pasted image 20230921231608.png]]

When we click any links to visit any page under `/basicauth/`, the authorization header will still be included so that we don't have to input user-id and passcode again for resource under the same protection space. 
![[Pasted image 20230921232115.png]]
This "caching" behavior is specified in section 6.2 in RFC 7617
> Existing HTTP clients and user agents typically retain authentication
   information indefinitely.  HTTP does not provide a mechanism for the
   origin server to direct clients to discard these cached credentials,
   since the protocol has no awareness of how credentials are obtained or managed by the user agent.
#### If the user just doesn't input anything
In this annoying but actually common case, the browser will keep sending special TCP Keep Alive packets to tell the server keep the TCP connection open and continue to wait for user response. 
![[Pasted image 20230921232612.png]]
If at some point user closed the browser, TCP connection will be terminated by the server using TCP packet with `FIN` flag.
![[Pasted image 20230921232951.png]]
#### If the user entered the wrong user-id or password
The browser will still construct the user-pass and send it along, which shows it really doesn't check the password itself.
![[Pasted image 20230921233212.png]]
Upon receiving the wrong user-pass, the server will just ask with the same `401` unauthorized response again, and the browser prompt the user-id and password input once more.
![[Pasted image 20230921233441.png]]
