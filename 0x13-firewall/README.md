# Firewall (computing)

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/Firewall_%28computing%29#mw-head)[Jump to search](https://en.wikipedia.org/wiki/Firewall_%28computing%29#searchInput)

Part of a series on

[Information security](https://en.wikipedia.org/wiki/Information_security "Information security")

[

In  [computing](https://en.wikipedia.org/wiki/Computing "Computing"), a  **firewall**  is a  [network security](https://en.wikipedia.org/wiki/Network_security "Network security")  system that  [monitors](https://en.wikipedia.org/wiki/Network_monitoring "Network monitoring")  and controls incoming and outgoing  [network traffic](https://en.wikipedia.org/wiki/Network_traffic "Network traffic")  based on predetermined security rules.[[1]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-1)  A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the  [Internet](https://en.wikipedia.org/wiki/Internet "Internet").[[2]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-Oppliger_1997_94-2)

## Contents



## History[[edit](https://en.wikipedia.org/w/index.php?title=Firewall_(computing)&action=edit&section=1 "Edit section: History")]

The term  _[firewall](https://en.wikipedia.org/wiki/Firewall_(construction) "Firewall (construction)")_  originally referred to a wall intended to confine a fire within a line of adjacent buildings.[[3]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-3)  Later uses refer to similar structures, such as the  [metal sheet](https://en.wikipedia.org/wiki/Firewall_(engine) "Firewall (engine)")  separating the  [engine](https://en.wikipedia.org/wiki/Engine "Engine")  compartment of a vehicle or  [aircraft](https://en.wikipedia.org/wiki/Aircraft "Aircraft")  from the passenger compartment. The term was applied in the late 1980s to network technology[[4]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-cheskwick1994-4)  that emerged when the Internet was fairly new in terms of its global use and connectivity.[[5]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-5)  The predecessors to firewalls for network security were  [routers](https://en.wikipedia.org/wiki/Router_(computing) "Router (computing)")  used in the late 1980s. Because they already segregated networks, routers could apply filtering to packets crossing them.[[6]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-report_unm-6)

Before it was used in real-life computing, the term appeared in the 1983 computer-hacking movie  [WarGames](https://en.wikipedia.org/wiki/WarGames "WarGames"), and possibly inspired its later use.[[7]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-7)

## Types[[edit](https://en.wikipedia.org/w/index.php?title=Firewall_(computing)&action=edit&section=2 "Edit section: Types")]

See also:  [Computer security](https://en.wikipedia.org/wiki/Computer_security "Computer security")  and  [Comparison of firewalls](https://en.wikipedia.org/wiki/Comparison_of_firewalls "Comparison of firewalls")

Firewalls are categorized as a network-based or a host-based system. Network-based firewalls can be positioned anywhere within a  [LAN](https://en.wikipedia.org/wiki/Local_area_network "Local area network")  or  [WAN](https://en.wikipedia.org/wiki/Wide_area_network "Wide area network").[[8]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-8)  They are either a  [software appliance](https://en.wikipedia.org/wiki/Software_appliance "Software appliance")  running on general-purpose hardware, a  [hardware appliance](https://en.wikipedia.org/wiki/Computer_appliance#Types_of_appliances "Computer appliance")  running on special-purpose hardware, or a  [virtual appliance](https://en.wikipedia.org/wiki/Virtual_appliance "Virtual appliance")  running on a virtual host controlled by a  [hypervisor](https://en.wikipedia.org/wiki/Hypervisor "Hypervisor"). Firewall appliances may also offer non firewall functionality, such as  [DHCP](https://en.wikipedia.org/wiki/DHCP "DHCP")[[9]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-9)[[10]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-10)  or  [VPN](https://en.wikipedia.org/wiki/VPN "VPN")[[11]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-11)  services. Host-based firewalls are deployed directly on the  [host](https://en.wikipedia.org/wiki/Host_(network) "Host (network)")  itself to control network traffic or other computing resources.[[12]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-12)[[13]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-13)  This can be a  [daemon](https://en.wikipedia.org/wiki/Daemon_(computing) "Daemon (computing)")  or  [service](https://en.wikipedia.org/wiki/Windows_service "Windows service")  as a part of the  [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system")  or an  [agent application](https://en.wikipedia.org/wiki/Endpoint_security "Endpoint security")  for protection.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Firewall.png/220px-Firewall.png)](https://en.wikipedia.org/wiki/File:Firewall.png)

An illustration of a network based firewall within a network

### Packet filter[[edit](https://en.wikipedia.org/w/index.php?title=Firewall_(computing)&action=edit&section=3 "Edit section: Packet filter")]

The first reported type of network firewall is called a packet filter, which inspect packets transferred between computers. The firewall maintains an  [access control list](https://en.wikipedia.org/wiki/Access_control_list "Access control list")  which dictates what packets will be looked at and what action should be applied, if any, with the default action set to silent discard. Three basic actions regarding the packet consist of a silent discard, discard with  [Internet Control Message Protocol](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol "Internet Control Message Protocol")  or  [TCP reset](https://en.wikipedia.org/wiki/TCP_reset_attack "TCP reset attack")  response to the sender, and forward to the next hop.[[14]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-14)  Packets may be filtered by source and destination  [IP addresses](https://en.wikipedia.org/wiki/Network_address "Network address"), protocol, source and destination  [ports](https://en.wikipedia.org/wiki/Port_number "Port number"). The bulk of Internet communication in 20th and early 21st century used either  [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol "Transmission Control Protocol")  (TCP) or  [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol "User Datagram Protocol")  (UDP) in conjunction with  [well-known ports](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers "List of TCP and UDP port numbers"), enabling firewalls of that era to distinguish between specific types of traffic such as web browsing, remote printing, email transmission, and file transfers.[[15]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-15)[[16]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-cheswick2003-16)

The first paper published on firewall technology was in 1987 when engineers from  [Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation "Digital Equipment Corporation")  (DEC) developed filter systems known as packet filter firewalls. At  [AT&T Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs "Bell Labs"),  [Bill Cheswick](https://en.wikipedia.org/wiki/William_Cheswick "William Cheswick")  and  [Steve Bellovin](https://en.wikipedia.org/wiki/Steven_M._Bellovin "Steven M. Bellovin")  continued their research in packet filtering and developed a working model for their own company based on their original first-generation architecture.[[17]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-17)

### Connection tracking[[edit](https://en.wikipedia.org/w/index.php?title=Firewall_(computing)&action=edit&section=4 "Edit section: Connection tracking")]

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Netfilter-packet-flow.svg/220px-Netfilter-packet-flow.svg.png)](https://en.wikipedia.org/wiki/File:Netfilter-packet-flow.svg)

Flow of  [network packets](https://en.wikipedia.org/wiki/Network_packet "Network packet")  through  [Netfilter](https://en.wikipedia.org/wiki/Netfilter "Netfilter"), a  [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel "Linux kernel")  module

Main article:  [Stateful firewall](https://en.wikipedia.org/wiki/Stateful_firewall "Stateful firewall")

From 1989–1990, three colleagues from  [AT&T Bell Laboratories](https://en.wikipedia.org/wiki/AT%26T_Bell_Laboratories "AT&T Bell Laboratories"), Dave Presotto, Janardan Sharma, and Kshitij Nigam, developed the second generation of firewalls, calling them  [circuit-level gateways](https://en.wikipedia.org/wiki/Circuit-level_gateway "Circuit-level gateway").[[18]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-18)

Second-generation firewalls perform the work of their first-generation predecessors but also maintain knowledge of specific conversations between endpoints by remembering which port number the two  [IP addresses](https://en.wikipedia.org/wiki/IP_address "IP address")  are using at layer 4 ([transport layer](https://en.wikipedia.org/wiki/Transport_layer "Transport layer")) of the  [OSI model](https://en.wikipedia.org/wiki/OSI_model "OSI model")  for their conversation, allowing examination of the overall exchange between the nodes.[[19]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-19)

### Application layer[[edit](https://en.wikipedia.org/w/index.php?title=Firewall_(computing)&action=edit&section=5 "Edit section: Application layer")]

Main article:  [Application firewall](https://en.wikipedia.org/wiki/Application_firewall "Application firewall")

[Marcus Ranum](https://en.wikipedia.org/wiki/Marcus_Ranum "Marcus Ranum"), Wei Xu, and Peter Churchyard released an application firewall known as Firewall Toolkit (FWTK) in October 1993.[[20]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-20)  This became the basis for Gauntlet firewall at  [Trusted Information Systems](https://en.wikipedia.org/wiki/Trusted_Information_Systems "Trusted Information Systems").[[21]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-21)[[22]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-22)

The key benefit of  [application layer](https://en.wikipedia.org/wiki/Application_layer "Application layer")  filtering is that it can understand certain applications and protocols such as  [File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol "File Transfer Protocol")  (FTP),  [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System "Domain Name System")  (DNS), or  [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol")  (HTTP). This allows it to identify unwanted applications or services using a non standard port, or detect if an allowed protocol is being abused.[[23]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-23)  It can also provide unified security management including enforced  [encrypted DNS](https://en.wikipedia.org/wiki/DNS_over_TLS "DNS over TLS")  and  [virtual private networking](https://en.wikipedia.org/wiki/Virtual_private_network "Virtual private network").[[24]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-24)[[25]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-25)[[26]](https://en.wikipedia.org/wiki/Firewall_%28computing%29#cite_note-26)

As of 2012, the  [next-generation firewall](https://en.wikipedia.org/wiki/Next-generation_firewall "Next-generation firewall")  provides a wider range of inspection at the application layer, extending  [deep packet inspection](https://en.wikipedia.org/wiki/Deep_packet_inspection "Deep packet inspection")  functionality to include, but is not limited to:

-   [Web filtering](https://en.wikipedia.org/wiki/Web_filtering "Web filtering")
-   [Intrusion prevention systems](https://en.wikipedia.org/wiki/Intrusion_prevention_system "Intrusion prevention system")
-   [User identity management](https://en.wikipedia.org/wiki/Identity_management "Identity management")
-   [Web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall "Web application firewall")

#### Endpoint specific[[edit](https://en.wikipedia.org/w/index.php?title=Firewall_(computing)&action=edit&section=6 "Edit section: Endpoint specific")]

Endpoint based application firewalls function by determining whether a process should accept any given connection. Application firewalls filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. Application firewalls accomplish their function by hooking into socket calls to filter the connections between the application layer and the lower layers. Application firewalls that hook into socket calls are also referred to as socket filters.[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]