==========
freeNetGIS
==========

--------
¿Qué es?
--------

freeNetGIS significa free networks geographical information system (sistema de información geográfica para redes comunitarias), y como su nombre lo indica está orientado a dar soporte a redes comunitarias, incluyendo pero no limitándose a las redes inalámbricas libres.

Está inspirado en otros proyectos similares, entre los cuales pueden mencionarse:

    NodeShot -> Ver mapa
    BALLS -> Ver mapa
    FFSomething -> Ver mapa
    guifi.net -> Ver mapa

------------------------
Características técnicas
------------------------

freeNetGIS tiene una serie de características técnicas que lo diferencian de otros proyectos, entre las cuales se destacan:

Basado en el framework web django (GeoDjango)
=============================================

Se abstrae de las consultas geoespaciales y el manejo de tipos de datos geométricos, pudiendo utilizar como backend postgis, mysql, oracle y/o spatialite.

No está cerrado exclusivamente a una API privativa
==================================================

Utiliza OpenLayers para la visualización de mapas, que permite utilizar capas de distintos servidores al mismo tiempo:

    Open Street Maps – libre
    Google Maps – propietario
    Yahoo Maps – propietario
    Bing Maps – propietario

No necesita internet para funcionar
===================================

Al utilizar bases de datos que permiten almacenar objetos geográficos, se pueden importar vectores geoespaciales (por ejemplo shapefiles), por lo que no es necesario tener conectividad a internet para poder visualizar capas en el mapa.

Está enfocado en la descentralización
=====================================

Se están desarrollando técnicas de sincronización utilizando el protocolo pubsubhubbub, esto permite sincronizar la aplicación con instancias del mismo sistema, y con otros sistemas que utilicen un estándar de publicación en común, como por ejemplo GeoRSS.

-------------------
Estado del proyecto
-------------------

Actualmente el proyecto se encuentra en desarrollo, estamos abiertos a cualquier desarrollador que tenga ganas de realizar aportes.
