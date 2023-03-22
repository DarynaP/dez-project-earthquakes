# DATA ENGINEERING ZOOMCAMP – Final Project
## Overview
This project was developed as a part of the [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) 
course held by [DataTalks.Club](https://datatalks.club/). 
The goal of this project was to build an end-to-end data pipeline, with a focus on: 
* Creating a data pipeline to aid with batch data processing (on a weekly basis);
* Producing an analytical dashboard that will allow to easily discover trends and assimilate insights.

> *** Disclaimer *** The dataset used for this project was collected between January and April 2023, which makes it a relatively small dataset (X observations). The main idea of this project wasn't to deal with a big dataset at this point, but rater build a pipeline that can fetch, organize and transform present data on a weekly basis. However, it is possible to obtain a bigger dataset if you maintain this pipeline to fetch data for longer time, but for me that wasn't possible due to course deadlines.

## Table of Contents
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#dataset-used">Dataset used</a></li>
        <li><a href="#technologies">Technologies</a></li>
        <li><a href="#project-architecture">Project architecture</a></li>
      </ul>
      <a href="#dashboard">Dashboard</a>
      <ul>
      <a href="#conclusions">Conclusions</a>
      <ul>
      <a href="#reproducibility">Reproducibility</a>
      <ul>
      </ol>
</details>

## About the Project
The planet Earth is constantly changing. Seismic activity is produced when tectonic plates shift or when other events take place below the surface. While some earthquakes are sizable and do a lot of damage, other earthquakes are so little that they can hardly be felt without sensitive technology. 

Earthquake data is a valuable resource for public safety, and this project aims to look to this information at weekly basis. With the power of this data, we can answer a series of questions:
 * How many earthquakes happened per day?
 * 
 * Which geographical area had the most earthquakes? How many had 
 *
 *



### Dataset used
The data of was collected using [EveryEarthquake API](https://rapidapi.com/dbarkman/api/everyearthquake/), additionally the data obtained between January and April 2023 can be found in the folder `earthquake-data` as parquet files (per week).
The complete information about the dataset can be found at [ANSS Comprehensive Earthquake Catalog](https://earthquake.usgs.gov/data/comcat/#event-terms). 


The final dataset contain the following information:


<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

### Technologies
For this project the following technologies were used:
<br>
Infrastructure as code (IaC): *Terraform* 

<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

### Project architecture
<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

## Dashboard

## Conclusions

## Reproducibility 