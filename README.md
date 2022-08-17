# Awesome Censys Queries [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A collection of fascinating and bizarre [Censys Search](https://search.censys.io) queries.

<!-- markdownlint-disable MD033 -->
<center>
    <img src="./images/search.censys.io.png" alt="Censys Search" width="500px" />
</center>
<!-- markdownlint-enable MD033 -->

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


#### WinAQMS Environmental Monitor [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=services.banner%3A%22WinAQMS+Data+Server%22) 

```dsl
services.banner:"WinAQMS Data Server"
```

#### [Emerson Site Supervisor](https://www.emerson.com/en-us/site-supervisor-5385648A) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.http.response.html_title%3D%22Emerson+Site+Supervisor%22)

```dsl
services.http.response.html_title="Emerson Site Supervisor"
```

### Security Applications

#### Cobalt Strike Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.certificate%3A+%7B%2264257fc0fac31c01a5ccd816c73ea86e639260da1604d04db869bb603c2886e6%22%2C+%2287f2085c32b6a2cc709b365f55873e207a9caa10bffecf2fd16d3cf9d94d390c%22%7D+or+services.tls.certificates.leaf_data.issuer.common_name%3A+%22Major+Cobalt+Strike%22+or+services.tls.certificates.leaf_data.subject.common_name%3A+%22Major+Cobalt+Strike%22)

```dsl
services.certificate: {
    "64257fc0fac31c01a5ccd816c73ea86e639260da1604d04db869bb603c2886e6",
    "87f2085c32b6a2cc709b365f55873e207a9caa10bffecf2fd16d3cf9d94d390c"
}
or services.tls.certificates.leaf_data.issuer.common_name: "Major Cobalt Strike"
or services.tls.certificates.leaf_data.subject.common_name: "Major Cobalt Strike"
```

#### Metasploit Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Metasploit%22+and+%28services.tls.certificates.leaf_data.subject.organization%3A+%22Rapid7%22+or+services.tls.certificates.leaf_data.subject.common_name%3A+%22MetasploitSelfSignedCA%22%29)

```dsl
services.http.response.html_title: "Metasploit" and (
    services.tls.certificates.leaf_data.subject.organization: "Rapid7"
    or services.tls.certificates.leaf_data.subject.common_name: "MetasploitSelfSignedCA"
)
```

### Random Services

#### shell2http [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=services.http.response.html_title%3A+%22shell2http%22&cursor=eyJBZnRlciI6WyIyMS4yOTIxMzEiLCJBaTJPMzhHWlRtN2ZrUTFCdERPOUp3PT0iXSwiUmV2ZXJzZSI6ZmFsc2UsIlNlZWQiOjB9)

```dsl
services.http.response.html_title: "shell2http"
```

#### Busybox Shells [&#x2192;](https://search.censys.io/search?resource=hosts&q=%28services.banner%3A+%22Enter+%27help%27+for+a+list+of+built-in+commands%22+and+services.truncated%3A+false%29+)

```dsl
(same_service(services.banner: "Enter 'help' for a list of built-in commands" and services.service_name=TELNET) and services.truncated: false)
```

#### Services Listening on Port 22 that are not SSH [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=same_service%28not+services.service_name%3D%7BSSH%7D+and+services.port%3D22+and+not+services.banner%3A+%7B%22Connection+refused%22%2C+%22SSH-%22%2C+%22Exceeded+MaxStartups%22%2C+%22Too+many+users%22%2C+%22Connection+closed+by+server%22%7D%29+and+services.truncated%3Dfalse)

```dsl
same_service(
    not services.service_name={SSH}
    and services.port=22 
    and not services.banner: {"Connection refused", "SSH-", "Exceeded MaxStartups", "Too many users", "Connection closed by server"}
)
and services.truncated=false
```

#### Services Listening on 80 or 443 that are not HTTP or HTTPS (or UNKNOWN with TLS) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=not+same_service%28+services.port%3D443+and+services.name%3DUNKNOWN++and+services.tls.certificates.leaf_data.subject_dn%3A*+%29+and+same_service%28+++++services.port%3D%7B80%2C443%7D+++++and+not+services.service_name%3D%7BKUBERNETES%2CANYCONNECT%2COPENVPN%2CHTTP%7D++and+not+services.banner%3A+%E2%80%9CHTTP%2F%E2%80%9D+%29)

```dsl
not same_service(
    services.port=443
    and services.name=UNKNOWN
    and services.tls.certificates.leaf_data.subject_dn:*
) 
and same_service(
    services.port={80,443} 
    and not services.service_name={KUBERNETES,ANYCONNECT,OPENVPN,HTTP}
    and not services.banner: “HTTP/”
) 
and services.truncated=false
```

#### Services Listening on 53 that are not DNS [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RANDOM&per_page=25&virtual_hosts=EXCLUDE&q=same_service%28services.port%3D53+and+not+services.service_name%3DDNS%29+and+services.truncated%3Dfalse)

```dsl
same_service(services.port=53 and not services.service_name=DNS) and services.truncated=false
```

#### Unauthenticated Redis Servers [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.redis.ping_response%3DPONG)

```dsl
services.redis.ping_response=PONG
```

#### Misconfigured Kubernetes Installations [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.kubernetes.pod_names%3A*)

```dsl
services.kubernetes.pod_names:*
```

#### Directory Listing [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.http.response.html_title%3A+%22Index+of+%2F%22)

```dsl
services.http.response.html_title: "Index of /"
```

#### Hosts that identify as US government or military [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=dns.names%3A+*.gov+or+dns.names%3A+*.mil+or+name%3A+*.gov+or+name%3A+*.mil) 

```dsl
dns.names: *.gov or dns.names: *.mil or name: *.gov or name: *.mil
```

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

## Credits

- [jakejarvis/awesome-shodan-queries](https://github.com/jakejarvis/awesome-shodan-queries)
