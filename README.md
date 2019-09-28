# DnsLOL

A dns-exfil method for use in networks that do not strictly enforce DNS server assignment policy.

The idea being, the traffic will look vaguely normal on the wire, out-wit the alternative destination.

Uses base64 encoding wrapped around normal dns queries.

server.py

Receives connections and parses the clients hostname into a postgresql database, data is encrypted on the wire using nacl.

```
bf=# SELECT * FROM hosts;
        host        |        stamp        |       lastcom       
--------------------+---------------------+---------------------
 student-VirtualBox | 2019-09-28 23:14:50 | 2011-01-01 00:00:00
```

client.py

Sends hostname string to the server via conventional dns queries encoded to base64.

# Dependencies

Under Ubuntu:
```
server.py:
postgresql
python-nacl
python-psycopg2

client.py:
python-nacl
```


# Disclaimer

Please refer to LICENSE file.
