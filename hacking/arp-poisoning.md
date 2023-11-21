Name: Tianyi Lu
## Execution
a. b6:8d:4a:d3:b8:d6
![[Pasted image 20231121013714.png]]
    
b. 192.168.64.6
![[Pasted image 20231121013743.png]]

c. 7a:ff:f2:3e:be:a6
![[Pasted image 20231121013806.png]]
    
d. 192.168.64.7
![[Pasted image 20231121013913.png]]
    
e.
![[Pasted image 20231121014720.png]]
    
f.
![[Pasted image 20231121014036.png]]
g.
![[Pasted image 20231121014746.png]]
h.
![[Pasted image 20231121014241.png]]
    
i. The `netstat -r` command output shows that the default gateway for this machine is at IP address 192.168.64.1. This is typically the address of the router or next-hop that packets should be sent to when the destination is not on the local subnet.

The `arp -n` command output shows the ARP table. In this case, the IP address 192.168.64.1 is mapped to the MAC address CE:08:FA:07:08:64.

Thus, the TCP SYN packet to start the HTTP query should be sent to the MAC address CE:08:FA:07:08:64.

j. HTTP response on Metasploitable:
![[Pasted image 20231121015438.png]]
Wireshark didn't capture any packet.
    
l. The MAC address for the default gateway 192.168.64.1 has changed to Kali's MAC address.
![[Pasted image 20231121021545.png]]
    
m. Without actually doing it yet, predict what will happen if you execute "curl http://cs338.jeffondich.com/" on Metasploitable now. Specifically, to what MAC address will Metasploitable send the TCP SYN packet? Explain why.

Metasploitable will send the TCP SYN packet to Kali's MAC address b6:8d:4a:d3:b8:d6.
The ARP cache tells the Metasploitable machine that the default gateway (at IP address 192.168.64.1) has the MAC address b6:8d:4a:d3:b8:d6. Therefore, the Metasploitable machine will send the TCP SYN packet to this MAC address, which, because of ARP poisoning, belongs to the attacker's machine rather than the actual gateway.

o. HTTP response on Metasploitable:
![[Pasted image 20231121022423.png]]
Packets captured in Wireshark:
![[Pasted image 20231121022525.png]]
From Kali, we can see the TCP handshake packets and HTTP request and response between Metasploitable (192.168.64.7) and cs338.jeffondich.com (172.233.221.124)
    
p. 
After running ARP poisoning on Kali, Kali will repeatedly send out corrupted ARP response to Metasploitable's MAC address. The next time Metasploitable sends ARP request for 192.168.64.1, corrupted ARP response will step in. Then, Metasploitable will receive attacker's MAC address for the default gateway and store this entry in its ARP cache.
![[Pasted image 20231121023257.png]]

q. The ARP spoofing detector will detect duplicated MAC addresses for a specific IP address in ARP message histories. ARP spoofing is very likely happening especially when the IP address for the default gateway on the network is mapped to multiple MAC addresses.
![[Pasted image 20231121024437.png]]
## Synthesis
a. When Alice attempts to communicate with Bob over a network, her packets are initially sent to the local network's default gateway interface before being forwarded to Bob. To correctly identify this gateway, Alice needs to know both its IP and MAC addresses. She typically obtains the MAC address from her local ARP cache. However, this process can be compromised by Mal. Mal can exploit the ARP cache's functionality, where it updates whenever an IP address is resolved to a MAC address. By repeatedly sending ARP responses to Alice while posing as the default gateway, Mal can deceive Alice into updating her ARP cache with a falsified IP-MAC mapping. Consequently, all of Alice's packets intended for Bob will be rerouted through Mal first, allowing him to view them in their entirety.

b. It is detectable. If a Alice keeps a record of ARP responses, a sudden change in the MAC address associated with an IP address, without a corresponding change in the network could be suspicious. There are tools available that can monitor the ARP traffic on the network and alert administrators to unusual patterns, such as the same IP address being associated with different MAC addresses in a short period of time, or a single MAC address claiming to own multiple IP addresses.

c. Bob generally can't detect the attack. Bob, which is likely remote and not on the same local network, does not see ARP traffic because ARP requests and responses are not routed across the internet.

d. Using HTTPS instead of HTTP would not prevent ARP poisoning itself because ARP poisoning attacks occur at the local network. However, HTTPS can mitigate some of the risks associated with ARP poisoning, particularly the risk of man-in-the-middle attacks that could intercept or modify the data being transmitted.

For Alice:
Alice would still detect the ARP poisoning itself by monitoring local ARP traffic.
HTTPS ensures that the communication between the Alice and Bob is encrypted. Therefore, even if an attacker intercepts the traffic through ARP poisoning, they would not be able to read or modify the HTTPS traffic easily due to the strong encryption.

For Bob:
Bob would still not detect the ARP poisoning, as it does not participate in the ARP process of the local network. However, Bob can detect a MitM attack if the attacker tries to intercept the HTTPS connection and present a false certificate, as browsers and clients check the validity of the server's SSL certificate. If the certificate does not match or is not signed by a trusted certificate authority, the browser or client would alert the user.