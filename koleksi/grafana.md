# Instalasi grafana Server untuk Monitoring 

di Ubuntu
```
sudo apt-get update
```

terus
```
sudo apt-get install grafana-server
```

terus
```
sudo systemctl restart grafana-server
```

biar jalan waktu startup
```
sudo systemctl enable grafana-server
```

# Pemasangan Prometheus untuk Server yang di Monitoring

di Ubuntu
```
sudo apt-get update
```

terus
```
sudo apt-get install prometheus
```

terus
```
sudo systemctl restart prometheus
```

biar jalan waktu startup
```
sudo systemctl enable prometheus
```

# Menambah Datasource buat grafana
buka url ini di browser
```
http://ip-server-lu:3000
```

user defaultnya `admin` passwordnya juga `admin` kalo gasalah. cari datasource di sidebarnya, pilih prometheus, terus isi ip sama portnya prometheus disitu, contohnya `http://127.0.0.1:9090`.

udah itu aja
