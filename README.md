# Awesome Censys Queries [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A collection of fascinating and bizarre [Censys Search](https://search.censys.io) queries.

## Table of Contents

- [Industrial Control Systems](#industrial-control-systems)
- [Internet of Things Devices](#internet-of-things-devices)
- [Security Applications](#security-applications)
- [Random Services](#random-services)

### Industrial Control Systems

#### Prismview (Samsung Electronic Billboards) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.tls.certificates.leaf_data.subject.common_name%3A+%22Prismview%22+or+services.http.response.headers.server%3A+%22Prismview+Player%22)

```dsl
services.tls.certificates.leaf_data.subject.common_name: "Prismview" or services.http.response.headers.server: "Prismview Player"
```

#### Gas Station Pump Controllers (ATGs) [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28services.port%3A+10001+and+services.banner%3A+%22IN-TANK+INVENTORY%22%29+or+services.service_name%3A+ATG)

```dsl
same_service(services.port: 10001 and services.banner: "IN-TANK INVENTORY") or services.service_name: ATG
```

### Internet of Things Devices

#### Roombas [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.tls.certificates.leaf_data.issuer.common_name%3A+%22Roomba+CA%22)

```dsl
services.tls.certificates.leaf_data.issuer.common_name: "Roomba CA"
```

#### Mein Automowers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.headers.Www_Authenticate%3A+%60Basic+realm%3D+%22Mein+Automower+%28Robonect+Hx%2B%29%22%60)

```dsl
services.http.response.headers.Www_Authenticate: `Basic realm= "Mein Automower (Robonect Hx+)"`
```

### Security Applications

#### Cobalt Strike Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.certificate%3A+%7B%2264257fc0fac31c01a5ccd816c73ea86e639260da1604d04db869bb603c2886e6%22%2C+%2287f2085c32b6a2cc709b365f55873e207a9caa10bffecf2fd16d3cf9d94d390c%22%7D+or+services.tls.certificates.leaf_data.issuer.common_name%3A+%22Major+Cobalt+Strike%22+or+services.tls.certificates.leaf_data.subject.common_name%3A+%22Major+Cobalt+Strike%22)

```dsl
services.certificate: {"64257fc0fac31c01a5ccd816c73ea86e639260da1604d04db869bb603c2886e6", "87f2085c32b6a2cc709b365f55873e207a9caa10bffecf2fd16d3cf9d94d390c"} or services.tls.certificates.leaf_data.issuer.common_name: "Major Cobalt Strike" or services.tls.certificates.leaf_data.subject.common_name: "Major Cobalt Strike"
```

#### Metasploit Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Metasploit%22+and+%28services.tls.certificates.leaf_data.subject.organization%3A+%22Rapid7%22+or+services.tls.certificates.leaf_data.subject.common_name%3A+%22MetasploitSelfSignedCA%22%29)

```dsl
services.http.response.html_title: "Metasploit" and (services.tls.certificates.leaf_data.subject.organization: "Rapid7" or services.tls.certificates.leaf_data.subject.common_name: "MetasploitSelfSignedCA")
```

### Random Services

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

## Credits

- [jakejarvis/awesome-shodan-queries](https://github.com/jakejarvis/awesome-shodan-queries)
