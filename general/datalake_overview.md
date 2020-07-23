# Bigstep Datalake service overview

The Bigstep DataLake is a specialised file system designed for scalability and hadoop compatibility. It is optimised for Parquet, Avro and Orc files and has no file size limit. It is the de-facto file system for Big Data applications.

The customer only pays for the stored data, independent of the underlying hardware.

The prefered access method is the [DataLake command line tool](/guides/using_the_datalake_command_line_tool).

Alternatively you can also use the [WebHDFS rest interface using cURL utility](/guides/managing_datalake_files_using_curl) or  access the files programatically via our [DataLake client libraries](https://github.com/bigstepinc/datalake-client-libraries).

## Architecture

To achieve high horizontal scalability the DataLake service employs a distributed replication schema. Every file is composed out of a sequence of 120MB blocks, and every block is stored multiple times across the cluster. The system attempts to distribute the blocks evenly across the data-nodes while also making sure replicas are not on the same machines or disks.
Every node has many disks, managed independently, and this replication system ensures that disk failures are not catastrophic. As opposed to RAID, this has the benefit of increased throughput, as a client can download different parts of a big file simultaneously from different data nodes.

![](/assets/general/datalake_architecture.svg)

##  DataLake permissions

DataLake authorization is done on a per file basis, in a UNIX-like way. Each file has an owner string and a group string, and permissions are set for:
1. the owner
2. the group
3. everybody else

There are multiple permissions possible for each of these categories:
1. (R)ead
2. (W)rite
3. (E)execute - or browse directory
4. no access

Permissions are not inherited and must be set on every file. The default setting is that the owner and the group are the same, and write permission is granted only to the owner (770).

To add a user to a group, simply add them as a delegate on the infrastructure. Users with admin rights on an infrastructure in Bigstep Metal Cloud also have admin rights on the HDFS home directory.

All file paths are prefixed with a `/dl<data_lake_id>`, where `data_lake_id` is a [DataLake object](https://api.bigstep.com/metal-cloud#schemas/DataLake) property.

Users do not have a home directory, however each DataLake of every [Infrastructure](https://api.bigstep.com/metal-cloud#schemas/Infrastructure) gets a uniquely identifiable home directory.

Files residing under the home directory of each DataLake service are owned by the owner of infrastructure the DataLake belongs to, regardless of permissions.


## Using the Bigstep Datalake with Apache Spark and Hadoop

The DataLake service is a GSS enabled WebHDFS and Kerberised HDFS compatible store so it can also be accessed through the native protocols:
1. Through the [WebHDFS](http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/WebHDFS.html) protocol which is a HTTP based protocol that can be used by many web enabled applications including cURL.
2. Through the binary HDFS protocol by [Hadoop](http://hadoop.apache.org/) native applications such as [Apache Spark](https://spark.apache.org/).

## Mounting the DataLake as a filesystem

A DataLake directory can also be mounted as a regular directory in the filesystem via [FUSE](http://www.cloudera.com/content/cloudera/en/documentation/core/v5-2-x/topics/cdh_ig_hdfs_mountable.html). Please note that because the underlying filesystem is an object storage certain functions, notably random access are not supported by the FUSE connector and will fail.

### Additional datalake resources

* [HDFS Apache user guide](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
* [Java native API](http://hadoop.apache.org/docs/current/api/)
* [Kite SDK](https://github.com/kite-sdk/kite)
* [Microsoft .NET SDK for HDFS file access](https://code.msdn.microsoft.com/windowsdesktop/Hadoop-Net-HDFS-File-Access-18e9bbee)
* [Python SDK  for HDFS file access](https://pypi.python.org/pypi/snakebite/)
* [Thrift generated APIs for HDFS file access](http://wiki.apache.org/hadoop/HDFS-APIs/)
