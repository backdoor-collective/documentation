# Datamill

## About
Within our work, we are conceiving a [Datenmischwerk](https://community.hiveeyes.org/t/datenmischwerk/702)
made from Open Data and different Open Source Software components.

## Exhibition


## Tools

#### Earth observations / Open Data
- [Wetterdienst] - Python Toolset For Accessing Weather Data From German Weather Service.
- [GribMagic] - A generic weather forecast downloader.
- [Luftdatenpumpe] - Process live and historical data from luftdaten.info, IRCELINE and OpenAQ. Filter by station-id, sensor-id and sensor-type, apply reverse geocoding, store into timeseries and RDBMS databases, publish to MQTT, output as JSON or visualize in Grafana. 
- [phenodata] - A data acquisition and manipulation toolkit for open access phenology data.


#### Data acquisition
- [Kotori] - A flexible data historian based on InfluxDB, Grafana, MQTT and more.
- [Terkin] - A datalogger for MicroPython and CPython.
- [mqttwarn] - Subscribe to MQTT topics and notify pluggable services.


#### Grafana
- [Grafana Map Panel] - Fork of the original Grafana Worldmap Panel with improved convenience, robustness and features.
- [grafanimate] - Animate timeseries data with Grafana.
- [grafana-wtf] - Grep through all Grafana entities in the spirit of git-wtf.


[Wetterdienst]: https://github.com/panodata/wetterdienst
[GribMagic]: https://github.com/earthobservations/gribmagic
[Luftdatenpumpe]: https://github.com/panodata/luftdatenpumpe
[phenodata]: https://github.com/hiveeyes/phenodata

[Kotori]: https://github.com/daq-tools/kotori
[Terkin]: https://github.com/hiveeyes/terkin-datalogger
[mqttwarn]: https://github.com/jpmens/mqttwarn

[Grafana Map Panel]: https://github.com/panodata/grafana-map-panel
[grafanimate]: https://github.com/panodata/grafanimate
[grafana-wtf]: https://github.com/panodata/grafana-wtf
