# App Perf Monitoring, related terms & tools 

## REST (API) : REpresentational State Transfer 
- software architectural style that defines a set of constraints to be used for creating Web services [wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
- eng [Introduction to REST API - RESTful Web Services @Nov 14, 2019](https://www.springboottutorial.com/introduction-to-rest-api) / rus [Введение в REST API — RESTful веб-сервисы](https://habr.com/ru/post/483202/)

### HTTP connection explained:
  - The _persistent network connection_ allows the client and server to send/receive multiple HTTP requests/responses without opening a new connection for every single request/response pair.
  - Persistent connections _can improve overall system performance_ by eliminating the need to send additional TCP/IP packets for establishing and closing the network connection before/after each request.
  - The connection is _persistent by default for HTTP/1.1__ clients. _For HTTP/1.0 connections_, you need to explicitly indicate that you want a persistent connection by adding the `"Connection: keep-alive"` header.
  - A client can inform the server that it doesn't need a persistent connection by sending the `"Connection: close"` header, thereby freeing up server resources. For example, if the client does not plan to send more than one request to this server.
  - If the server _does not support persistent connections or cannot provide_ a persistent connection at this time, it can indicate this by sending the `"Connection: close"` _header in the response_.

[try `Keep-Alive` connection](https://reqbin.com/req/4sa9kqvu); [try `Close` connection](https://reqbin.com/req/84xntxmp) 
- https://reqbin.com/Article/Connection
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive

### JSON (objects / documents) : (JavaScript Object Notation) 
> an open standard file format, and data interchange format, uses human-readable text to store and transmit data objects consisting of `attribute–value pairs` and `array data` types (or any other serializable value) [wiki](https://en.wikipedia.org/wiki/JSON)
- https://www.json.org/json-en.html
- https://jsonapi.org/ 
- https://www.w3schools.com/js/js_json_intro.asp { with live [script examples](https://www.w3schools.com/js/tryit.asp?filename=tryjson_receive) }
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON 
- [ECMAScript&reg; 2021 Language Specification](https://tc39.es/ecma262/)

### YAML (language) : (a recursive acronym for "YAML Ain't Markup Language") 
> human-readable data-serialization language, commonly used for configuration files and in applications... targets many of the same communications applications as XML... uses both `Python-style indentation` to indicate nesting, and a more compact format - so that `JSON files are valid YAML 1.2`. 
> is simply a data-representation language,.. integration with other languages allows `Perl parsers`, for example, which can execute Perl code. [wiki](https://en.wikipedia.org/wiki/YAML)
- https://yaml.org/spec/
- https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started/
- https://blog.stackpath.com/yaml/

## Virtualization on OS level \ Containerization : [wiki](https://uk.wikipedia.org/wiki/%D0%92%D1%96%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F_%D0%BD%D0%B0_%D1%80%D1%96%D0%B2%D0%BD%D1%96_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D1%96%D0%B9%D0%BD%D0%BE%D1%97_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B8)
- https://habr.com/ru/company/virtuozzo/blog/319998/
- https://gigacloud.ua/blog/navchannja/chomu-kontejneri-ce-majbutne-virtualizacii
- https://www.bigdataschool.ru/blog/containers-big-data.html
- https://docs.microsoft.com/ru-ru/virtualization/windowscontainers/about/containers-vs-vm
- youtube 
    - "Виртуализация или контейнеры ? В чем разница ?"  https://www.youtube.com/watch?v=NWhc96LbDME --> https://system-admins.ru/teoriya-primery-virtualizacii/ 
    - Контейнерная виртуализация в Linux - YouTube  https://www.youtube.com/watch?v=rJRLZfk3a8U
    - "007. Виртуализация и контейнеризация" - Антон Конвалюк - YouTube  https://www.youtube.com/watch?v=YsQAAaNpw6Y
- NGINX Ingress Controller - NGINX   https://www.nginx.com/products/nginx-ingress-controller/
- How it works - NGINX Ingress Controller  https://kubernetes.github.io/ingress-nginx/how-it-works/

### Apache Kafka : [wiki](https://en.wikipedia.org/wiki/Apache_Kafka); [GitHub](https://github.com/apache/kafka)
> Apache Kafka is an open-source stream-processing software platform developed by the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. Kafka can connect to external systems (for data import/export) via Kafka Connect and provides Kafka Streams, a Java stream processing library. Kafka uses a binary TCP-based protocol... 
> We can use Kafka as a __Message Queue or a Messaging System__ but as a distributed streaming platform Kafka has several other usages for stream processing or storing data. Messaging System: a __highly scalable, fault-tolerant and distributed Publish/Subscribe__ messaging system. 
> In short, Kafka is used for stream processing, __website activity tracking, metrics collection and monitoring, log aggregation, real-time analytics__, CEP, ingesting data into Spark, ingesting data into Hadoop, CQRS, replay messages, error recovery, and guaranteed distributed commit log for in-memory computing... 
> Kafka provides a __framework for storing, reading and analysing streaming data__... was originally created at LinkedIn, where it played a part in __analysing the connections between their millions of professional users__ in order to build networks between people.
- https://kafka.apache.org/documentation/
- https://dzone.com/articles/what-is-kafka
- https://www.cloudkarafka.com/blog/2016-11-30-part1-kafka-for-beginners-what-is-apache-kafka.html
- {from @ZinoviiYu} https://blog.newrelic.com/engineering/new-relic-kafkapocalypse/ 

### Microsoft Message Queuing, MSMQ : [wiki](https://en.wikipedia.org/wiki/Microsoft_Message_Queuing) 
- https://docs.microsoft.com/en-us/previous-versions/ms834460(v=msdn.10)

### NoSQL database : 
> "non-relational" DB provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases [wiki](https://en.wikipedia.org/wiki/NoSQL) 
- https://www.mongodb.com/nosql-explained 
- https://www.trustradius.com/nosql-databases

### PRTG Network Monitor : [wiki](https://en.wikipedia.org/wiki/PRTG_Network_Monitor) 

> __Paessler Router Traffic Grapher until version 7__ is an agentless network monitoring software from Paessler AG. PRTG 100 is available for both personal and commercial use for free, but is limited to monitoring 100 sensors. If you want to monitor more sensors, you need one of the Commercial Editions. Our licensing model is based on the number of sensors and core server installations.  
- https://www.paessler.com/manuals/prtg/introduction_monitoring_with_prtg 
- https://kb.paessler.com/en/topic/66113-how-can-prtg-send-notifications-to-slack (integration with #Slack)

### Pagerduty (vs Victorops) vs Opsgenie 
- [PagerDuty vs Opsgenie | Why PagerDuty?](https://www.pagerduty.com/vs/opsgenie/)
- [Opsgenie vs. PagerDuty | Alternative to PagerDuty](https://www.atlassian.com/software/opsgenie/comparison/pagerduty)
- [Why VictorOps is the DevOps Alternative to Opsgenie | VictorOps](https://victorops.com/opsgenie-alternative/)
- https://www.reddit.com/r/devops/comments/g34drp/pagerduty_vs_victorops_vs_opsgenie/
- [OpsGenie vs PagerDuty | What are the differences?](https://stackshare.io/stackups/opsgenie-vs-pagerduty#:~:text=OpsGenie%20is%20a%20cloud%2Dbased,call%20schedule%20management%2C%20and%20escalations.&text=PagerDuty%20is%20an%20alarm%20aggregation,system%20administrators%20and%20support%20teams.)
- [OpsGenie vs PagerDuty | TrustRadius](https://www.trustradius.com/compare-products/opsgenie-vs-pagerduty)
- [Which is better, PagerDuty, VictorOps, or OpsGenie? - Quora](https://www.quora.com/Which-is-better-PagerDuty-VictorOps-or-OpsGenie)
- [5 reasons why Zenduty is a great alternative to Opsgenie, Pagerduty, and VictorOps(O/P/V) | by Vishwa Krishnakumar | Zenduty | Medium](https://medium.com/zenduty/5-reasons-why-zenduty-is-a-great-alternative-to-opsgenie-pagerduty-and-victorops-o-p-v-9befbedddf8f)
- https://sourceforge.net/software/compare/Opsgenie-vs-PagerDuty/
- https://www.itcentralstation.com/products/comparisons/opsgenie_vs_pagerduty_vs_victorops

## Load Balancing / Availability / Robustness / Scaling concenrns
- How to Use HAProxy for Load Balancing | Linode  https://www.linode.com/docs/guides/how-to-use-haproxy-for-load-balancing/
- HAProxy - The Reliable, High Performance TCP/HTTP Load Balancer  http://www.haproxy.org/

## Security concerns
- https://learn.javascript.ru/csrf
- https://duo.com/docs/radius
- https://www.watchguard.com/help/docs/help-center/en-US/Content/Integration-Guides/General/duo-security-authentication.html 
- https://en.wikipedia.org/wiki/Nessus_(software) 
- https://www.varonis.com/blog/what-is-siem/ 

### devOps / serviceOps (general)
- https://t.me/s/catops
- https://www.youtube.com/watch?v=8eH3k4BxV6k&
- https://www.devops-research.com/research.html
- https://system-admins.ru/devops-engineer/
- https://en.wikipedia.org/wiki/Azure_DevOps_Server#:~:text=formerly%20Team%20Foundation%20Server%20(TFS 
- SRE (concept): { 
  - https://en.wikipedia.org/wiki/Site_reliability_engineering: { 

__SRE satisfies `the DevOps [five] pillars` as follows:__
1) Reduce `organizational silos`
    - SRE shares ownership with developers to create shared responsibility
    - SREs use the same tools that developers use, and vice versa
2) Accept `failure as normal`
    - SREs embrace risk[6]
    - SRE quantifies failure and availability in a prescriptive manner using [Service Level Indicators](https://en.wikipedia.org/wiki/Service_Level_Indicator) (SLIs) and [Service Level Objectives](https://en.wikipedia.org/wiki/Service-level_objective) (SLOs)
    - SRE mandates blameless post mortems
3) Implement `gradual changes`
    - SRE encourages developers and product owners to move quickly by reducing the cost of failure
4) Leverage `tooling and automation`
    - SREs have a charter to automate manual tasks (called "toil") away 
5) `Measure everything`
    - SRE defines prescriptive ways to measure values
    - SRE fundamentally believes that systems operation is a software problem 

    }

    - https://sre.google/
    - https://www.redhat.com/en/topics/devops/what-is-sre#
    - https://www.overops.com/blog/devops-vs-sre-whats-the-difference-between-them-and-which-one-are-you/ {2018}
    - https://www.atlassian.com/incident-management/devops/sre
    - https://victorops.com/blog/site-reliability-engineer-sre-roles-and-responsibilities {2019}

}
