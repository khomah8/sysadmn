## Application Performance M(onitoring | anagement) [APM] [wiki](https://en.wikipedia.org/wiki/Application_performance_management)

related to: devOps, serviceOps, etc. 

tagged: #app-monitoring-task #app-monitoring-tools #app-monitoring-framework #app-moinitoring-solution #app-performance-monitoring 

### [some products/tools]
- https://webapplicationmonitoring.net/
- https://smartbear.com/learn/performance-monitoring/why-you-should-be-monitoring/
- https://www.atlassian.com/software/opsgenie
- https://sentry.io/for/performance/
- https://www.nagios.com/solutions/web-application-monitoring/
- https://www.pingdom.com/blog/best-practices-for-web-app-monitoring/
- https://www.apmdigest.com/the-anatomy-of-apm-4-foundational-elements-to-a-successful-strategy `"APM is "the translation of IT metrics into business meaning ([i.e.] value)"`

### [APM tools comparison]

1. https://coralogix.com/log-analytics-blog/apm-comparison/
2. https://crozdesk.com/it/application-performance-monitoring-apm-software, https://crozdesk.com/compare/appdynamics-vs-dynatrace-vs-new-relic 

### cornerstones | key terms : 
- APM is for "application performance management/monitoring"  
- measuring-of : 1) user eXperience; 2) resources usage; 
- dashboard view(s) 
- score index (apdex IDX as [ SAtisfied T ; TOlerating 1' < T < 4': FRustrated T > 4' ] for neW reLiCt; )
- index baseline 
- System health issues: 1) events; 2) incidents --> 1) violations; 2) warnings 3) ??
- Root Cause analysis 
- MTTD/R / MTTD-R [mean-time to detect AND resolve] parameter 
- SIEM [security information and event management] platform

### APM by targets 
- FrontEnd applications
- BackEnd applications
- Orchestration applications
- other?

### New Relic One (VS other services)
> `New Relic` is a SaaS platform, while `AppDynamics` and `Dynatrace` offer [full SaaS, on-prem, and hybrid installation options] 

> `two ways` to write your own queries to retrieve data and build charts (`Query builder`):
- __NRQL mode__: query using [New Relic query language (NRQL)](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-new-relics-query-language), the same language we use to build most of our UI experiences.
- __PromQL-style mode__: write basic queries using a [PromQL-style query](https://prometheus.io/docs/prometheus/latest/querying/basics/).  

### Centralized logs solutions ( SPLUNK, ELK, etc. ) 
{ Grafana, Kafka, Graphite, Nagios, etc. are related items } 

> `ELK Stack { log analytics platform }` was a collection of three **open-source products** — [__E__lasticsearch](https://logz.io/tag/elasticsearch/), [__L__ogstash](https://logz.io/tag/logstash/),[github](https://github.com/elastic/logstash), and [__K__ibana](https://logz.io/tag/kibana/) — all developed, managed and maintained by [Elastic](https://www.elastic.co/). The introduction and subsequent addition of **Beats** turned the stack into a four-legged project and led to a renaming of the stack as the `**Elastic Stack**`.
> `Elasticsearch` is NoSQL database that uses the __Lucene search engine__. `Logstash` is a data processing and transportation pipeline used to populate Elasticsearch with the data (though also it supports other destinations including Graphite, Kafka, Nagios and RabbitMQ). [Kibana](https://www.elastic.co/kibana) is a dashboard that works on top of Elasticsearch. Kibana query is based on the [Lucene query syntax](https://lucene.apache.org/core/3_5_0/queryparsersyntax.html). 

:green_book: [small-size ELK, PNG-diagram](https://logz.io/wp-content/uploads/2018/08/image21-1024x328.png)

:orange_book: [more complex ELK, PNG-diagram](https://logz.io/wp-content/uploads/2018/08/image6-1024x422.png) 

> There are many `varieties of ELK`:
- The open-source ELK Stack platform ([on Elastic](https://www.elastic.co/webinars/introduction-elk-stack))
- [Hosted Elasticsearch](https://aws.amazon.com/elasticsearch-service/) (AWS) : [installing ELK on Ubuntu](https://logz.io/learn/complete-guide-elk-stack/#installing-elk), accessing by SSH and TCP 5601 (Kibana) 
- AI-powered ELK on an enterprise-grade platform ([on Logz.io](https://logz.io/platform/))

* [SPLUNK](https://www.splunk.com) { forwarder --> indexer --> search head ; uses its own [Splunk Search Processing Language (SPL)](https://www.splunk.com/en_us/resources/search-processing-language.html) which supports the search pipeline - consecutive commands are chained together using a pipe character }

> __ELK Stack__ provides `role-based security` as a separate paid tool. __Splunk and managed-ELK services__ offer `user management` out of the box with user auditing included.

comparisions: 
- https://stackshare.io/stackups/logz-io-vs-splunk-enterprise-vs-logstash
- https://devops.com/splunk-elk-stack-side-side-comparison/
- https://www.getapp.com/business-intelligence-analytics-software/a/logz-io/compare/splunk-enterprise/
