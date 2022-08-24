# Awesome Censys Queries

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub contributors](https://img.shields.io/github/contributors/thehappydinoa/awesome-censys-queries)](https://github.com/thehappydinoa/awesome-censys-queries/graphs/contributors)
[![GitHub Repo stars](https://img.shields.io/github/stars/thehappydinoa/awesome-censys-queries)](https://github.com/thehappydinoa/awesome-censys-queries)
[![License](https://img.shields.io/github/license/thehappydinoa/awesome-censys-queries)](#license)

A collection of fascinating and bizarre [Censys Search](https://search.censys.io) queries.

<!-- markdownlint-disable MD033 -->
<p align="center">
    <img src="./images/search.censys.io.png" alt="Censys Search" width="500px" />
</p>

## Contributing

Found an awesome query? [Submit it here](https://github.com/thehappydinoa/awesome-censys-queries/issues/new?assignees=thehappydinoa&labels=query+submissions&template=query-submission.md&title=)

Interested in contributing in another way? [See the contributing guidelines](CONTRIBUTING.md)

## Table of Contents

- [Industrial Control Systems](#industrial-control-systems)
- [Internet of Things Devices](#internet-of-things-devices)
- [Security Applications](#security-applications)
- [Databases](#databases)
- [Game Servers](#game-servers)
- [Dashboards](#dashboards)
- [Random Services](#random-services)

### Industrial Control Systems

#### Prismview (Samsung Electronic Billboards) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.tls.certificates.leaf_data.subject.common_name%3A+%22Prismview%22+or+services.http.response.headers.server%3A+%22Prismview+Player%22)

```dsl
services.tls.certificates.leaf_data.subject.common_name: "Prismview" or services.http.response.headers.server: "Prismview Player"
```

<details>
    <summary markdown="span">Screenshot</summary>
    <img src="./images/prismview.png" alt="Prismview" width="300px" />
</details>

#### Gas Station Pump Controllers (ATGs) [&#x2192;](https://search.censys.io/search?resource=hosts&q=%28same_service%28port%3A+10001+and+banner%3A+%22IN-TANK+INVENTORY%22%29+or+services.service_name%3A+ATG%29+and+services.truncated%3A+false)

```dsl
(same_service(port: 10001 and banner: "IN-TANK INVENTORY")
or services.service_name: ATG) and services.truncated: false
```

<details>
    <summary markdown="span">Screenshot</summary>
    <img src="./images/atg.png" alt="ATG" width="300px" />
</details>

#### Electric Vehicle Chargers [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28http.response.headers.server%3A+%22gSOAP%2F2.8%22+and+http.response.headers.content_length%3A+583%29)

```dsl
same_service(http.response.headers.server: "gSOAP/2.8" and http.response.headers.content_length: 583)
```

#### [Carel PlantVisor](https://www.carel.com/product/plantvisor) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22CAREL+Pl%40ntVisor%22)

```dsl
services.http.response.html_title: "CAREL Pl@ntVisor"
```

#### [C4 Max Vehicle GPS](https://wiki.neweagle.net/ProductDocumentation/Telematics/C4MAX_datasheet.pdf) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.banner%3A+%22%5B1m%5B35mWelcome+on+console%22)

```dsl
services.banner: "[1m[35mWelcome on console"
```

#### GaugeTech Electricity Meters [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.headers.server%3A+%22EIG+Embedded+Web+Server%22)

```dsl
services.http.response.headers.server: "EIG Embedded Web Server"
```

<details>
    <summary markdown="span">Screenshot</summary>
    <img src="./images/gaugetech.png" alt="GaugeTech" width="300px" />
</details>

### Internet of Things Devices

#### Roombas [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.tls.certificates.leaf_data.issuer.common_name%3A+%22Roomba+CA%22)

```dsl
services.tls.certificates.leaf_data.issuer.common_name: "Roomba CA"
```

#### Mein Automowers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.headers.Www_Authenticate%3A+%60Basic+realm%3D+%22Mein+Automower+%28Robonect+Hx%2B%29%22%60)

```dsl
services.http.response.headers.Www_Authenticate: `Basic realm= "Mein Automower (Robonect Hx+)"`
```

#### WinAQMS Environmental Monitor [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.banner%3A+%22WinAQMS+Data+Server%22+and+services.truncated%3A+false)

```dsl
services.banner: "WinAQMS Data Server" and services.truncated: false
```

#### [Emerson Site Supervisor](https://www.emerson.com/en-us/site-supervisor-5385648A) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Emerson+Site+Supervisor%22)

```dsl
services.http.response.html_title: "Emerson Site Supervisor"
```

<details>
    <summary markdown="span">Screenshot</summary>
    <img src="./images/emerson-site-supervisor.png" alt="Emerson" width="500px" />
</details>

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

#### Nessus Scanner Servers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.headers.server%3A+%22NessusWWW%22+or+services.tls.certificates.leaf_data.subject.organizational_unit%3A+%22Nessus+Server%22)

```dsl
services.http.response.headers.server: "NessusWWW"
or services.tls.certificates.leaf_data.subject.organizational_unit: "Nessus Server"
```

#### NTOP Network Analyzers [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.html_title%3A+%22Welcome+to+ntopng%22+or+same_service%28services.http.response.html_title%3A+%22Global+Traffic+Statistics%22+and+services.http.response.headers.server%3A+%22ntop%2F*%22%29)

```dsl
services.http.response.html_title: "Welcome to ntopng"
or same_service(
    services.http.response.html_title: "Global Traffic Statistics"
    and services.http.response.headers.server: "ntop/*"
)
```

#### [Merlin C2](https://github.com/Ne0nd0g/merlin) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.jarm.fingerprint%3A+29d21b20d29d29d21c41d21b21b41d494e0df9532e75299f15ba73156cee38)

```dsl
services.jarm.fingerprint: "29d21b20d29d29d21c41d21b21b41d494e0df9532e75299f15ba73156cee38"
```

#### [Mythic C2](https://github.com/its-a-feature/Mythic) [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28port%3A+7443+and+tls.certificates.leaf_data.subject.organization%3A+%22Mythic%22%29)

```dsl
same_service(port: 7443 and tls.certificates.leaf_data.subject.organization: "Mythic")
```

> **Note**: When using the `same_service` operator, the initial `services.` prefix is optional.

#### [Deimos C2](https://github.com/DeimosC2/DeimosC2) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.jarm.fingerprint%3A+00000000000000000041d00000041d9535d5979f591ae8e547c5e5743e5b64)

```dsl
services.jarm.fingerprint: "00000000000000000041d00000041d9535d5979f591ae8e547c5e5743e5b64"
```

#### [Covenant C2](https://github.com/cobbr/Covenant) [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28http.response.body%3A+%22Blazor%22+and+tls.certificates.leaf_data.issuer.common_name%3A+%22Covenant%22%29)

```dsl
same_service(http.response.body: "Blazor" and tls.certificates.leaf_data.issuer.common_name: "Covenant")
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

### Dashboards

#### [cAdvisor Dashboards](https://github.com/google/cadvisor) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RANDOM&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.html_title%3D%60cAdvisor+-+%2F%60+and+services.http.response.status_code%3D200+and+services.http.request.uri%3D%22*%2Fcontainers%2F%22%29)

```dsl
same_service(
    services.http.response.html_title=`cAdvisor - /`
    and services.http.response.status_code=200
    and services.http.request.uri="*/containers/"
)
```

#### [HashiCorp Consul Dashboards](https://www.consul.io/) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RANDOM&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.html_title%3D%60Consul+by+HashiCorp%60+and+services.http.request.uri%3A+%22*%2Fui%2F%22%29)

```dsl
same_service(
    services.http.response.html_title=`Consul by HashiCorp`
    and services.http.request.uri: "*/ui/"
)
```

#### [Netdata Dashboards](https://www.netdata.cloud/) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RANDOM&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.headers.Server%3D%22Netdata+Embedded+HTTP*%22+and+services.http.response.html_title%3D%22netdata+dashboard%22%29)

```dsl
same_service(
    services.http.response.headers.Server="Netdata Embedded HTTP*"
    and services.http.response.html_title="netdata dashboard"
)
```

#### Rancher Dashboards [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RANDOM&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.headers.unknown.name%3A+%22X-Rancher-Version%22+and+services.http.response.html_title%3A+%22Loading%26hellip%3B%22%29)

```dsl
same_service(
    services.http.response.headers.unknown.name: "X-Rancher-Version"
    and services.http.response.html_title: "Loading&hellip;"
)
```

#### [Traefik Dashboards](https://github.com/traefik/traefik) [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28services.http.request.uri%3A+%22*%2Fdashboard%2F%22+and+services.http.response.html_title%3A+%22Traefik%22%29)

```dsl
same_service(services.http.request.uri: "*/dashboard/" and services.http.response.html_title: "Traefik")
```

#### [Weave Scope](https://www.weave.works/oss/scope/) [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28services.http.response.html_title%3A+%22Weave+Scope%22+and+services.http.response.body%3D%22*WEAVEWORKS_CSRF*%22%29)

```dsl
same_service(services.http.response.html_title: "Weave Scope" and services.http.response.body="*WEAVEWORKS_CSRF*")
```

### Game Servers

#### Counter-Strike: Global Offensive [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28banner%3A+%22Counter-Strike%3A+Global+Offensive+Server%22+and+service_name%3A+VALVE%29)

```dsl
same_service(banner: "Counter-Strike: Global Offensive Server" and service_name: VALVE)
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

<details>
    <summary markdown="span">Screenshot</summary>
    <img src="./images/busybox.png" alt="Busybox" width="300px" />
</details>

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

#### North Korean Hosts [&#x2192;](https://search.censys.io/search?resource=hosts&q=location.country%3A+%22North+Korea%22)

```dsl
location.country: "North Korea"
```

#### Honepots Hosts [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.truncated%3A+true)

```dsl
services.truncated: true
```


#### Prometheus Node Exporters [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28services.http.response.html_title%3A+%22node+exporter%22+and+services.http.response.body%3A+%22%2Fmetrics%22%29)

```dsl
same_service(services.http.response.html_title: "node exporter" and services.http.response.body: "/metrics")
```

#### [VictoriaMetrics VMAgent](https://docs.victoriametrics.com/vmagent.html) [&#x2192;](https://search.censys.io/search?resource=hosts&q=services.http.response.body%3A+%22%3Ch2%3Evmagent%3C%2Fh2%3E%22)

```dsl
services.http.response.body: "<h2>vmagent</h2>"
```

#### [SonarQube](https://www.sonarqube.org/) [&#x2192;](https://search.censys.io/search?resource=hosts&q=same_service%28http.response.html_title%3A+%22SonarQube%22+and+http.response.status_code%3A+200+and+http.response.protocol%09%3A+%22HTTP%2F1.1%22%29)

```dsl
same_service(
    http.response.html_title: "SonarQube"
    and http.response.status_code: 200
    and http.response.protocol: "HTTP/1.1"
)
```

#### [Unconfigured AdGuard](https://adguard.com/en/welcome.html) [&#x2192;](https://search.censys.io/search?resource=hosts&sort=RANDOM&per_page=25&virtual_hosts=INCLUDE&q=same_service%28services.http.response.html_title%3A+%22Setup+AdGuard+Home%22+and+services.http.request.uri%3D%22*%2Finstall.html%22%29)

```dsl
same_service(
    services.http.response.html_title: "Setup AdGuard Home"
    and services.http.request.uri="*/install.html"
)
```


####

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

## Credits

- [jakejarvis/awesome-shodan-queries](https://github.com/jakejarvis/awesome-shodan-queries)
- [woj-ciech/Kamerka-GUI](https://github.com/woj-ciech/Kamerka-GUI)
- [salesforce/jarm](https://github.com/salesforce/jarm)
- [cedowens/C2-JARM](https://github.com/cedowens/C2-JARM)
