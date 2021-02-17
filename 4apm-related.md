# App Perf Monitoring, related terms & tools 

- NoSQL database : 
> "non-relational" DB provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases [wiki](https://en.wikipedia.org/wiki/NoSQL) 

> https://www.mongodb.com/nosql-explained 

> https://www.trustradius.com/nosql-databases

## REST (API) : REpresentational State Transfer 
> software architectural style that defines a set of constraints to be used for creating Web services [wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)

> eng [Introduction to REST API - RESTful Web Services @Nov 14, 2019](https://www.springboottutorial.com/introduction-to-rest-api) / rus [Введение в REST API — RESTful веб-сервисы](https://habr.com/ru/post/483202/)

### HTTP connection explained:
  - The _persistent network connection_ allows the client and server to send/receive multiple HTTP requests/responses without opening a new connection for every single request/response pair.
  - Persistent connections _can improve overall system performance_ by eliminating the need to send additional TCP/IP packets for establishing and closing the network connection before/after each request.
  - The connection is _persistent by default for HTTP/1.1__ clients. _For HTTP/1.0 connections_, you need to explicitly indicate that you want a persistent connection by adding the `"Connection: keep-alive"` header.
  - A client can inform the server that it doesn't need a persistent connection by sending the `"Connection: close"` header, thereby freeing up server resources. For example, if the client does not plan to send more than one request to this server.
  - If the server _does not support persistent connections or cannot provide_ a persistent connection at this time, it can indicate this by sending the `"Connection: close"` _header in the response_.

[try `Keep-Alive` connection](https://reqbin.com/req/4sa9kqvu); [try `Close` connection](https://reqbin.com/req/84xntxmp) 
  
> https://reqbin.com/Article/Connection

> https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive

### JSON (objects / documents) : (JavaScript Object Notation) 
> an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value) [wiki](https://en.wikipedia.org/wiki/JSON)

> https://www.json.org/json-en.html

> https://jsonapi.org/ 

> https://www.w3schools.com/js/js_json_intro.asp { with live [script examples](https://www.w3schools.com/js/tryit.asp?filename=tryjson_receive) }

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON 

> [ECMAScript&reg; 2021 Language Specification](https://tc39.es/ecma262/)

### Virtualization on OS level \ Containerization : [wiki](https://uk.wikipedia.org/wiki/%D0%92%D1%96%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F_%D0%BD%D0%B0_%D1%80%D1%96%D0%B2%D0%BD%D1%96_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D1%96%D0%B9%D0%BD%D0%BE%D1%97_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B8)

> https://habr.com/ru/company/virtuozzo/blog/319998/
> https://gigacloud.ua/blog/navchannja/chomu-kontejneri-ce-majbutne-virtualizacii
> https://www.bigdataschool.ru/blog/containers-big-data.html
> https://docs.microsoft.com/ru-ru/virtualization/windowscontainers/about/containers-vs-vm

### PRTG Network Monitor : [wiki](https://en.wikipedia.org/wiki/PRTG_Network_Monitor) 

> __Paessler Router Traffic Grapher until version 7__ is an agentless network monitoring software from Paessler AG. PRTG 100 is available for both personal and commercial use for free, but is limited to monitoring 100 sensors. If you want to monitor more sensors, you need one of the Commercial Editions. Our licensing model is based on the number of sensors and core server installations.  

> https://www.paessler.com/manuals/prtg/introduction_monitoring_with_prtg 

### Apache Kafka : [wiki](https://en.wikipedia.org/wiki/Apache_Kafka); [GitHub](https://github.com/apache/kafka)

> Apache Kafka is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. Kafka can connect to external systems (for data import/export) via Kafka Connect and provides Kafka Streams, a Java stream processing library. Kafka uses a binary TCP-based protocol... 

> We can use Kafka as a __Message Queue or a Messaging System__ but as a distributed streaming platform Kafka has several other usages for stream processing or storing data. Messaging System: a __highly scalable, fault-tolerant and distributed Publish/Subscribe__ messaging system. 

> In short, Kafka is used for stream processing, __website activity tracking, metrics collection and monitoring, log aggregation, real-time analytics__, CEP, ingesting data into Spark, ingesting data into Hadoop, CQRS, replay messages, error recovery, and guaranteed distributed commit log for in-memory computing... 

> Kafka provides a __framework for storing, reading and analysing streaming data__... was originally created at LinkedIn, where it played a part in __analysing the connections between their millions of professional users__ in order to build networks between people.

> https://kafka.apache.org/documentation/

> https://dzone.com/articles/what-is-kafka

> https://www.cloudkarafka.com/blog/2016-11-30-part1-kafka-for-beginners-what-is-apache-kafka.html

> {from @ZinoviiYu} https://blog.newrelic.com/engineering/new-relic-kafkapocalypse/ 

## Security concerns

> https://learn.javascript.ru/csrf

> https://duo.com/docs/radius

> https://www.watchguard.com/help/docs/help-center/en-US/Content/Integration-Guides/General/duo-security-authentication.html 

### devOps / serviceOps (general)

> https://t.me/s/catops?

> https://www.youtube.com/watch?v=8eH3k4BxV6k&

> https://www.devops-research.com/research.html

