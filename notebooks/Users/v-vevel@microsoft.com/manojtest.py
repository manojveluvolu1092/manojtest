# Databricks notebook source
dataFrame = "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv"
spark.read.format("csv").option("header","false")\
  .option("inferSchema", "false").load(dataFrame)\
  .createOrReplaceTempView("diamonds1")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM diamonds1 limit 1

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/databricks/test/")

# COMMAND ----------

dbutils.fs.put("/databricks/test/postgresql-install.sh","""
#!/bin/bash
wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar http://central.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar
wget --quiet -O /mnt/jars/driver-daemon/postgresql-42.2.2.jar http://central.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/test/postgresql-install.sh"))

# COMMAND ----------

import sys
print(sys.version)

# COMMAND ----------

import sys
print(numpy.version)

# COMMAND ----------

# MAGIC %sh
# MAGIC /home/ubuntu/databricks/python/bin/pip3

# COMMAND ----------

import numpy
numpy.version.version

# COMMAND ----------

import numexpr
numexpr.print_versions()

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/databricks/numpy/")

# COMMAND ----------

dbutils.fs.put("dbfs:/databricks/numpy/numpy.sh","""
#!/bin/bash
pip uninstall --yes numpy
rm -rf /home/ubuntu/databricks/python/lib/python3.5/site-packages/numpy*
rm -rf /databricks/python/lib/python3.5/site-packages/numpy*
/usr/bin/yes | /home/ubuntu/databricks/python/bin/pip install numpy==1.15.0
""",True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/numpy/numpy.sh"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/cluster-logs/0514-170154-lured342/init_scripts/0514-170154-lured342_10_139_64_7/20190514_200610_00_postgresql-install.sh.stdout.log"))

# COMMAND ----------

/Users/v-vevel@microsoft.com/

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ls /databricks/hive/conf/hive-site.xml

# COMMAND ----------

cat /databricks/hive/conf/hive-site.xml

# COMMAND ----------

# MAGIC %sh 
# MAGIC 
# MAGIC ls /databricks/hive/conf/

# COMMAND ----------

# MAGIC %sh 
# MAGIC 
# MAGIC cat /databricks/hive/conf/hive-site.xml

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC dbutils.fs.put(
# MAGIC     "/databricks/init/manojcluster/external-metastore.sh",
# MAGIC     """#!/bin/sh
# MAGIC       |# Loads environment variables to determine the correct JDBC driver to use.
# MAGIC       |source /etc/environment
# MAGIC       |# Quoting the label (i.e. EOF) with single quotes to disable variable interpolation.
# MAGIC       |cat << 'EOF' > /databricks/driver/conf/00-custom-spark.conf
# MAGIC       |[driver] {
# MAGIC       |    # Hive specific configuration options for metastores in the local mode.
# MAGIC       |    # spark.hadoop prefix is added to make sure these Hive specific options will propagate to the metastore client.
# MAGIC       |    "spark.hadoop.javax.jdo.option.ConnectionURL" = "jdbc:mysql://<mysql-host>:<mysql-port>/<metastore-db>"
# MAGIC       |    "spark.hadoop.javax.jdo.option.ConnectionUserName" = "<mysql-username>"
# MAGIC       |    "spark.hadoop.javax.jdo.option.ConnectionPassword" = "<mysql-password>"
# MAGIC       |
# MAGIC       |    # Spark specific configuration options
# MAGIC       |    "spark.sql.hive.metastore.version" = "<hive-version>"
# MAGIC       |    # Skip this one if <hive-version> is 0.13.x.
# MAGIC       |    "spark.sql.hive.metastore.jars" = "<hive-jar-source>"
# MAGIC       |
# MAGIC       |    # If any of your table or database use s3 as the file system scheme,
# MAGIC       |    # uncomment the next line to set the s3:// URL scheme to S3A file system.
# MAGIC       |    # spark.hadoop prefix is added to make sure these file system options will
# MAGIC       |    # propagate to the metastore client and Hadoop configuration.
# MAGIC       |    # "spark.hadoop.fs.s3.impl" = "com.databricks.s3a.S3AFileSystem"
# MAGIC       |
# MAGIC       |    # If you need to use AssumeRole, uncomment the following settings.
# MAGIC       |    # "spark.hadoop.fs.s3a.impl" = "com.databricks.s3a.S3AFileSystem"
# MAGIC       |    # "spark.hadoop.fs.s3n.impl" = "com.databricks.s3a.S3AFileSystem"
# MAGIC       |    # "spark.hadoop.fs.s3a.credentialsType" = "AssumeRole"
# MAGIC       |    # "spark.hadoop.fs.s3a.stsAssumeRole.arn" = "<sts-arn>"
# MAGIC       |EOF
# MAGIC       |
# MAGIC       |case "$DATABRICKS_RUNTIME_VERSION" in
# MAGIC       |  "")
# MAGIC       |     DRIVER="com.mysql.jdbc.Driver"
# MAGIC       |     ;;
# MAGIC       |  *)
# MAGIC       |     DRIVER="org.mariadb.jdbc.Driver"
# MAGIC       |     ;;
# MAGIC       |esac
# MAGIC       |# Add the JDBC driver separately since must use variable expansion to choose the correct
# MAGIC       |# driver version.
# MAGIC       |cat << EOF >> /databricks/driver/conf/00-custom-spark.conf
# MAGIC       |    "spark.hadoop.javax.jdo.option.ConnectionDriverName" = "$DRIVER"
# MAGIC       |}
# MAGIC       |EOF
# MAGIC       |""".stripMargin,
# MAGIC     overwrite = true
# MAGIC )

# COMMAND ----------

# MAGIC 
# MAGIC %sh
# MAGIC 
# MAGIC cat /databricks/hive/conf/hive-site.xml

# COMMAND ----------

# MAGIC %sh
# MAGIC nc -vz <DNS name> <port>

# COMMAND ----------

1 + 1


# COMMAND ----------

2 + 1

# COMMAND ----------

