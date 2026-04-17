# Databricks notebook source

# COMMAND ----------

print("Deployed via GitHub Actions with Workload Identity Federation")

# COMMAND ----------

spark.sql("SELECT current_user() AS deployed_by, current_timestamp() AS deployed_at").display()
