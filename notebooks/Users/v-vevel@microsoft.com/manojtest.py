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

notebooks/Users/v-vevel@microsoft.com/githubcheck