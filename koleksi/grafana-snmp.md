# Setup Grafana untuk Monitoring SNMP Exporter
Berikut adalah langkah-langkah untuk melakukan setup monitoring snmp di grafana
## Pastikan SNMP bisa di akses
Setup SNMP dan community string nya agar bisa di akses dari server, setelah itu ssh ke server lalu jalankan perintah `snmpwalk -v1 -c public 192.168.1.1`, ganti dan sesuaikan ip `192.168.1.1` dan community string `public`, sama dengan ip dan community string yang sudah di setting di perangkat.\\
Jika sudah sesuai, maka snmp akan memunculkan banyak oid dan data snmp dari perangkat. Setelah itu dapat lanjut ke tahap selanjutnya.

## Download SNMP Exporter
Download snmp exporter di server yang udah ada `prometheus` nya. boleh cek di https://github.com/prometheus/snmp_exporter/releases .Cari yang sesuai dengan os atau ambil langsung tar.gz nya, terus extract dengan

```
tar -zxvf snmp_exporter*.tar.gz /opt/snmp_exporter
```

## Konfigurasi SNMP Exporter

lalu, masuk ke directory hasil extractnya.
```
cd /opt/snmp_exporter 
```

Buka snmp.yml, bisa juga di buat kalau kosong, isi kayak gini (sebelumnya pastikan targetnya udah bener, dan udah di cek pakai snmpwalk dari servernya)
```
modules:
  - name: myrouter
    target: 192.168.1.1
    timeout: 5s
    retries: 3
    auth:
      community: public
    metrics:
      - if_mib
      - system
```

Buat nyoba bisa pakai
```
./snmp_exporter &
```

Buat ngecek port nya kebuka atau ngga, bisa lewat netstat, port nya snmp exporter defaultnya 9116
```
netstat -puntel
```

Kill proses SNMP exporter
```
killall snmp_exporter
```

Buat Systemd agar SNMP exporter jalan di awal
```
sudo vi /etc/systemd/system/snmp_exporter.service
```

Isikan
```
[Unit]
Description=Prometheus SNMP Exporter
After=network.target

[Service]
ExecStart=/opt/snmp_exporter

[Install]
WantedBy=default.target
```

Jika ada penambahan init script jangan lupa untuk daemon-reload systemd
```
sudo systemctl daemon-reload
```

Agar bisa langsung jalan di awal bisa di enable dulu
```
sudo systemctl enable snmp_exporter
```

Coba cek
```
sudo systemctl status snmp_exporter
```

# Masang job di prometheus, untuk narik data dari SNMP Exporter
Edit file yaml nya prometheus
```
sudo vi /etc/prometheus/prometheus.yml
```

Tambah job nya, isiin kayak gini, di dalem `scrape_configs`
```
- job_name: 'snmp_exporter'
  static_configs:
    - targets: ['localhost:9116']
```

Setelah itu di save, lalu restart prometheus
```
sudo systemctl restart prometheus
```

Coba cek di datasource nanti, muncul ngga itu job, kalau belum, coba hapus terus tambah ulang lagi.
