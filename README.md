# Reddit Sentiment Analysis Using AWS Services

## Project Overview

This project focuses on performing sentiment analysis on Reddit data using various AWS services. Sentiment analysis involves extracting opinions, emotions, and attitudes from textual content, and this project aims to understand the sentiments of Reddit users on different topics. By utilizing AWS services such as Amazon Comprehend, AWS Lambda, and Amazon S3, we built a pipeline to collect, process, and analyze Reddit comments in real-time, providing insights into public sentiment trends.

## Features

- **Data Collection**: Automated data collection from Reddit using the Python Reddit API Wrapper (PRAW) integrated with AWS Lambda.
- **Real-Time Data Ingestion**: Utilizes AWS Kinesis Firehose to ingest and stream data to further processing stages.
- **Sentiment Analysis**: AWS Comprehend is used to classify Reddit comments into positive, negative, neutral, or mixed sentiment categories.
- **Data Storage**: Processed data is stored securely in Amazon S3 for further analysis and retrieval.
- **Data Cataloging**: AWS Glue is employed for metadata management and data cataloging.
- **Querying and Visualization**: AWS Athena is used to query the processed data, and Power BI provides a visual representation of sentiment trends.

## Tools and Technologies

- **AWS Lambda**: For triggering the collection and processing of data.
- **Amazon Kinesis Firehose**: For real-time data streaming.
- **Amazon Comprehend**: To perform sentiment analysis on collected Reddit data.
- **Amazon S3**: For scalable storage of the processed data.
- **AWS Glue**: For automating data cataloging and integration.
- **Amazon Athena**: For querying data with standard SQL.
- **Power BI**: For creating interactive visualizations and reports.

## Project Architecture

The pipeline for sentiment analysis is broken down into the following steps:

1. **Data Collection**: AWS Lambda, with PRAW, collects Reddit posts and comments and sends them through the data pipeline.
2. **Data Ingestion**: AWS Kinesis Firehose ingests the data in real time, invoking another Lambda function for sentiment analysis.
3. **Sentiment Analysis**: AWS Comprehend analyzes the text and assigns sentiment scores to each comment.
4. **Data Storage**: The processed data is stored in Amazon S3 for further querying.
5. **Data Cataloging**: AWS Glue creates a data catalog for seamless integration with Athena.
6. **Querying and Visualization**: AWS Athena queries the data, while Power BI visualizes the trends.

## Flowchart

![Flowchart](/Flowchart.jpeg)

## Dashboard

![Dashboard](/Dashboard.jpg)

## Poster

![Poster](/Poster.jpg)
