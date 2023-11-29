# <p align='center'>0x07. Networking basics #0</p>

<details>
    <summary><h1>Table of Contents</h1></summary>

- [Resources](#resources)
- [Mandatory](#mandatory)
    - [0. OSI model](#0-osi-model)
    - [1. Types of network](#1-types-of-network)
    - [2. MAC and IP address](#2-mac-and-ip-address)
    - [3. UDP and TCP](#3-udp-and-tcp)
    - [4. TCP and UDP ports](#4-tcp-and-udp-ports)
    - [5. Is the host on the network](#5-is-the-host-on-the-network)

</details>

## OSI Model
- What it is
- How many layers it has
- How it is organized

## What is a LAN
- Typical usage
- Typical geographical size

## What is a WAN
- Typical usage
- Typical geographical size

## What is the Internet
- What is an IP address
- What are the 2 types of IP address
- What is `localhost`
- What is a subnet
- Why IPv6 was created

## TCP/UDP
- What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
- What is the main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network

## Resources
Read or watch:

- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
- [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
- [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://www.adminschoice.com/bash-positional-parameters)

man or help:

- `netstat`
- `ping`

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your Bash script files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `shellcheck` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info
The second line of all your Bash scripts should be a comment explaining what is the script doing

For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:

What is the most important position in a software company?

1. Project manager
2. Backend developer
3. System administrator
```shell
sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
```
Source for question 1 [here](https://twitter.com/devopsreact/status/831922429215662080).

# <p align='center'>Tasks</p>

<br>

## <p align='center'>Mandatory</p>

<br>

### 0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![image](https://github.com/Bebo-K-S/alx-system_engineering-devops/assets/107813045/e7cc2017-6c50-46eb-bef9-d3928541cce3)

In this project we will mainly focus on:

- The Transport layer and especially TCP/UDP
- On the Network layer with IP and ICMP

The image bellow describes more concretely how you can relate to every level.

![image](https://github.com/Bebo-K-S/alx-system_engineering-devops/assets/107813045/4ade9f16-186b-4399-8eda-58df3b075f61)

Questions:

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

1. Alphabetically
2. From the lowest to the highest level
3. Randomly

<br>

Solution: [0-OSI_model](0-OSI_model).

<hr>
  
### 1. Types of network

![image](https://github.com/Bebo-K-S/alx-system_engineering-devops/assets/107813045/c4a0ad85-8504-4a84-9187-6c93807eb568)

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

1. Internet
2. WAN
3. LAN

What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. WAN
3. LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

1. Internet
2. WAN
3. LAN

<br>

Solution: [1-types_of_network](1-types_of_network).

<hr>

### 2. MAC and IP address

![image](https://github.com/Bebo-K-S/alx-system_engineering-devops/assets/107813045/b4eee25f-136f-4504-8e26-318643859bd4)

Questions:

What is a MAC address?

1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

What is an IP address?

1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

<br>

Solution: [2-MAC_and_IP_address](2-MAC_and_IP_address).

<hr>

### 3. UDP and TCP

![image](https://github.com/Bebo-K-S/alx-system_engineering-devops/assets/107813045/38a64039-b16f-4f25-8b61-08e4875ca320)

Let’s fill the empty parts in the drawing above.

Questions:

- Which statement is correct for the TCP box:
1. `It is a protocol that is transferring data in a slow way but surely`
2. `It is a protocol that is transferring data in a fast way and might loss data along in the process`

- Which statement is correct for the UDP box:
1. `It is a protocol that is transferring data in a slow way but surely`
2. `It is a protocol that is transferring data in a fast way and might loss data along in the process`

- Which statement is correct for the TCP worker:
1. `Have you received boxes x, y, z?`
2. `May I increase the rate at which I am sending you boxes?`

<br>

Solutoin: [3-UDP_and_TCP](3-UDP_and_TCP).

<hr>
  
### 4. TCP and UDP ports

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

- **22** for SSH
- **80** for HTTP
- **443** for HTTPS
Note that a specific [IP + port = socket](https://stackoverflow.com/questions/152457/what-is-the-difference-between-a-port-and-a-socket).

Write a Bash script that displays listening ports:

- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs

Example:

```shell
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
```

<br>

Solution: [4-TCP_and_UDP_ports](4-TCP_and_UDP_ports).

<hr>
  
### 5. Is the host on the network

![pingpong](https://media.giphy.com/media/uDxkJAVSU7GY8/giphy.gif)


The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command `ping` uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

- Accepts a string as an argument
- Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
- Ping the IP 5 times

Example:

```shell
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
```

It is interesting to look at the `time` value, which is the time that it took for the ICMP request to go to the `8.8.8.8` IP and come back to my host. The IP `8.8.8.8` is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the `ping` command to see what is going on!

<br>

Solution: [5-is_the_host_on_the_network](5-is_the_host_on_the_network).
