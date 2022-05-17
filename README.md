# dhcpd

Installs/configure a DHCP server and TFTP server

A few assumptions are made by this role:

- If `routers` is not set in the `subnet` dictionary (within `dhcpd_subnets`),
  then the first usable address is set as the router.

- If `routers` is set and has a list of IP addresses as a part of the
  `rfc3442routes` key, RFC3442 classless static routes (option 121) will be
  added in addition to the standard `routers` (option 3)

Supports using PXE to load both traditional BIOS and EFI payloads, tested
primarily with `iPXE`.

## Configuration docs

dhcpd - ISC's docs:

- https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhcpd
- https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhcpdconf
- https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhcp-options

tftpd - Documentation is scarce. Upstream source repo:

- https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git

Also supports OpenBSD dhcpd (fork of ISC) and tftpd (BSD), which has some
difference in configuration/behavior - missing conditionals, additional option
definitions, etc.

## Reference docs

DHCP:

- [RFC2131 - DHCP Protocol](https://tools.ietf.org/html/rfc2131)
- [RFC2132 - DHCP Options](https://tools.ietf.org/html/rfc2132)
- [RFC3442 - Classless Static routes](https://tools.ietf.org/html/rfc3442)

TFTP:

- [RFC1350 - TFTP protocol v2](https://tools.ietf.org/html/rfc1350)

[iPXE Chainloading](https://ipxe.org/howto/chainloading)

## Requirements

Minimum ansible version: 2.9.5


## Example Playbook

```yaml
- hosts: all
  vars:
    dhcpd_interfaces:
      - eth0
    dhcpd_subnets:
      "192.168.0.1/24":
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
        routers:
          - ip: "192.168.0.1"
  roles:
    - dhcpd

```
### ToDo

Add classless static route support for OpenBSD - see dhcp-options(5) on that
system.

## License and Author

© 2020 Open Networking Foundation <support@opennetworking.org>

License: Apache-2.0
