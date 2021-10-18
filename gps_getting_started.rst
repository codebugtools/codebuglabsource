.. how to get started with the gps
.. (c) OpenLX SP Ltd 2021 All rights reserved

:difficulty: easy

.. title:: Get started with the GPS add-on

.. TODO change title image

.. titleimage:: img/gps.jpg

.. codelab:: Introduction

   This will show how to setup the GPS add-on on a CodeBug Connect.

   .. important:: You need the latest eMicroPython OS running on your CodeBug Connect before you use it with the GPS add-on. 

   .. TODO Link to update guide

   GPS works by receiving radio signals from satellites orbiting the earth. Before a position can be found it needs to receive information from multiple satellites. When first powered on, a lot of information needs to be received before the signal 'locks on'. Buildings, trees, etc. which block signals will make it harder to get a lock.
   
   As such you'll have best results when outdoors with a clear view of most of the sky.

.. codelab:: Plugging In
   .. warning:: Take care when plugging in add-ons. Always disconnect the power, check all the pins are aligned and never use excessive force.

   #. Ensure the power is disconnected
   #. Make sure everything is the right way up. The square GPS antenna should be on the same side as CodeBug Connect display.
   #. Check all the pins are aligned and gently slide in.
   #. Power up your CodeBug Connect
   
   The GPS add-on will start looking for satellites as soon as it is powered on. The small LED will flash once a second when it has got a good lock.

.. TODO add image or animation

.. codelab:: Running code

   .. important:: Check your CodeBug Connect eMicroPython version.
      This code will only work with eMicroPython later than version 1.2.

   Run the following code:

   .. literalinclude:: gps_test.py
   
   GPS positions are given as a latitude and longitude. Latitude describes how far North or South (with 0 being the equator and increasing going north). Longitude describes how far East or West of a line in Greenwich, London, UK.

   Latitudes and longitudes are measured in degrees. These degrees can be split up in different ways, as decimals, or as minutes and decimal-minutes, or as minutes, seconds and decimal seconds.

   To get the latitude in degrees minutes and decimal degrees:

   ``gps.gps_sensor.lat``

   You'll see a result in the following format:

   ``(53, 28.7694)``

   To get the longitude in degrees minutes and decimal degrees:

   ``gps.gps_sensor.lon``

   You'll see a result in the following format:

   ``(-2, 14.7069)``

   This means the GPS has position is 53° 28.7694, -2° 14.7069. Enter the coordinates into your favourite online map e.g. Google Maps and you should see your position shown on the map.

   If you'd prefer the position as decimal degrees use the conversion function:

   ``gps.deg_decmin_to_dec_deg()``

.. codelab:: Further ideas

   Now you've seen how to get started with the GPS add-on there's lots of possibilities. You could:

   *  Record the position every few seconds into a file to log your cycle
   *  Calculate your distance and angle from an object and display an arrow on CodeBug Connect's LED that points to it
   *  Use the precision of GPS timing to accurately set the clock on CodeBug Connect

   Check out the reference documentation for the add-on to learn more.
