# DnsLOL

A dns-exfil method for use in networks that do not strictly enforce DNS server assignment policy.

The idea being, traffic will look vaguely normal on the wire, out-wit the alternative destination.

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

NOTE: Takes a few minutes to send the data, console output will cease when fully sent, change time.sleep if you want to speed up, although be carful as this is UDP and things can get out of sync.

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

# Postgres Setup
temp/data is used for processing data
bf/hosts is used for holding the results

```
sudo -u postgres psql
ALTER USER postgres PASSWORD 'Nope';
CREATE DATABASE bf;
CREATE DATABASE temp;

\c bf

CREATE TABLE HOSTS(
   HOST TEXT PRIMARY KEY  NOT NULL,
   STAMP TIMESTAMP NOT NULL,
   LASTCOM TIMESTAMP NULL
);

\c temp

CREATE TABLE DATA(
   HOST TEXT PRIMARY KEY  NOT NULL,
   WHAT TEXT NULL
);


To View:

\c bf
SELECT * FROM hosts;

To Exit:
\q;
```


# Disclaimer

Please refer to LICENSE file.
