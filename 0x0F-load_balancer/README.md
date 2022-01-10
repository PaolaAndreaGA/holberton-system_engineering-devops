# What Is Load Balancing?

**Load balancing**  refers to efficiently distributing incoming network traffic across a group of backend servers, also known as a  _server farm_  or  _server pool_.

Modern high‑traffic websites must serve hundreds of thousands, if not millions, of concurrent requests from users or clients and return the correct text, images, video, or application data, all in a fast and reliable manner. To cost‑effectively scale to meet these high volumes, modern computing best practice generally requires adding more servers.

A  [load balancer](https://www.nginx.com/solutions/adc)  acts as the “traffic cop” sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance. If a single server goes down, the load balancer redirects traffic to the remaining online servers. When a new server is added to the server group, the load balancer automatically starts to send requests to it.

In this manner, a load balancer performs the following functions:

-   Distributes client requests or network load efficiently across multiple servers
-   Ensures high availability and reliability by sending requests only to servers that are online
-   Provides the flexibility to add or subtract servers as demand dictates

![load balancing diagram](https://www.nginx.com/wp-content/uploads/2014/07/what-is-load-balancing-diagram-NGINX-1024x518.png)

load balancing diagram

### Load Balancing Algorithms

Different load balancing algorithms provide different benefits; the choice of load balancing method depends on your needs:

-   **Round Robin** – Requests are distributed across the group of servers sequentially.
-   **Least Connections** – A new request is sent to the server with the fewest current connections to clients. The relative computing capacity of each server is factored into determining which one has the least connections.
-   **Least Time**  – Sends requests to the server selected by a formula that combines the
    fastest response time and fewest active connections. Exclusive to NGINX Plus.
    -   **Hash**  – Distributes requests based on a key you define, such as the client IP address or
        the request URL. NGINX Plus can optionally apply a consistent hash to minimize redistribution
	    of loads if the set of upstream servers changes.
	    -   **IP Hash** – The IP address of the client is used to determine which server receives the request.
	    -   **Random with Two Choices**  – Picks two servers at random and sends the request to the
	        one that is selected by then applying the Least Connections algorithm (or for NGINX Plus
		    the Least Time algorithm, if so configured).

## Benefits of Load Balancing

-   Reduced downtime
-   Scalable
-   Redundancy
-   Flexibility
-   Efficiency

## Related Topics

### Session Persistence

Information about a user’s session is often stored locally in the browser. For example, in a shopping cart application the items in a user’s cart might be stored at the browser level until the user is ready to purchase them. Changing which server receives requests from that client in the middle of the shopping session can cause performance issues or outright transaction failure. In such cases, it is essential that all requests from a client are sent to the same server for the duration of the session. This is known as  _session persistence_.

The best  [load balancers](https://www.nginx.com/solutions/adc/)  can handle session persistence as needed. Another use case for session persistence is when an upstream server stores information requested by a user in its cache to boost performance. Switching servers would cause that information to be fetched for the second time, creating performance inefficiencies.

### Dynamic Configuration of Server Groups

Many fast‑changing applications require new servers to be added or taken down on a constant basis. This is common in environments such as the  [Amazon Web Services](https://www.nginx.com/partners/amazon-web-services/)  (AWS) Elastic Compute Cloud (EC2), which enables users to pay only for the computing capacity they actually use, while at the same time ensuring that capacity scales up in response traffic spikes. In such environments it greatly helps if the load balancer can dynamically add or remove servers from the group without interrupting existing connections.

### Hardware vs. Software Load Balancing

Load balancers typically come in two flavors: hardware‑based and software‑based. Vendors of hardware‑based solutions load proprietary software onto the machine they provide, which often uses specialized processors. To cope with increasing traffic at your website, you have to buy more or bigger machines from the vendor. Software solutions generally run on commodity hardware, making them less expensive and more flexible. You can install the software on the hardware of your choice or in cloud environments like AWS EC2.

### Seven-Layer Open System Interconnection (OSI)

Load balancing can be performed at various layers in the Open Systems Interconnection (OSI) Reference Model for networking.

Layer 7 load balancing is more CPU‑intensive than packet‑based Layer 4 load balancing, but rarely causes degraded performance on a modern server. Layer 7 load balancing enables the load balancer to make smarter load‑balancing decisions, and to apply optimizations and changes to the content.

For more information about load balancing, see .

## How Can NGINX Plus Help?

[NGINX Plus](https://www.nginx.com/products/nginx/)  and  [NGINX](https://nginx.org/en)  are the  best-in-class  load‑balancing solutions used by high‑traffic websites such as Dropbox, Netflix, and Zynga. More than  [400 million  websites](https://news.netcraft.com/archives/category/web-server-survey/)  worldwide rely on NGINX Plus and NGINX Open Source to deliver their content quickly, reliably, and securely.

As a software‑based load balancer, NGINX Plus is much less expensive than hardware‑based solutions with similar capabilities. The comprehensive load balancing capabilities in NGINX Plus enable you to build a highly optimized application delivery network.

When you insert NGINX Plus as a load balancer in front of your application and web server farms, it increases your website’s efficiency, performance, and reliability. NGINX Plus helps you maximize both customer satisfaction and the return on your IT investments.

## Related Content

-   [What Is Cloud Load Balancing?](https://www.nginx.com/resources/glossary/cloud-load-balancing)
-   [What Is DNS Load Balancing?](https://www.nginx.com/resources/glossary/dns-load-balancing/)
-   [What Is Global Server Load Balancing?](https://www.nginx.com/resources/glossary/global-server-load-balancing/)
-   [What is HTTP?](https://www.nginx.com/resources/glossary/http)
-   [What Is Hybrid Load Balancing?](https://www.nginx.com/resources/glossary/hybrid-load-balancing/)
-   [What Is Layer 4 Load Balancing?](https://www.nginx.com/resources/glossary/layer-4-load-balancing/)
-   [What Is Layer 7 Load Balancing?](https://www.nginx.com/resources/glossary/layer-7-load-balancing/)
-   [What Is a Network Load Balancer?](https://www.nginx.com/resources/glossary/network-load-balancer/)
-   [What Is Round‑Robin Load Balancing?](https://www.nginx.com/resources/glossary/round-robin-load-balancing/)
-   [What Is an SSL Load Balancer??](https://www.nginx.com/resources/glossary/ssl-load-balancer/)
-   [High‑Performance Load Balancing](https://www.nginx.com/products/nginx/load-balancing)  with NGINX Plus
-   [Load Balancer](https://docs.nginx.com/nginx/admin-guide/load-balancer)  in the NGINX Plus Admin Guide
-   [NGINX Plus Customer Success Stories](https://www.nginx.com/success-stories/solutions/load-balancer-application-delivery/)

#### Resources

-   [Load balancing (computing)](https://en.wikipedia.org/wiki/Load_balancing_(computing))  on Wikipedia
-   [What Is Load Balancing?](https://www.youtube.com/watch?