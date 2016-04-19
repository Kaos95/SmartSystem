# Smart System  [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)


A smart system designed for high-reliability on low costing hardware. Aims to aid in the future development of smart homes and Systems.

# Motivation

Smart home system inspired by the [HDFS] (https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html#Streaming+Data+Access)(Hadoop Distributed File System) architecture, particularly the Hadoop Cluster design approach for the storing and analyzing of large volume of unstructured data. A general smart structure that permits, connections between sensors. External sensors interact with a controller system, whilst corresponding with a storage system.  

# Installation

###### Download repository   
[Download Zip] (https://github.com/HaydenMcParlane/SmartSystem)

# Design

+ Virtual network associated with Controllers
+ Virtual NAS (or similar distributed storage)
+ Flow of data: Sensor --> Controller Private Network <--> Storage Private Network
+ Redundancy with fail-over (either load-balancing or active-standby for reliability) in controllers and physical storage.

Testing something...

#Maintainer

###### Hayden McParlane
###### Contact 
+ [GitHub] (https://github.com/hmcparlane)
+ [LinkedIn] (https://www.linkedin.com/in/haydenmcp)
