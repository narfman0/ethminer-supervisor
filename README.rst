===================
ethminer-supervisor
===================


.. image:: https://img.shields.io/pypi/v/ethminer-supervisor.svg
        :target: https://pypi.python.org/pypi/ethminer-supervisor

.. image:: https://img.shields.io/travis/narfman0/ethminer-supervisor.svg
        :target: https://travis-ci.org/narfman0/ethminer-supervisor

WIP Supervise ethminer daemon and restart process or machine when appropriate.

This assumes ethminer was set up using ansible-ethminer, where systemd manages
the ethminer.service process. This is required, since this is based on parsing
logs from sytemd.

Features
--------

* Restart process when process gets stuck
* Restart machine when graphics driver fails

Usage
-----

Install ethminer supervisor with::

    pip install ethminer-supervisor

Then hook up either supervisor or systemd

CLI
---

The command line interface may be used to run manually::

    ethminer_supervisor

License
-------

See LICENSE file for further licensing information