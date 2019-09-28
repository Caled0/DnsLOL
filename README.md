# DnsLOL

A dns-exfil "method" for use in networks that do not strictly enforce DNS server policy.

The idea being, the traffic will look vaguely normal on the wire, out-wit the alternative destination.

Uses base64 encoding wrapped around normal dns queries.

