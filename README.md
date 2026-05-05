# PySpark Big Data Basics

This project demonstrates the fundamental concepts of Big Data processing using PySpark and Spark SQL.

It covers the core operations required to load, transform, and analyze data in a distributed environment.

---

## 📊 Overview

The project introduces:
- Apache Spark architecture basics
- Working with distributed DataFrames
- Data transformation and aggregation
- Filtering and SQL-like queries
- Understanding Lazy Evaluation

---

## ⚙️ Technologies

- PySpark
- Spark SQL

---

## 🗂 Project Workflow

### 1. Spark Session Initialization
- Creating a `SparkSession` as the entry point to Spark

### 2. Data Loading
- Reading CSV data into a distributed DataFrame

### 3. Data Exploration
- Previewing data using `show()`
- Inspecting schema with `printSchema()`

### 4. Data Transformation
- Renaming columns
- Selecting required fields
- Handling missing values

### 5. Data Analysis
- Aggregation using `groupBy()` and `count()`
- Sorting results
- Extracting distinct values

### 6. Filtering
- Using PySpark functions (`col`, `isNotNull`)
- Using SQL-style conditions

### 7. Working with Partitions
- Understanding data partitioning
- Checking number of partitions

### 8. Lazy Evaluation
- Explanation of transformations vs actions
- Execution triggered only by actions (`show()`)

---

## 📈 Key Concepts Demonstrated

- Distributed data processing
- DataFrame API
- Spark SQL filtering
- Aggregations and grouping
- DAG (Directed Acyclic Graph)
- Partitioning

---

## 🎯 Purpose

This project is a beginner-level introduction to Big Data tools and demonstrates how to process large datasets efficiently using PySpark.

---

## 📌 Notes

- Dataset: CSV file (`customs_data.csv`)
- Designed for learning and practice purposes

------------------------------------------------------

# Основы PySpark и Big Data

Данный проект демонстрирует базовые принципы обработки больших данных с использованием PySpark и Spark SQL.

---

## 📊 Обзор

В проекте реализованы:
- Основы архитектуры Apache Spark
- Работа с распределенными DataFrame
- Трансформации и агрегации данных
- Фильтрация данных (включая SQL-подход)
- Концепция Lazy Evaluation

---

## ⚙️ Технологии

- PySpark
- Spark SQL

---

## 🗂 Процесс работы

### 1. Инициализация Spark
- Создание `SparkSession`

### 2. Загрузка данных
- Чтение CSV файла в DataFrame

### 3. Исследование данных
- Просмотр данных (`show`)
- Анализ структуры (`printSchema`)

### 4. Трансформация данных
- Переименование колонок
- Выбор нужных полей
- Работа с пропущенными значениями

### 5. Анализ данных
- Группировка (`groupBy`)
- Подсчет записей
- Сортировка
- Уникальные значения

### 6. Фильтрация
- Через PySpark функции
- Через SQL-условия

### 7. Партиции
- Работа с распределением данных
- Проверка количества партиций

### 8. Lazy Evaluation
- Отложенное выполнение операций
- Выполнение только при вызове Action (`show`)

---

## 📈 Ключевые концепции

- Распределенная обработка данных
- DataFrame API
- Spark SQL
- DAG (граф выполнения)
- Партиционирование

---

## 🎯 Цель проекта

Проект предназначен для изучения основ Big Data и демонстрирует базовые возможности PySpark.

---

## 📌 Примечание

- Данные: `customs_data.csv`
- Проект выполнен в учебных целях
