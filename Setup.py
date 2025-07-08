# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE VOLUME workspace.raw.rawvolume

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA workspace.bronze;
# MAGIC CREATE SCHEMA workspace.silver;
# MAGIC CREATE SCHEMA workspace.gold;

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/workspace/raw/rawvolume/rawdata/")

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/workspace/raw/rawvolume/rawdata/bookings")
dbutils.fs.mkdirs("/Volumes/workspace/raw/rawvolume/rawdata/flights")
dbutils.fs.mkdirs("/Volumes/workspace/raw/rawvolume/rawdata/customers")
dbutils.fs.mkdirs("/Volumes/workspace/raw/rawvolume/rawdata/airports")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM DELTA.`/Volumes/workspace/bronze/bronzevolume/flights/data/`