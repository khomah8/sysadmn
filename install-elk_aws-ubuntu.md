## logz.io Guide 

https://logz.io/learn/complete-guide-elk-stack/

### Installing Elasticsearch
First, you need to add Elastic’s signing key so that the downloaded package can be verified (skip this step if you’ve already installed packages from Elastic):

`wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -`

For Debian, we need to then install the apt-transport-https package:

`sudo apt-get update`

`sudo apt-get install apt-transport-https`

The next step is to add the repository definition to your system:

`echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list`

To install a version of Elasticsearch that contains only features licensed under Apache 2.0 (aka OSS Elasticsearch):

`echo "deb https://artifacts.elastic.co/packages/oss-7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list`

All that’s left to do is to update your repositories and install Elasticsearch:

`sudo apt-get update`

`sudo apt-get install elasticsearch`

Elasticsearch configurations are done using a configuration file that allows you to configure general settings (e.g. node name), 
as well as network settings (e.g. host and port), where data is stored, memory, log files, and more.

For our example, since we are installing Elasticsearch on AWS, it is a good best practice to bind Elasticsearch to either a private IP or localhost:

`sudo vim /etc/elasticsearch/elasticsearch.yml`

```
network.host: "localhost"
http.port:9200
cluster.initial_master_nodes: ["<PrivateIP"]
```

To run Elasticsearch, use:

`sudo service elasticsearch start`

To confirm that everything is working as expected, point curl or your browser to http://localhost:9200, and you should see something like the following output:

```
{
  "name" : "ip-172-31-10-207",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "bzFHfhcoTAKCH-Niq6_GEA",
  "version" : {
    "number" : "7.1.1",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "7a013de",
    "build_date" : "2019-05-23T14:04:00.380842Z",
    "build_snapshot" : false,
    "lucene_version" : "8.0.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

Installing an Elasticsearch cluster requires a different type of setup. Read our Elasticsearch Cluster tutorial for more information on that.

### Installing Logstash
Logstash requires Java 8 or Java 11 to run so we will start the process of setting up Logstash with:

`sudo apt-get install default-jre`

Verify java is installed:

`java -version`

```
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-8u191-b12-2ubuntu0.16.04.1-b12)
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

Since we already defined the repository in the system, all we have to do to install Logstash is run:

`sudo apt-get install logstash`

Before you run Logstash, you will need to configure a data pipeline. We will get back to that once we’ve installed and started Kibana.

### Installing Kibana
As before, we will use a simple apt command to install Kibana:

`sudo apt-get install kibana`

Open up the Kibana configuration file at: /etc/kibana/kibana.yml, and make sure you have the following configurations defined:

```
server.port: 5601
elasticsearch.url: "http://localhost:9200"
```

These specific configurations tell Kibana which Elasticsearch to connect to and which port to use.

Now, start Kibana with:

`sudo service kibana start`

Open up Kibana in your browser with: http://localhost:5601. You will be presented with the Kibana home page.

### Installing Beats
The various shippers belonging to the Beats family can be installed in exactly the same way as we installed the other components.

As an example, let’s install Metricbeat:

`sudo apt-get install metricbeat`

To start Metricbeat, enter:

`sudo service metricbeat start`

Metricbeat will begin monitoring your server and create an Elasticsearch index which you can define in Kibana. In the next step, however, we will describe how to set up a data pipeline using Logstash.

More information on using the different beats is available on our blog: **Filebeat, Metricbeat, Winlogbeat, Auditbeat**.
