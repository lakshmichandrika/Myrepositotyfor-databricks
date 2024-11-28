# Databricks notebook source
# MAGIC  %run "../includes/configurations"

# COMMAND ----------

# We drop the database only if exists
spark.sql(f"DROP DATABASE IF EXISTS demo CASCADE;")

# COMMAND ----------

# We are goinf to mount a databse named "demo" on our gold container
# Note: If you drop your database all the folders inside the location of your database would be deleted
spark.sql( f"CREATE DATABASE IF NOT EXISTS demo LOCATION '{gold_folder_path}'")