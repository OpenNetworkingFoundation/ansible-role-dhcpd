<!--
SPDX-FileCopyrightText: © 2020 Open Networking Foundation <support@opennetworking.org>
SPDX-License-Identifier: Apache-2.0
--!>
# dhcpd

Installs/configure a DHCP server and TFTP server

## dhcpd

Documentation:

- https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhcpd
- https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhcpdconf
- https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhcp-options

## tftpd

Documentation is scarce. Upstream source repo:

- https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git


## Requirements

Minimum ansible version: 2.9.5


## Example Playbook

```yaml
- hosts: all
  vars:
    dhcpd_interfaces:
      - eth0
    dhcpd_subnets:
      - subnet: "192.168.0.1/24"
        range: "192.168.0.128/25"
        dns_servers:
          - "192.168.0.1"
          - "192.168.0.2"
        dns_search:
          - "example.com"
        tftpd_server: "192.168.0.1"
        hosts:
          - name: "dns"
            ip_addr: "192.168.0.2"
            mac_addr: "a1:b2:c3:d4:e5:f6"

  roles:
    - dhcpd

```

## License and Author

© 2020 Open Networking Foundation <support@opennetworking.org>

License: Apache-2.0
