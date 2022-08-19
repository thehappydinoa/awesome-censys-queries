# Awesome Censys Queries [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A collection of fascinating and bizarre [Censys Search](https://search.censys.io) queries.

<!-- markdownlint-disable MD033 -->
<p align="center">
    <img src="./images/search.censys.io.png" alt="Censys Search" width="500px" />
</p>
<!-- markdownlint-enable MD033 -->

## Table of Contents

- [Industrial Control Systems](#industrial-control-systems)
- [Internet of Things Devices](#internet-of-things-devices)
- [Security Applications](#security-applications)
- [Databases](#databases)
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

#### WinAQMS Environmental Monitor [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.banner%3A+%22WinAQMS+Data+Server%22)

```dsl
services.banner: "WinAQMS Data Server"
```

#### [Emerson Site Supervisor](https://www.emerson.com/en-us/site-supervisor-5385648A) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Emerson+Site+Supervisor%22)

```dsl
services.http.response.html_title: "Emerson Site Supervisor"
```

#### [Nethix Wireless Controller](https://nethix.com/en/) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.headers.set_cookie%3A+%22NethixSession%22)

```dsl
services.http.response.headers.set_cookie: "NethixSession"
```

### Security Applications

#### Cobalt Strike Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.certificate%3A+%7B%2264257fc0fac31c01a5ccd816c73ea86e639260da1604d04db869bb603c2886e6%22%2C+%2287f2085c32b6a2cc709b365f55873e207a9caa10bffecf2fd16d3cf9d94d390c%22%7D+or+services.tls.certificates.leaf_data.issuer.common_name%3A+%22Major+Cobalt+Strike%22+or+services.tls.certificates.leaf_data.subject.common_name%3A+%22Major+Cobalt+Strike%22+or+services.jarm.fingerprint%3A+%7B%2207d14d16d21d21d07c42d41d00041d24a458a375eef0c576d23a7bab9a9fb1%22%2C+%2207d14d16d21d21d00042d41d00041de5fb3038104f457d92ba02e9311512c2%22%7D)

```dsl
services.certificate: {
    "64257fc0fac31c01a5ccd816c73ea86e639260da1604d04db869bb603c2886e6",
    "87f2085c32b6a2cc709b365f55873e207a9caa10bffecf2fd16d3cf9d94d390c"
}
or services.tls.certificates.leaf_data.issuer.common_name: "Major Cobalt Strike"
or services.tls.certificates.leaf_data.subject.common_name: "Major Cobalt Strike"
or services.jarm.fingerprint: {
    "07d14d16d21d21d07c42d41d00041d24a458a375eef0c576d23a7bab9a9fb1",
    "07d14d16d21d21d00042d41d00041de5fb3038104f457d92ba02e9311512c2"
}
```

#### Metasploit Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Metasploit%22+and+%28services.tls.certificates.leaf_data.subject.organization%3A+%22Rapid7%22+or+services.tls.certificates.leaf_data.subject.common_name%3A+%22MetasploitSelfSignedCA%22%29+or+services.jarm.fingerprint%3A+%7B07d14d16d21d21d00042d43d000000aa99ce74e2c6d013c745aa52b5cc042d%2C+07d14d16d21d21d07c42d43d000000f50d155305214cf247147c43c0f1a823%7D)

```dsl
services.http.response.html_title: "Metasploit" and (
    services.tls.certificates.leaf_data.subject.organization: "Rapid7"
    or services.tls.certificates.leaf_data.subject.common_name: "MetasploitSelfSignedCA"
)
or services.jarm.fingerprint: {
    "07d14d16d21d21d00042d43d000000aa99ce74e2c6d013c745aa52b5cc042d",
    "07d14d16d21d21d07c42d43d000000f50d155305214cf247147c43c0f1a823"
}
```

#### Nessus Scanner Servers [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=services.http.response.headers.server%3DNessusWWW+or+services.tls.certificates.leaf_data.subject.organizational_unit%3A+%22Nessus+Server%22)

```dsl
services.http.response.headers.server=NessusWWW
or services.tls.certificates.leaf_data.subject.organizational_unit: "Nessus Server"
```

#### NTOP Network Analyzers [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=services.http.response.html_title%3D%22Welcome+to+ntopng%22+or+same_service%28services.http.response.html_title%3A+%22Global+Traffic+Statistics%22+and+services.http.response.headers.server%3A+%22ntop%2F*%22%29)

```dsl
services.http.response.html_title="Welcome to ntopng"
or same_service(
    services.http.response.html_title: "Global Traffic Statistics"
    and services.http.response.headers.server: "ntop/*")
```


#### [Merlin C2](https://github.com/Ne0nd0g/merlin) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.jarm.fingerprint%3A+29d21b20d29d29d21c41d21b21b41d494e0df9532e75299f15ba73156cee38)

```dsl
services.jarm.fingerprint: "29d21b20d29d29d21c41d21b21b41d494e0df9532e75299f15ba73156cee38"
```

#### [Deimos C2](https://github.com/DeimosC2/DeimosC2) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.jarm.fingerprint%3A+00000000000000000041d00000041d9535d5979f591ae8e547c5e5743e5b64)

```dsl
services.jarm.fingerprint: "00000000000000000041d00000041d9535d5979f591ae8e547c5e5743e5b64"
```

#### [EvilGinx2](https://github.com/kgretzky/evilginx2) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.jarm.fingerprint%3A+20d14d20d21d20d20c20d14d20d20daddf8a68a1444c74b6dbe09910a511e6)

```dsl
services.jarm.fingerprint: "20d14d20d21d20d20c20d14d20d20daddf8a68a1444c74b6dbe09910a511e6"
```

### Databases

#### [Exposed CouchDB Servers](https://couchdb.apache.org/) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.body%3A+%27%22couchdb%22%3A+%22Welcome%22%27)

```dsl
services.http.response.body: '"couchdb": "Welcome"'
```

### Random Services

#### shell2http [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=services.http.response.html_title%3A+%22shell2http%22&cursor=eyJBZnRlciI6WyIyMS4yOTIxMzEiLCJBaTJPMzhHWlRtN2ZrUTFCdERPOUp3PT0iXSwiUmV2ZXJzZSI6ZmFsc2UsIlNlZWQiOjB9)

```dsl
services.http.response.html_title: "shell2http"
```

#### Busybox Shells [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28services.banner%3A+%22Enter+%27help%27+for+a+list+of+built-in+commands%22+and+services.service_name%3A+TELNET%29+and+services.truncated%3A+false)

```dsl
same_service(services.banner: "Enter 'help' for a list of built-in commands" and services.service_name: TELNET) and services.truncated: false
```

#### Services Listening on Port 22 that are not SSH [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28not+services.service_name%3A+%7BSSH%7D+and+services.port%3A+22+and+not+services.banner%3A+%7B%22Connection+refused%22%2C+%22SSH-%22%2C+%22Exceeded+MaxStartups%22%2C+%22Too+many+users%22%2C+%22Connection+closed+by+server%22%7D%29+and+services.truncated%3A+false)

```dsl
same_service(
    not services.service_name: {SSH}
    and services.port: 22
    and not services.banner: {"Connection refused", "SSH-", "Exceeded MaxStartups", "Too many users", "Connection closed by server"}
)
and services.truncated: false
```

#### Services Listening on 80 or 443 that are not HTTP or HTTPS (or UNKNOWN with TLS) [&#x2192;](https://search.censys.io/search?resource=hosts&q=not+same_service%28services.port%3A+443+and+services.name%3A+UNKNOWN+and+services.tls.certificates.leaf_data.subject_dn%3A+*+%29+and+same_service%28services.port%3A+%7B80%2C+443%7D+and+not+services.service_name%3A+%7BKUBERNETES%2C+ANYCONNECT%2C+OPENVPN%2C+HTTP%7D+and+not+services.banner%3A+%E2%80%9CHTTP%2F%E2%80%9D+%29++and+services.truncated%3A+false)

```dsl
not same_service(
    services.port: 443
    and services.name: UNKNOWN
    and services.tls.certificates.leaf_data.subject_dn: *
)
and same_service(
    services.port: {80, 443}
    and not services.service_name: {KUBERNETES, ANYCONNECT, OPENVPN, HTTP}
    and not services.banner: “HTTP/”
)
and services.truncated: false
```

#### Services Listening on 53 that are not DNS [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28services.port%3A+53+and+not+services.service_name%3A+DNS%29+and+services.truncated%3A+false)

```dsl
same_service(services.port: 53 and not services.service_name: DNS) and services.truncated: false
```

#### Unauthenticated Redis Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.redis.ping_response%3A+%22PONG%22)

```dsl
services.redis.ping_response: "PONG"
```

#### Misconfigured Kubernetes Installations [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.kubernetes.pod_names%3A+*)

```dsl
services.kubernetes.pod_names: *
```

#### Directory Listing [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Index+of+%2F%22)

```dsl
services.http.response.html_title: "Index of /"
```

#### Hosts that identify as US government or military [&#x2192;](https://search.censys.io/search?resource=hosts&q=dns.names%3A+*.gov+or+dns.names%3A+*.mil+or+name%3A+*.gov+or+name%3A+*.mil)

```dsl
dns.names: *.gov or dns.names: *.mil or name: *.gov or name: *.mil
```

#### Hosts emitting GNSS payloads [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.banner%3A+%22%24GPRMC%22)

```dsl
services.banner: "$GPRMC"
```

#### [Mongo Express Admin Interface](https://github.com/mongo-express/mongo-express) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Home+-+Mongo+Express%22)

```dsl
services.http.response.html_title: "Home - Mongo Express"
```

#### Misconfigured WordPress [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.body%3A+%22The+wp-config.php+creation+script+uses+this+file%22)

```dsl
services.http.response.body: "The wp-config.php creation script uses this file"
```

#### [North Korean Subnets](https://www.vox.com/2014/12/22/7435625/north-korea-internet) [&#x2192;](https://search.censys.io/search?resource=hosts&q=ip%3A+%7B175.45.176.0%2F22%2C+210.52.109.0%2F24%2C+77.94.35.0%2F24%7D)

```dsl
ip: {175.45.176.0/22, 210.52.109.0/24, 77.94.35.0/24}
```

#### Honepots Hosts [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.truncated%3A+true)

```dsl
services.truncated: true
```

#### [Traefik Dashboards](https://github.com/traefik/traefik) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.request.uri%3A+%22*%2Fdashboard%2F%22+and+services.http.response.html_title%3DTraefik%29)

```dsl
same_service(services.http.request.uri: "*/dashboard/" and services.http.response.html_title=Traefik)
```

#### [Weave Scope](https://www.weave.works/oss/scope/) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.html_title%3D%22Weave+Scope%22+and+services.http.response.body%3D%22*WEAVEWORKS_CSRF*%22%29)

```dsl
same_service(services.http.response.html_title="Weave Scope" and services.http.response.body="*WEAVEWORKS_CSRF*")
```

#### Prometheus Node Exporters [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.html_title%3A+%22node+exporter%22+and+services.http.response.body%3A+%22%2Fmetrics%22%29)

```dsl
same_service(services.http.response.html_title: "node exporter" and services.http.response.body: "/metrics")
```

#### [VictoriaMetrics VMAgent](https://docs.victoriametrics.com/vmagent.html) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=INCLUDE&q=services.http.response.body%3A+%22%3Ch2%3Evmagent%3C%2Fh2%3E%22)

```dsl
services.http.response.body: "<h2>vmagent</h2>"
```



## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

## Credits

- [jakejarvis/awesome-shodan-queries](https://github.com/jakejarvis/awesome-shodan-queries)
- [woj-ciech/Kamerka-GUI](https://github.com/woj-ciech/Kamerka-GUI)
- [salesforce/jarm](https://github.com/salesforce/jarm)
- [cedowens/C2-JARM](https://github.com/cedowens/C2-JARM)
