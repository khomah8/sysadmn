## sysadmn :specifically: App Technical {operational} Support / App Performance Monitoring [APM]

about devOps, etc. and #app-monitoring-task #app-monitoring-tools #app-monitoring-framework #app-moinitoring-solution #app-performance-monitoring ... 

### [search hits of products/tools]

https://webapplicationmonitoring.net/

https://smartbear.com/learn/performance-monitoring/why-you-should-be-monitoring/

https://www.atlassian.com/software/opsgenie

https://sentry.io/for/performance/

https://www.nagios.com/solutions/web-application-monitoring/

https://www.pingdom.com/blog/best-practices-for-web-app-monitoring/

## [APM-related comparison] 
https://www.google.com/search?q=New+Relic%2C+Dynatrace%2C+AppDynamics 

1. https://coralogix.com/log-analytics-blog/apm-comparison/
2. https://crozdesk.com/it/application-performance-monitoring-apm-software, https://crozdesk.com/compare/appdynamics-vs-dynatrace-vs-new-relic 
3. 

### cornerstone/key terms : 
- APM as application performance management/monitoring tools 

- measuring-of : 1) user eXperience; 2) resources usage; 

- dashboard 

- score index (apdex IDX as [ SAtisfied T ; TOlerating 1' < T < 4': FRustrated T > 4' ] for new reLiCt; )

- [index] baseline 

- [system] health issues 

- New Relic is a SaaS platform, while AppDynamics and Dynatrace offer [full SaaS, on-prem, and hybrid installation options] 

- Root Cause analysis


## [centralized logs solutions] 
### (SPLUNK, Logz.IO, Logstash, etc.) {ELK Stack, Grafana, Kafka, Graphite, etc. too}
[**Elasticsearch**](https://logz.io/tag/elasticsearch/) is NoSQL database that uses the _Lucene search engine_. [**Logstash**](https://logz.io/tag/logstash/) is a data processing and transportation pipeline used to populate Elasticsearch with the data (though also it supports other destinations including Graphite, Kafka, Nagios and RabbitMQ). [**Kibana**](https://logz.io/tag/kibana/) is a dashboard that works on top of Elasticsearch. 

ELK Stack was a collection of three **open-source products** — **E**lasticsearch, **L**ogstash, and **K**ibana — all developed, managed and maintained by [Elastic](https://www.elastic.co/). The introduction and subsequent addition of **Beats** turned the stack into a four legged project and led to a renaming of the stack as the **Elastic Stack**.

* [SPLUNK](https://www.splunk.com)  { forwarder --> indexer --> search head }
* [Logz.io](https://logz.io)  [as platform for ELK] 
* Logstash https://github.com/elastic/logstash 


https://www.google.com/search?q=SPLUNK%2C+Logz.IO%2C+Logstash 
### some comparison 
- https://stackshare.io/stackups/logz-io-vs-splunk-enterprise-vs-logstash
- https://devops.com/splunk-elk-stack-side-side-comparison/
