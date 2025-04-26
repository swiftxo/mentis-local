---
title: "Network congestion - Wikipedia"
source: "https://en.wikipedia.org/wiki/Network_congestion"
author:
published:
created: 2025-04-25
description:
tags:
  - "clippings"
---
**Network congestion** in [data networking](https://en.wikipedia.org/wiki/Data_networking "Data networking") and [queueing theory](https://en.wikipedia.org/wiki/Queueing_theory "Queueing theory") is the reduced [quality of service](https://en.wikipedia.org/wiki/Quality_of_service "Quality of service") that occurs when a network node or link is carrying more data than it can handle. Typical effects include [queueing delay](https://en.wikipedia.org/wiki/Queueing_delay "Queueing delay"), [packet loss](https://en.wikipedia.org/wiki/Packet_loss "Packet loss") or the blocking of new connections. A consequence of congestion is that an incremental increase in [offered load](https://en.wikipedia.org/wiki/Offered_load "Offered load") leads either only to a small increase or even a decrease in network [throughput](https://en.wikipedia.org/wiki/Throughput "Throughput").[^1]

[Network protocols](https://en.wikipedia.org/wiki/Network_protocol "Network protocol") that use aggressive [retransmissions](https://en.wikipedia.org/wiki/Retransmission_\(data_networks\) "Retransmission (data networks)") to compensate for packet loss due to congestion can increase congestion, even after the initial load has been reduced to a level that would not normally have induced network congestion. Such networks exhibit two stable states under the same level of load. The stable state with low throughput is known as **congestive collapse**.

Networks use **congestion control** and **congestion avoidance** techniques to try to avoid collapse. These include: [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff "Exponential backoff") in protocols such as [CSMA/CA](https://en.wikipedia.org/wiki/CSMA/CA "CSMA/CA") in [802.11](https://en.wikipedia.org/wiki/802.11 "802.11") and the similar [CSMA/CD](https://en.wikipedia.org/wiki/CSMA/CD "CSMA/CD") in the original [Ethernet](https://en.wikipedia.org/wiki/Ethernet "Ethernet"), [window](https://en.wikipedia.org/wiki/Sliding_window "Sliding window") reduction in [TCP](https://en.wikipedia.org/wiki/Transmission_control_protocol "Transmission control protocol"), and [fair queueing](https://en.wikipedia.org/wiki/Fair_queueing "Fair queueing") in devices such as [routers](https://en.wikipedia.org/wiki/Router_\(computing\) "Router (computing)") and [network switches](https://en.wikipedia.org/wiki/Network_switch "Network switch"). Other techniques that address congestion include priority schemes which transmit some packets with higher priority ahead of others and the explicit allocation of network resources to specific flows through the use of [admission control](https://en.wikipedia.org/wiki/Admission_control "Admission control").

## Network capacity

Network resources are limited, including [router](https://en.wikipedia.org/wiki/Router_\(computing\) "Router (computing)") processing time and link [throughput](https://en.wikipedia.org/wiki/Throughput "Throughput"). [Resource contention](https://en.wikipedia.org/wiki/Resource_contention "Resource contention") may occur on networks in several common circumstances. A [wireless LAN](https://en.wikipedia.org/wiki/Wireless_LAN "Wireless LAN") is easily filled by a single personal computer.[^2] Even on fast computer networks, the [backbone](https://en.wikipedia.org/wiki/Backbone_network "Backbone network") can easily be congested by a few servers and client PCs. [Denial-of-service attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack "Denial-of-service attack") by [botnets](https://en.wikipedia.org/wiki/Botnet "Botnet") are capable of filling even the largest [Internet backbone](https://en.wikipedia.org/wiki/Internet_backbone "Internet backbone") network links, generating large-scale network congestion. In telephone networks, a [mass call event](https://en.wikipedia.org/wiki/Mass_call_event "Mass call event") can overwhelm digital telephone circuits, in what can otherwise be defined as a denial-of-service attack.

## Congestive collapse

Congestive collapse (or congestion collapse) is the condition in which congestion prevents or limits useful communication. Congestion collapse generally occurs at choke points in the network, where incoming traffic exceeds outgoing bandwidth. Connection points between a [local area network](https://en.wikipedia.org/wiki/Local_area_network "Local area network") and a [wide area network](https://en.wikipedia.org/wiki/Wide_area_network "Wide area network") are common choke points. When a network is in this condition, it settles into a stable state where traffic demand is high but little useful throughput is available, during which [packet delay](https://en.wikipedia.org/wiki/Packet_delay "Packet delay") and loss occur and [quality of service](https://en.wikipedia.org/wiki/Quality_of_service "Quality of service") is extremely poor.

Congestive collapse was identified as a possible problem by 1984.[^3] It was first observed on the early Internet in October 1986,[^4] when the [NSFNET](https://en.wikipedia.org/wiki/NSFNET "NSFNET") phase-I backbone dropped three orders of magnitude from its capacity of 32 kbit/s to 40 bit/s,[^5] which continued until end nodes started implementing [Van Jacobson](https://en.wikipedia.org/wiki/Van_Jacobson "Van Jacobson") and [Sally Floyd](https://en.wikipedia.org/wiki/Sally_Floyd "Sally Floyd") 's congestion control between 1987 and 1988.[^6] When more [packets](https://en.wikipedia.org/wiki/Packet_\(information_technology\) "Packet (information technology)") were sent than could be handled by intermediate routers, the intermediate routers discarded many packets, expecting the endpoints of the network to retransmit the information. However, early TCP implementations had poor retransmission behavior. When this packet loss occurred, the endpoints sent extra packets that repeated the information lost, doubling the incoming rate.

## Congestion control

Congestion control modulates traffic entry into a telecommunications network in order to avoid congestive collapse resulting from oversubscription.[^7] This is typically accomplished by reducing the rate of packets. Whereas congestion control prevents senders from overwhelming the *network*, [flow control](https://en.wikipedia.org/wiki/Flow_control_\(data\) "Flow control (data)") prevents the sender from overwhelming the *receiver*.

The theory of congestion control was pioneered by [Frank Kelly](https://en.wikipedia.org/wiki/Frank_Kelly_\(professor\) "Frank Kelly (professor)"), who applied [microeconomic theory](https://en.wikipedia.org/wiki/Microeconomic_theory "Microeconomic theory") and [convex optimization](https://en.wikipedia.org/wiki/Convex_optimization "Convex optimization") theory to describe how individuals controlling their own rates can interact to achieve an *optimal* network-wide rate allocation. Examples of *optimal* rate allocation are [max-min fair allocation](https://en.wikipedia.org/wiki/Max-min_fairness "Max-min fairness") and Kelly's suggestion of [proportionally fair](https://en.wikipedia.org/wiki/Proportionally_fair "Proportionally fair") allocation, although many others are possible.

Let ${\displaystyle x_{i}}$ be the rate of flow ${\displaystyle i}$ , ${\displaystyle c_{l}}$ be the capacity of link ${\displaystyle l}$ , and ${\displaystyle r_{li}}$ be 1 if flow ${\displaystyle i}$ uses link ${\displaystyle l}$ and 0 otherwise. Let ${\displaystyle x}$ , ${\displaystyle c}$ and ${\displaystyle R}$ be the corresponding vectors and matrix. Let ${\displaystyle U(x)}$ be an increasing, strictly [concave function](https://en.wikipedia.org/wiki/Concave_function "Concave function"), called the [utility](https://en.wikipedia.org/wiki/Utility "Utility"), which measures how much benefit a user obtains by transmitting at rate ${\displaystyle x}$ . The optimal rate allocation then satisfies

${\displaystyle \max \limits _{x}\sum _{i}U(x_{i})}$

such that ${\displaystyle Rx\leq c}$

The [Lagrange dual](https://en.wikipedia.org/wiki/Lagrange_duality "Lagrange duality") of this problem decouples so that each flow sets its own rate, based only on a *price* signaled by the network. Each link capacity imposes a constraint, which gives rise to a [Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier "Lagrange multiplier"), ${\displaystyle p_{l}}$ . The sum of these multipliers, ${\displaystyle y_{i}=\sum _{l}p_{l}r_{li},}$ is the price to which the flow responds.

Congestion control then becomes a distributed optimization algorithm. Many current congestion control algorithms can be modeled in this framework, with ${\displaystyle p_{l}}$ being either the loss probability or the queueing delay at link ${\displaystyle l}$ . A major weakness is that it assigns the same price to all flows, while sliding window flow control causes [burstiness](https://en.wikipedia.org/wiki/Burst_transmission "Burst transmission") that causes different flows to observe different loss or delay at a given link.

Among the ways to classify congestion control algorithms are:

- By type and amount of feedback received from the network: Loss; delay; single-bit or multi-bit explicit signals
- By incremental deployability: Only sender needs modification; sender and receiver need modification; only router needs modification; sender, receiver and routers need modification.
- By performance aspect: high bandwidth-delay product networks; lossy links; fairness; advantage to short flows; variable-rate links
- By fairness criterion: Max-min fairness; proportionally fair; [controlled delay](https://en.wikipedia.org/w/index.php?title=Controlled_delay&action=edit&redlink=1 "Controlled delay (page does not exist)")

## Mitigation

Mechanisms have been invented to prevent network congestion or to deal with a network collapse:

- [Network scheduler](https://en.wikipedia.org/wiki/Network_scheduler "Network scheduler")  – [active queue management](https://en.wikipedia.org/wiki/Active_queue_management "Active queue management") which reorders or selectively drops network packets in the presence of congestion
- [Explicit Congestion Notification](https://en.wikipedia.org/wiki/Explicit_Congestion_Notification "Explicit Congestion Notification") – an extension to IP and TCP communications protocols that adds a flow control mechanism
- [TCP congestion control](https://en.wikipedia.org/wiki/TCP_congestion_control "TCP congestion control") – various implementations of efforts to deal with network congestion

The correct endpoint behavior is usually to repeat dropped information, but progressively slow the repetition rate. Provided all endpoints do this, the congestion lifts and the network resumes normal behavior. Other strategies such as [slow start](https://en.wikipedia.org/wiki/TCP_congestion_control#Slow_start "TCP congestion control") ensure that new connections don't overwhelm the router before congestion detection initiates.

Common router congestion avoidance mechanisms include [fair queuing](https://en.wikipedia.org/wiki/Fair_queuing "Fair queuing") and other [scheduling algorithms](https://en.wikipedia.org/wiki/Scheduling_algorithms "Scheduling algorithms"), and [random early detection](https://en.wikipedia.org/wiki/Random_early_detection "Random early detection") (RED) where packets are randomly dropped as congestion is detected. This proactively triggers the endpoints to slow transmission before congestion collapse occurs.

Some end-to-end protocols are designed to behave well under congested conditions; TCP is a well known example. The first TCP implementations to handle congestion were described in 1984,[^8] but Van Jacobson's inclusion of an open source solution in the Berkeley Standard Distribution UNIX (" [BSD](https://en.wikipedia.org/wiki/BSD "BSD") ") in 1988 first provided good behavior.

[UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol "User Datagram Protocol") does not control congestion. Protocols built atop UDP must handle congestion independently. Protocols that transmit at a fixed rate, independent of congestion, can be problematic. Real-time streaming protocols, including many [Voice over IP](https://en.wikipedia.org/wiki/Voice_over_IP "Voice over IP") protocols, have this property. Thus, special measures, such as quality of service, must be taken to keep packets from being dropped in the presence of congestion.

[Connection-oriented protocols](https://en.wikipedia.org/wiki/Connection-oriented_communication "Connection-oriented communication"), such as the widely used TCP protocol, watch for [packet loss](https://en.wikipedia.org/wiki/Packet_loss "Packet loss") or [queuing delay](https://en.wikipedia.org/wiki/Queuing_delay "Queuing delay") to adjust their transmission rate. Various network congestion avoidance processes support different trade-offs.[^9]

The [TCP congestion avoidance algorithm](https://en.wikipedia.org/wiki/TCP_congestion_avoidance_algorithm "TCP congestion avoidance algorithm") is the primary basis for congestion control on the Internet.[^10] [^11] [^12] [^13] [^14]

Problems occur when concurrent TCP flows experience [tail-drops](https://en.wikipedia.org/wiki/Tail-drop "Tail-drop"), especially when [bufferbloat](https://en.wikipedia.org/wiki/Bufferbloat "Bufferbloat") is present. This delayed packet loss interferes with TCP's automatic congestion avoidance. All flows that experience this packet loss begin a TCP retrain at the same moment – this is called [TCP global synchronization](https://en.wikipedia.org/wiki/TCP_global_synchronization "TCP global synchronization").

[Active queue management](https://en.wikipedia.org/wiki/Active_queue_management "Active queue management") (AQM) is the reordering or dropping of network packets inside a transmit buffer that is associated with a [network interface controller](https://en.wikipedia.org/wiki/Network_interface_controller "Network interface controller") (NIC). This task is performed by the [network scheduler](https://en.wikipedia.org/wiki/Network_scheduler "Network scheduler").

One solution is to use [random early detection](https://en.wikipedia.org/wiki/Random_early_detection "Random early detection") (RED) on the network equipment's egress queue.[^15] [^16] On [networking hardware](https://en.wikipedia.org/wiki/Networking_hardware "Networking hardware") ports with more than one egress queue, [weighted random early detection](https://en.wikipedia.org/wiki/Weighted_random_early_detection "Weighted random early detection") (WRED) can be used.

RED indirectly signals TCP sender and receiver by dropping some packets, e.g. when the average queue length is more than a threshold (e.g. 50%) and deletes [linearly](https://en.wikipedia.org/wiki/Linear "Linear") or [cubically](https://en.wikipedia.org/wiki/Cubic_function "Cubic function") more packets,[^17] up to e.g. 100%, as the queue fills further.

The [robust random early detection](https://en.wikipedia.org/wiki/Robust_random_early_detection "Robust random early detection") (RRED) algorithm was proposed to improve the TCP throughput against denial-of-service (DoS) attacks, particularly low-rate denial-of-service (LDoS) attacks. Experiments confirmed that RED-like algorithms were vulnerable under LDoS attacks due to the oscillating TCP queue size caused by the attacks.[^18]

#### Flow-based WRED

Some network equipment is equipped with ports that can follow and measure each flow and are thereby able to signal a too big bandwidth flow according to some quality of service policy. A policy could then divide the bandwidth among all flows by some criteria.[^19]

Another approach is to use [Explicit Congestion Notification](https://en.wikipedia.org/wiki/Explicit_Congestion_Notification "Explicit Congestion Notification") (ECN).[^20] ECN is used only when two hosts signal that they want to use it. With this method, a protocol bit is used to signal explicit congestion. This is better than the indirect congestion notification signaled by packet loss by the RED/WRED algorithms, but it requires support by both hosts.[^21] [^15]

When a router receives a packet marked as ECN-capable and the router anticipates congestion, it sets the ECN flag, notifying the sender of congestion. The sender should respond by decreasing its transmission bandwidth, e.g., by decreasing its sending rate by reducing the TCP window size or by other means.

The [L4S](https://en.wikipedia.org/wiki/L4S "L4S") protocol is an enhanced version of ECN which allows senders to collaborate with network devices to control congestion.[^22]

Congestion avoidance can be achieved efficiently by reducing traffic. When an application requests a large file, graphic or web page, it usually advertises a *window* of between 32K and 64K. This results in the server sending a full window of data (assuming the file is larger than the window). When many applications simultaneously request downloads, this data can create a congestion point at an upstream provider. By reducing the window advertisement, the remote servers send less data, thus reducing the congestion.[^23] [^24]

#### Backward ECN

Backward ECN (BECN) is another proposed congestion notification mechanism. It uses [ICMP source quench](https://en.wikipedia.org/wiki/ICMP_source_quench "ICMP source quench") messages as an IP signaling mechanism to implement a basic ECN mechanism for IP networks, keeping congestion notifications at the IP level and requiring no negotiation between network endpoints. Effective congestion notifications can be propagated to transport layer protocols, such as TCP and UDP, for the appropriate adjustments.[^25]

### Radio links

The protocols that avoid congestive collapse generally assume that data loss is caused by congestion. On wired networks, errors during transmission are rare. [WiFi](https://en.wikipedia.org/wiki/WiFi "WiFi"), [3G](https://en.wikipedia.org/wiki/3G "3G") and other networks with a radio layer are susceptible to data loss due to interference and may experience poor throughput in some cases. The TCP connections running over a radio-based [physical layer](https://en.wikipedia.org/wiki/Physical_layer "Physical layer") see the data loss and tend to erroneously believe that congestion is occurring.

### Short-lived connections

The slow-start protocol performs badly for short connections. Older [web browsers](https://en.wikipedia.org/wiki/Web_browser "Web browser") created many short-lived connections and opened and closed the connection for each file. This kept most connections in the slow start mode. Initial performance can be poor, and many connections never get out of the slow-start regime, significantly increasing latency. To avoid this problem, modern browsers either open multiple connections simultaneously or [reuse one connection](https://en.wikipedia.org/wiki/HTTP_persistent_connections "HTTP persistent connections") for all files requested from a particular server.

## Admission control

[Admission control](https://en.wikipedia.org/wiki/Admission_control "Admission control") is any system that requires devices to receive permission before establishing new network connections. If the new connection risks creating congestion, permission can be denied. Examples include Contention-Free Transmission Opportunities (CFTXOPs) in the ITU-T [G.hn](https://en.wikipedia.org/wiki/G.hn "G.hn") standard for home networking over legacy wiring, [Resource Reservation Protocol](https://en.wikipedia.org/wiki/Resource_Reservation_Protocol "Resource Reservation Protocol") for IP networks and [Stream Reservation Protocol](https://en.wikipedia.org/wiki/Stream_Reservation_Protocol "Stream Reservation Protocol") for [Ethernet](https://en.wikipedia.org/wiki/Ethernet "Ethernet").

## See also

- [Bandwidth management](https://en.wikipedia.org/wiki/Bandwidth_management "Bandwidth management") – Capacity control on a communications network
- [Cascading failure](https://en.wikipedia.org/wiki/Cascading_failure "Cascading failure") – Systemic risk of failure
- [Choke exchange](https://en.wikipedia.org/wiki/Choke_exchange "Choke exchange") – Telephone exchange designed to handle many simultaneous call attempts
- [Erlang (unit)](https://en.wikipedia.org/wiki/Erlang_\(unit\) "Erlang (unit)") – Load measure in telecommunications
- [Sorcerer's Apprentice syndrome](https://en.wikipedia.org/wiki/Sorcerer%27s_Apprentice_syndrome "Sorcerer's Apprentice syndrome") – Network protocol flaw in the original versions of TFTP
- [Teletraffic engineering](https://en.wikipedia.org/wiki/Teletraffic_engineering "Teletraffic engineering") – Application of traffic engineering theory to telecommunications
- [Thrashing](https://en.wikipedia.org/wiki/Thrashing_\(computer_science\) "Thrashing (computer science)") – Constant exchange between memory and storage
- [Traffic shaping](https://en.wikipedia.org/wiki/Traffic_shaping "Traffic shaping") – Communication bandwidth management technique
- [Reliability (computer networking)](https://en.wikipedia.org/wiki/Reliability_\(computer_networking\) "Reliability (computer networking)") – Protocol acknowledgement capability

## References

## External links

- Floyd, S. and K. Fall, *[Promoting the Use of End-to-End Congestion Control in the Internet](http://www.aciri.org/floyd/end2end-paper.html)* (IEEE/ACM Transactions on Networking, August 1999)
- Sally Floyd, *[On the Evolution of End-to-end Congestion Control in the Internet: An Idiosyncratic View](http://www.ima.umn.edu/talks/workshops/10-22-24.99/floyd/floyd.pdf)* (IMA Workshop on Scaling Phenomena in Communication Networks, October 1999) (*[pdf](https://en.wikipedia.org/wiki/Pdf "Pdf") format*)
- [Linktionary term: Queuing](http://www.linktionary.com/q/queuing.html) [Archived](https://web.archive.org/web/20030308154423/http://www.linktionary.com/q/queuing.html) 2003-03-08 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine")
- [Pierre-Francois Quet, Sriram Chellappan, Arjan Durresi, Mukundan Sridharan, Hitay Ozbay, Raj Jain, "Guidelines for optimizing Multi-Level ECN, using fluid flow based TCP model"](https://www.cse.wustl.edu/~jain/papers/mecn_cth.htm)
- [Sally Floyd, Ratul Mahajan, David Wetherall: RED-PD: RED with Preferential Dropping](http://www.cs.washington.edu/homes/ratul/red-pd/) [Archived](https://web.archive.org/web/20030402201326/http://www.cs.washington.edu/homes/ratul/red-pd/) 2003-04-02 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine")
- [A Generic Simple RED Simulator for educational purposes by Mehmet Suzen](https://code.google.com/p/guduz/)
- [Approaches to Congestion Control in Packet Networks](https://web.archive.org/web/20140221123729/http://utopia.duth.gr/~emamatas/jie2007.pdf)
- [Papers in Congestion Control](https://web.archive.org/web/20100611055219/http://www.ecse.rpi.edu/Homepages/shivkuma/research/cong-papers.html)
- [Random Early Detection Homepage](http://www.icir.org/floyd/red.html)
- [Explicit Congestion Notification Homepage](http://www.icir.org/floyd/ecn.html)
- [TFRC Homepage](http://www.icir.org/tfrc/)
- [AIMD-FC Homepage](https://web.archive.org/web/20090113204941/http://www.ccs.neu.edu/home/ladrian/abstract/aimdfc.html)
- [Recent Publications in low-rate denial-of-service (DoS) attacks](https://sites.google.com/site/cwzhangres/home/posts/recentpublicationsinlow-ratedosattacks)

[^1]: (Al-Bahadili, 2012, p. 282) Al-Bahadili, H. (2012). [Simulation in computer network design and modeling: Use and analysis](https://books.google.com/books?id=uNlplf2C03QC&dq=network+congestion+occurs+when+a+link+or+node+is+carrying+so+much+data+that+its+quality+of+service+deteriorates.&pg=PA282). Hershey, PA: IGI Global.

[^2]: den Hartog, F., Raschella, A., Bouhafs, F., Kempker, P., Boltjes, B., & Seyedebrahimi, M. (2017, November). [A Pathway to solving the Wi-Fi Tragedy of the Commons in apartment blocks](http://unsworks.unsw.edu.au/fapi/datastream/unsworks:50254/bin458a10d9-f568-479c-a9b5-5c185ef64e78?view=true). In 2017 27th International Telecommunication Networks and Applications Conference (ITNAC) (pp. 1-6). IEEE.

[^3]: [RFC](https://en.wikipedia.org/wiki/RFC_\(identifier\) "RFC (identifier)") [896](https://www.rfc-editor.org/rfc/rfc896)

[^4]: Fall, K.R.; Stevens, W.R. (2011). [*TCP/IP Illustrated, Volume 1: The Protocols*](https://books.google.com/books?id=a23OAn5i8R0C) (2 ed.). Pearson Education. p. 739. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780132808187](https://en.wikipedia.org/wiki/Special:BookSources/9780132808187 "Special:BookSources/9780132808187").

[^5]: Van Jacobson; Michael J. Karels (November 1988), [*Congestion Avoidance and Control*](https://ee.lbl.gov/papers/congavoid.pdf) (PDF), In October of '86, the Internet had the first of what became a series of 'congestion collapses'. During this period, the data throughput from LBL to UC Berkeley (sites separatedby 400 yards and two IMP hops) dropped from 32 Kbps to 40 bps. We were fascinated by this sudden factor-of-thousand drop in bandwidth and embarked on an investigation of why things had gotten so bad. In particular, we wondered if the 4.3BSD (Berkeley UNIX) TCP was mis-behaving or if it could be tuned to work better under abysmal network conditions.The answer to both of these questions was "yes".

[^6]: Hafner, Katie (4 September 2019). ["Sally Floyd, Who Helped Things Run Smoothly Online, Dies at 69"](https://www.nytimes.com/2019/09/04/science/sally-floyd-dead.html). *New York Times*. Retrieved 5 September 2019.

[^7]: Nanda, Priyadarsi (2000-11-01). ["A Control Theory Approach for Congestion Control in Intranetwork"](https://www.sciencedirect.com/science/article/pii/S1474667017367356). *IFAC Proceedings Volumes*. 16th IFAC Workshop on Distributed Computer Control Systems (DCCS 2000), Sydney, Australia, 29 November-1 December 2000. **33** (30): 91– 94. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/S1474-6670(17)36735-6](https://doi.org/10.1016%2FS1474-6670%2817%2936735-6). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1474-6670](https://search.worldcat.org/issn/1474-6670).

[^8]: Vinton G. Cerf; Robert E. Kahn (May 1974). ["A Protocol for Packet Network Intercommunication"](https://web.archive.org/web/20160304150203/http://ece.ut.ac.ir/Classpages/F84/PrincipleofNetworkDesign/Papers/CK74.pdf) (PDF). *IEEE Transactions on Communications*. **22** (5): 637– 648. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/tcom.1974.1092259](https://doi.org/10.1109%2Ftcom.1974.1092259). Archived from [the original](http://ece.ut.ac.ir/Classpages/F84/PrincipleofNetworkDesign/Papers/CK74.pdf) (PDF) on March 4, 2016.

[^9]: Lee, B.P.; Balan, R.K.; Jacob, L.; Seah, W.K.G.; Ananda, A.L. (2000), "TCP Tunnels: Avoiding Congestion Collapse", *Proceedings 25th Annual IEEE Conference on Local Computer Networks. LCN 2000*, pp. 408– 417, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/LCN.2000.891077](https://doi.org/10.1109%2FLCN.2000.891077), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-7695-0912-6](https://en.wikipedia.org/wiki/Special:BookSources/0-7695-0912-6 "Special:BookSources/0-7695-0912-6"), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [34447400](https://api.semanticscholar.org/CorpusID:34447400)

[^10]: [Van Jacobson](https://en.wikipedia.org/wiki/Van_Jacobson "Van Jacobson"), [Michael J. Karels](https://en.wikipedia.org/wiki/Michael_J._Karels "Michael J. Karels"). [Congestion Avoidance and Control](http://citeseer.ist.psu.edu/484335.html) (1988). *Proceedings of the Sigcomm '88 Symposium*, vol.18(4): pp.314–329. Stanford, CA. August, 1988. This paper originated many of the congestion avoidance algorithms used in TCP/IP.

[^11]: RFC 2001 - TCP Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery Algorithms

[^12]: RFC 2581 - TCP Congestion Control

[^13]: RFC 3390 - TCP Increasing TCP's Initial Window

[^14]: [TCP Congestion Avoidance Explained via a Sequence Diagram](http://www.eventhelix.com/RealtimeMantra/Networking/TCP_Congestion_Avoidance.pdf)

[^15]: [Sally Floyd: RED (Random Early Detection) Queue Management](http://www.icir.org/floyd/red.html)

[^16]: Sally Floyd, Van Jacobson. [Random Early Detection Gateways for Congestion Avoidance](http://citeseer.ist.psu.edu/462978.html) (1993). *IEEE/ACM Transactions on Networking*, vol.1(4): pp.397–413. Invented Random Early Detection (RED) gateways.

[^17]: *An Analytical RED Function Design Guaranteeing Stable System Behavior*, [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.105.5995](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.105.5995), ...The advantage of this function lies not only in avoiding heavy oscillations but also in avoiding link under-utilization at low loads. The applicability of the derived function is independent of the load range, no parameters are to be adjusted. Compared to the original linear drop function applicability is extended by far...Our example with realistic system parameters gives an approximation function of the cubic of the queue size...

[^18]: Zhang, Changwang; Yin, Jianping; Cai, Zhiping; Chen, Weifeng (2010). ["RRED: Robust RED Algorithm to Counter Low-rate Denial-of-Service Attacks"](https://sites.google.com/site/cwzhangres/home/files/RREDRobustREDAlgorithmtoCounterLow-rateDenial-of-ServiceAttacks.pdf?attredirects=0) (PDF). *IEEE Communications Letters*. **14** (5). [IEEE](https://en.wikipedia.org/wiki/IEEE "IEEE"): 489– 491. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/LCOMM.2010.05.091407](https://doi.org/10.1109%2FLCOMM.2010.05.091407). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [1121461](https://api.semanticscholar.org/CorpusID:1121461).

[^19]: ["Congestion Avoidance Overview"](https://www.cisco.com/c/en/us/td/docs/ios/qos/configuration/guide/12_2sr/qos_12_2sr_book/congestion_avoidance.html). [Cisco Systems](https://en.wikipedia.org/wiki/Cisco_Systems "Cisco Systems"). Retrieved 2020-08-07.

[^20]: RFC 3168 - The Addition of Explicit Congestion Notification (ECN) to IP

[^21]: [Comparative study of RED, ECN and TCP Rate Control (1999)](http://citeseer.ist.psu.edu/bagal99comparative.html)

[^22]: ["L4S"](https://www.bell-labs.com/research-innovation/projects-and-initiatives/l4s/). *Nokia Bell Labs*. 2023-06-14. Retrieved 2025-01-31.

[^23]: [*Generalized Window Advertising for TCP CongestionControl*](http://nrlweb.cs.ucla.edu/nrlweb/publication/download/162/2002-ett-0.pdf) (PDF), retrieved 2020-11-13

[^24]: Pop, O.; Moldován, I.; Simon, Cs.; Bíró, J.; Koike, A.; Ishii, H. (2000), "Advertised Window-Based TCP Flow Control in Routers", *Telecommunication Network Intelligence*, pp. 197– 218, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-0-387-35522-1\_12](https://doi.org/10.1007%2F978-0-387-35522-1_12), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4757-6693-6](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4757-6693-6 "Special:BookSources/978-1-4757-6693-6")

[^25]: [A proposal for Backward ECN for the Internet Protocol](http://tools.ietf.org/html/draft-salim-jhsbnns-ecn-00)