# Project 3 - Udacity Data Engineering Nanodegree

## Introduction

## Data

## ETL

## Cloud Architecture

## Configuration

A sample `dwh.cfg` file is needed in the root of the project repository with the configuration for the Data Warehose architecture in AWS. The following sample configuration file can be filled:

```
[CLUSTER]
HOST=""
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=

[AWS]
KEY=
SECRET=

[DWH] 
DWH_CLUSTER_TYPE=multi-node
DWH_NUM_NODES=4
DWH_NODE_TYPE=dc2.large

DWH_IAM_ROLE_NAME=
DWH_CLUSTER_IDENTIFIER=
DWH_DB=
DWH_DB_USER=
DWH_DB_PASSWORD=
DWH_PORT=

DWH_ENDPOINT=""
DWH_ROLE_ARN=""

[IAM_ROLE]
ARN=""

[S3]
LOG_DATA=''
LOG_JSONPATH=''
SONG_DATA=''
```