## App Perf Monitoring 

### related terms\ tools 
- NoSQL database : 
> "non-relational" DB provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases [wiki](https://en.wikipedia.org/wiki/NoSQL) 

> https://www.mongodb.com/nosql-explained 

> https://www.trustradius.com/nosql-databases

- REST (API) : REpresentational State Transfer 
> software architectural style that defines a set of constraints to be used for creating Web services [wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)

> eng [Introduction to REST API - RESTful Web Services @Nov 14, 2019](https://www.springboottutorial.com/introduction-to-rest-api) / rus [Введение в REST API — RESTful веб-сервисы](https://habr.com/ru/post/483202/)

- JSON (objects / documents) : (JavaScript Object Notation) 
> an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value) [wiki](https://en.wikipedia.org/wiki/JSON)

> https://www.json.org/json-en.html

> https://jsonapi.org/ 

> https://www.w3schools.com/js/js_json_intro.asp { with live [script examples](https://www.w3schools.com/js/tryit.asp?filename=tryjson_receive) }

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON 

> [ECMAScript&reg; 2021 Language Specification](https://tc39.es/ecma262/)

- PRTG Network Monitor : [wiki](https://en.wikipedia.org/wiki/PRTG_Network_Monitor) 
> **Paessler Router Traffic Grapher until version 7** is an agentless network monitoring software from Paessler AG. PRTG 100 is available for both personal and commercial use for free, but is limited to monitoring 100 sensors. If you want to monitor more sensors, you need one of the Commercial Editions. Our licensing model is based on the number of sensors and core server installations.  

> https://www.paessler.com/manuals/prtg/introduction_monitoring_with_prtg 

- Security concerns

> https://learn.javascript.ru/csrf

> https://duo.com/docs/radius

> https://www.watchguard.com/help/docs/help-center/en-US/Content/Integration-Guides/General/duo-security-authentication.html 

- HTTP connection
  - The __persistent network connection__ allows the client and server to send/receive multiple HTTP requests/responses without opening a new connection for every single request/response pair.
  - Persistent connections _can improve overall system performance_ by eliminating the need to send additional TCP/IP packets for establishing and closing the network connection before/after each request.
  - The connection is __persistent by default for HTTP/1.1__ clients. _For HTTP/1.0 connections_, you need to explicitly indicate that you want a persistent connection by adding the _"Connection: keep-alive" header_.
  
> https://reqbin.com/Article/Connection

> https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive
