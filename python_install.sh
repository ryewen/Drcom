#!/bin/bash

opkg update

opkg remove git

opkg install python-openssl python-codecs

rm -rf /opt/app/* /opt/etc/* /opt/lib/libcurl* /opt/sbin/* /opt/var/* /opt/bin/curl /opt/bin/find /opt/bin/opkg /opt/bin/xargs /opt/share/* /opt/bin/htop /opt/bin/cpulimit /opt/lib/opkg
