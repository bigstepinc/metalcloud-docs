# Using the data lake command line tool

The DataLake client offers a way to interact with the datalake via the command line. It is part of the [datalake-client-libraries](https://github.com/bigstepinc/datalake-client-libraries) project that enables integration with external tools.
It is a standalone wrapper of the `hdfs dfs` command that hadoop users might be familiar with.

### Retrieving access credentials

All required credentials (the `core-site.xml` file) can be accessed from the Infrastructure Editor:

![](/assets/guides/using_the_datalake_command_line_tool.png)

### Installing the command line utility

1. Java JRE 1.8 is required. JAVA_HOME must be set or at least the java executable must be available in the path.
2. If you have the Oracle JDK, install [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html).
3. Create and deploy a DataLake using the infrastructure editor at [cloud.bigstep.com](https://cloud.bigstep.com).
4. Download the binaries from the [Bigstep DataLake repository](http://repo.bigstepcloud.com/bigstep/datalake/).
5. Download the `core-site.xml` configuration file from the Configuration tab of the DataLake overview panel in the interface.
6. Setup a keytab. Use the password you use to log in to your Bigstep account:
```bash
./bin/dl genkeytab kxxxx@bigstep.io /etc/kxxx.keytab
```
7. Edit `./conf/core-site.xml` and add your (kxxx) principal or the DataLake endpoint that you plan to use.
8. Execute commands by using `./bin/dl`.

### Listing a directory from the DataLake:

```bash
./bin/dl -ls dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dlxxxx/baseballdatabank-master/core
Found 27 items
-rw-r-----   3 k7 i1929     208224 2016-10-24 19:51 dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/baseballdatabank-master/core/AllstarFull.csv
-rw-r-----   3 k7 i1929    5989686 2016-10-24 19:52 dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/baseballdatabank-master/core/Appearances.csv
-rw-r-----   3 k7 i1929       8104 2016-10-24 19:52 dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/baseballdatabank-master/core/AwardsManagers.csv
-rw-r-----   3 k7 i1929     246769 2016-10-24 19:52 dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/baseballdatabank-master/core/AwardsPlayers.csv
-rw-r-----   3 k7 i1929      18188 2016-10-24 19:52 dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/baseballdatabank-master/core/AwardsShareManagers.csv
```

### Uploading a file/directory to the DataLake:

```bash
./bin/dl -copyFromLocal README.md dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dlxxx/
```

### Downloading a file/directory from the DataLake:

```bash
./bin/dl -cp dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/README.md /tmp
```

### Deleting a file/directory from the DataLake:

```bash
./bin/dl -rm -r -f dl://node10930-datanodes-data-lake01-uk-reading.bigstep.io:14000/data_lake/dl267/README.md 
```

To find out more comands run:

```
./bin/dl -help
```