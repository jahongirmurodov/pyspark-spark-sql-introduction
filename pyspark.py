
# pip install pyspark

import pyspark.sql.functions as F
from pyspark.sql import SparkSession

# 3. Запуск SparkSession
# SparkSession -> это основная точка входа в Spark.
spark = SparkSession.builder.appName('pyspark_learning').getOrCreate()

print(f'Spark version: {spark.version}')


# 4. Загрузка данных

df = spark.read.csv('customs_data.csv', sep=';', header=True)

# 5. Просмотр данных


# Первые строки:
df.show(5)

# Вывод без обрезания текста:
df.show(5, truncate=False)

# 6. Схема данных
# Spark автоматически пытается определить типы данных.
df.printSchema()

# 7. Переименование колонок
df_new = (
    df
    .withColumnRenamed('direction_eng', 'direction')
    .withColumnRenamed('measure_eng', 'measure')
)

print(df_new.columns)

# 8. Уникальные значения

# Посмотреть список стран:
df_new.select('country').distinct().show(10, truncate=False)

# 9. Агрегация данных

result = (
    df_new.groupBy('country')
    .agg(F.count('*').alias('total_rows'))
    .orderBy(F.col('total_rows').desc())
)
result.show()

# 10. Фильтрация данных

# Способ 1
df_filter = (
    df_new
    .where(F.col('country') == 'DE')
    .where(F.col('value').isNotNull())
)
df_filter.show()

# Способ 2 (SQL вариант)
df_filter = df_new.where("""
    country = 'DE' AND value IS NOT NULL
""")
df_filter.show()

# 11. Выбор колонок
final = (
    df_filter.select(
        'month',
        'country',
        'code',
        'value',
        'netto',
        'quantity'
    )
)
final.show(3)


# Transformations
# select
# filter
# groupBy
# withColumn

# Actions
# show()
# count()
# collect()
# write()

# Когда мы вызываем:
# final.show()
# Spark только тогда запускает вычисления.

# 13. Партиции (Partitions)
print(final.rdd.getNumPartitions())

# 14. Завершение Spark
spark.stop()