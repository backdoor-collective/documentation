# Datamill

## About
We are conceiving a [Datenmischwerk] made from Open Data and different 
Open Source Software components.

The journey started with the
[discussion about open weather data at the Hiveeyes project] and today we are running
a whole [DWD / Climate-Data-Center (CDC) pipeline]. By [ramping up Luftdatenpumpe],
we also started to process data from [luftdaten.info]. 

Spinoffs of those development efforts are taking place at the
[Panodata Community Forum] and the [Earth Observations GitHub Organization] these days.
We are always happy to see like-minded people joining us.

[Datenmischwerk]: https://community.hiveeyes.org/t/datenmischwerk/702
[discussion about open weather data at the Hiveeyes project]: https://community.hiveeyes.org/t/open-weather-data/113
[DWD / Climate-Data-Center (CDC) pipeline]: https://community.hiveeyes.org/t/datenquelle-dwd-climate-data-center-cdc-wetterdaten-aufzeichnungen/1532
[ramping up Luftdatenpumpe]: https://community.hiveeyes.org/t/erneuerung-der-luftdatenpumpe/1199
[luftdaten.info]: https://luftdaten.info/
[Panodata Community Forum]: https://community.panodata.org/
[Earth Observations GitHub Organization]: https://github.com/earthobservations

## Live data
We are running data pipelines on two machines.
- [https://weather.hiveeyes.org/](https://weather.hiveeyes.org/)
- [https://swarm.hiveeyes.org/](https://swarm.hiveeyes.org/)

## Tools

#### Earth observations
- [Wetterdienst] - Python Toolset For Accessing Weather Data From German Weather Service.
- [GribMagic] - A generic weather forecast downloader.
- [Luftdatenpumpe] - Process live and historical data from luftdaten.info, IRCELINE and OpenAQ. Filter by station-id, sensor-id and sensor-type, apply reverse geocoding, store into timeseries and RDBMS databases, publish to MQTT, output as JSON or visualize in Grafana. 
- [phenodata] - A data acquisition and manipulation toolkit for open access phenology data.


#### Data acquisition
- [Kotori] - A flexible data historian based on InfluxDB, Grafana, MQTT and more.
- [Terkin] - A datalogger for MicroPython and CPython.
- [Hiveeyes Firmwares] - Arduino firmwares for different MCUs.
- [mqttwarn] - Subscribe to MQTT topics and notify pluggable services.


#### Grafana
- [Grafana Map Panel] - Fork of the original Grafana Worldmap Panel with improved convenience, robustness and features.
- [grafana-pandas-datasource] - Grafana Python datasource - using Pandas for timeseries and table data.
- [grafanimate] - Animate timeseries data with Grafana.
- [grafana-wtf] - Grep through all Grafana entities in the spirit of git-wtf.


[Wetterdienst]: https://community.panodata.org/t/wetterdienst-a-new-toolset-for-accessing-weather-data-from-german-weather-service-dwd-based-on-pandas/165
[GribMagic]: https://github.com/earthobservations/gribmagic
[Luftdatenpumpe]: https://community.panodata.org/t/luftdatenpumpe/21
[phenodata]: https://github.com/hiveeyes/phenodata

[Kotori]: https://getkotori.org/
[Terkin]: https://terkin.org/
[Hiveeyes Firmwares]: https://github.com/hiveeyes/arduino
[mqttwarn]: https://github.com/jpmens/mqttwarn

[Grafana Map Panel]: https://community.panodata.org/t/grafana-map-panel/121
[grafana-pandas-datasource]: https://github.com/panodata/grafana-pandas-datasource
[grafanimate]: https://github.com/panodata/grafanimate
[grafana-wtf]: https://github.com/panodata/grafana-wtf


## Exhibition
For enjoying more screenshots and details about the projects and tools
beyond the tiny exhibition below, you are welcome to visit the [Panodata Overview].

[Panodata Overview]: https://community.panodata.org/t/overview/120

### Screenshots
Some Grafana screenshots to get a rough impression how data looks like
after coming out of the pipeline.

![image](https://community.panodata.org/uploads/default/original/1X/e2f1671157c4aadf0c06d488fddb7d691b2e3946.png)

![image](https://ptrace.hiveeyes.org/2018-12-28_wetter-dwd-temperatur-sonne-niederschlag-karten-cdc.gif)
![image](https://ptrace.hiveeyes.org/2018-12-26_ldi-coverage.gif)

### Presentation at the Geospatial Sensing Conference (GSC2019) in Münster
We are happy to have been invited to talk about the things we are doing
around environmental data collection, processing and visualization within
the lightning talks section of a GIS-related conference in 2019.
The audience was all ears about the capabilities of InfluxDB and Grafana.

* More information about the talk.

  [Talking about the Hiveeyes project and some Panodata technologies at the 5th Geospatial Sensor Web Conference in Münster, 3. September 2019](https://community.panodata.org/t/talking-about-the-hiveeyes-project-and-some-panodata-technologies-at-the-5th-geospatial-sensor-web-conference-in-munster-3-september-2019/18)


* The presentation slides.

  [Fancy synthesizing of bee-, weather- and environmental-data with Grafana and InfluxDB](https://weather.hiveeyes.org/pubs/20190903_52northV_Motl_Mehldau_-_Fancy_Synthesizing_of_Environmental_Data/)

![image](https://user-images.githubusercontent.com/453543/103153863-164fea00-4794-11eb-8129-8277c8d7bade.png)
