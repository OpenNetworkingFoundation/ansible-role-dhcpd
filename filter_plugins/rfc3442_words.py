#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2021 Open Networking Foundation <support@opennetworking.org>
# SPDX-License-Identifier: Apache-2.0

# rfc3442_words.py
# Input: a dict containing a router ip and multiple CIDR format routes
# Output a list of octets to be appended to option 121 RFC3442 Classless routes option
#
# References:
#  https://tools.ietf.org/html/rfc3442
#  https://netaddr.readthedocs.io/en/latest/index.html

from __future__ import absolute_import
import netaddr


class FilterModule(object):
    def filters(self):
        return {
            "rfc3442_words": self.rfc3442_words,
        }

    def rfc3442_words(self, var):

        words = []

        router = var["ip"]
        router_words = netaddr.IPNetwork(router).network.words

        for r3442r in var["rfc3442routes"]:

            # add prefix length
            prefixlen = netaddr.IPNetwork(r3442r).prefixlen
            words.append(prefixlen)

            # add only the relevant portion of the address, depending ow words
            (o1, o2, o3, o4) = netaddr.IPNetwork(r3442r).network.words
            if prefixlen >= 25:
                words += [o1, o2, o3, o4]
            elif prefixlen >= 17:
                words += [o1, o2, o3]
            elif prefixlen >= 9:
                words += [o1, o2]
            elif prefixlen >= 1:
                words += [o1]
            # no additional words if prefixlen == 0

            # add router address
            words += list(router_words)

        return words


# test when running standalone outside of Ansible
if __name__ == "__main__":

    example = {
        "ip": "192.168.1.10",
        "rfc3442routes": [
            "10.0.0.0/8",
            "172.16.0.0/16",
            "172.17.0.0/22",
            "172.31.10.0/25",
        ],
    }

    jfilter = FilterModule()

    words = jfilter.rfc3442_words(example)

    print(words)

    # verify correct functionality
    assert words == [
        8,
        10,
        192,
        168,
        1,
        10,
        16,
        172,
        16,
        192,
        168,
        1,
        10,
        22,
        172,
        17,
        0,
        192,
        168,
        1,
        10,
        25,
        172,
        31,
        10,
        0,
        192,
        168,
        1,
        10,
    ]
