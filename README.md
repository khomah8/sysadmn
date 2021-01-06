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

### cornerstone/key terms : 
- APM as application performance management/monitoring tools 

- measuring-of : 1) user eXperience; 2) resources usage; 

- dashboard 

- score index (apdex IDX as [ SAtisfied T ; TOlerating 1' < T < 4': FRustrated T > 4' ] for new reLiCt; )

- [index] baseline 

- [system] health issues 

- New Relic is a SaaS platform, while AppDynamics and Dynatrace offer [full SaaS, on-prem, and hybrid installation options] 

- Root Cause analysis


## Centralized logs solutions 
### (SPLUNK, Logz.io, Logstash, etc.) 
{Grafana, Kafka, Graphite, Nagios -are-related- too}

ELK Stack was a collection of three **open-source products** — **E**lasticsearch, **L**ogstash, and **K**ibana — all developed, managed and maintained by [Elastic](https://www.elastic.co/). The introduction and subsequent addition of **Beats** turned the stack into a four legged project and led to a renaming of the stack as the **Elastic Stack**.

[**Elasticsearch**](https://logz.io/tag/elasticsearch/) is NoSQL database that uses the _Lucene search engine_. [**Logstash**](https://logz.io/tag/logstash/) is a data processing and transportation pipeline used to populate Elasticsearch with the data (though also it supports other destinations including Graphite, Kafka, Nagios and RabbitMQ). [**Kibana**](https://logz.io/tag/kibana/) is a dashboard that works on top of Elasticsearch. 

There are many varieties of ELK:
- The open-source ELK Stack platform ([on Elastic](https://www.elastic.co/webinars/introduction-elk-stack))
- [Hosted Elasticsearch](https://aws.amazon.com/elasticsearch-service/) (AWS)
- AI-powered ELK on an enterprise-grade platform ([on Logz.io](https://logz.io/platform/))

**ELK Stack** provides role-based security as a _separate paid tool_. **Splunk and managed-ELK services** offer _user management out of the box with user auditing included_.

* [SPLUNK](https://www.splunk.com)  { forwarder --> indexer --> search head ; uses its own [Splunk Search Processing Language (SPL)](https://www.splunk.com/en_us/resources/search-processing-language.html) which supports the search pipeline - consecutive commands are chained together using a pipe character } 
* Logstash https://github.com/elastic/logstash  { open-source code }
* [Kibana](https://www.elastic.co/kibana)  { query is based on the [Lucene query syntax](https://lucene.apache.org/core/3_5_0/queryparsersyntax.html) }


https://www.google.com/search?q=SPLUNK%2C+Logz.io%2C+Logstash 

### some comparison 
- https://stackshare.io/stackups/logz-io-vs-splunk-enterprise-vs-logstash
- https://devops.com/splunk-elk-stack-side-side-comparison/
