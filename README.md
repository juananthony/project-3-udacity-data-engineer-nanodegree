# Project 3 - Udacity Data Engineering Nanodegree

## Introduction

This project is the third one in the Data Engineering Nanodegree. This is a ETL pipeline that extracts the data of Sparkify (a fake music streaming startup) from S3, stages them in Redhisft, and tranforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

## Data

### Project Datasets

#### Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

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