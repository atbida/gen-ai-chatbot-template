from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from chatbot_live_slack.config.ConfigStore import *
from chatbot_live_slack.udfs.UDFs import *

def extract_fields(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("value_parsed.payload.event.text").alias("text"), 
        col("value_parsed.payload.event.ts").alias("ts"), 
        col("value_parsed.payload.event.user").alias("user"), 
        col("value_parsed.payload.event.channel").alias("channel")
    )
