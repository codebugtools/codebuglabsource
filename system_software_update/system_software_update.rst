.. Updating CodeBug Connect's System Software
.. (c) OpenLX SP Ltd 2022 All rights reserved

:difficulty: easy

.. title:: Updating CodeBug Connect's system software

.. TODO change title image

.. titleimage:: gps-circle2.png

.. codelab:: Introduction

    CodeBug Connect has a tiny 'Operating System' that does various tasks in the background. Every so often we will provide an update that might add extra functionality or fix bugs.
    
    .. note:: You're in control! CodeBug Connect will never automatically update itself without your permission. You can chose which version you want it to update to.

.. codelab:: Prepare for the update

    .. warning:: Check everything on the list before proceeding!

    Before updating your CodeBug Connect, ensure:

    #. You have a backup of any programs and data on your CodeBug Connect, just in case!
    #. You're powering your CodeBug Connect from a good quality USB power supply.
    #. Your CodeBug Connect has a :codeguide:`WiFi connection setup<setting-up-wifi>` and...
    #. it's been :codeguide:`adopted<adopting-your-codebug>` on the CodeBug Website.

    .. note:: While we do our best not to introduce changes that will cause your programs to break, you may have to make slight updates to keep them working after the update.


.. codelab:: Request update from your CodeBug Connect

    #. Bring up a terminal, for instance via the onboard web IDE (over USB serial).

       .. image:: img/webterminal.png
        :alt: Terminal in CodeBug Connect web IDE
    
    
    #. enter the following:

       .. code-block:: python

        import remote_manage
        remote_manage.reboot_into_update()

    #. Read and follow the instructions displayed. Enter ``yes`` if appropriate.

    #. When prompted, remove the power (unplug all connections to CodeBug Connect).

.. codelab:: Power up and wait for update to download

    .. warning:: Once the update begins, do not disconnect your CodeBug Connect during an update as permanent damage to the file system may occur!

    #. Wait for at least 2 seconds and then reconnect power.

    #. CodeBug Connect will flash a light yellow searching for WiFi. Note the symbol is backwards compared with CodeBug Connect's normal searching for WiFi symbol.

       .. image:: img/UpdateScan1.png
        :alt: Scanning for WiFi1

       .. image:: img/UpdateScan2.png
        :alt: Scanning for WiFi2

       .. image:: img/UpdateScan3.png
        :alt: Scanning for WiFi3

    #. Once network has been found CodeBug Connect will indicate successful WiFi connection.

       .. figure:: img/WiFiConnectSuccess.png
            :alt: WiFi connected
            :align: center

    #. CodeBug Connect will attempt to connect to the update server. If successful, the connection icon will be light purple.

           .. figure:: img/connectionSuccess.png
            :alt: Successful connection
            :align: center

    #. Beginning from the top left, the LED display will fill with yellow dots to indicate download process. This sometimes has a slow start so be patient.

       .. image:: img/downloading1.png
        :alt: Download beginning

       .. image:: img/downloading7.png
        :alt: Download partial

       .. image:: img/downloadDone.png
        :alt: Download complete

    #. CodeBug will check the download for errors. If successful, a green smiling face will be displayed.

       .. figure:: img/smile.png
        :alt: Smile indicating firmware update success
        :align: center

       .. warning:: Your CodeBug Connect may still be cleaning up the file system, so do not remove power yet!

.. codelab:: Wait for reboot

    .. warning:: Wait until CodeBug Connect reboots before removing power!

    #. Wait at least 10 seconds after your CodeBug Connect has completed rebooting after the update.

    #. Once rebooted your Codebug Connect should be running the updated 'Operating System'.

    #. If you have a CodeBug Connect from the original kickstarter batch, and this is the first update, you may have to re-setup WiFi.

    That's it, you're ready to check out the new features brought by the update.