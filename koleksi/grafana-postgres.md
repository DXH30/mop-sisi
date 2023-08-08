# Setup grafana untuk postgres\_exporter

1. Download `snmp_exporter` ke `/opt/postgres_exporter`
   ```bash
   mkdir /opt/postgres_exporter && cd /opt/postgres_exporter
   ``` 

    ```bash
    wget https://github.com/wrouesnel/postgres_exporter/releases/download/v0.5.1/postgres_exporter_v0.5.1_linux-amd64.tar.gz
    ```

    ```bash
    tar -zxvf  postgres_exporter_v0.5.1_linux-amd64.tar.gz && cd postgres_exporter_v0.5.1_linux-amd64
    ```

    ```bash
    sudo cp postgres_exporter /usr/local/bin
    ```
2. Konfigurasi file `environment`
    ```bash
    vim /opt/postgres_exporter/postgres_exporter.env
    ```

    ```bash
    DATA_SOURCE_NAME="postgresql://username:password@localhost:5432/?sslmode=disabled"
    ```
    atau
    ```bash
    DATA_SOURCE_NAME="user=postgres host=/var/run/postgresql/ sslmode=disabled"
    ```

3. Konfigurasi service exporter `postgres_exporter`
    ```bash
    sudo vim /etc/systemd/system/postgres_exporter.service
    ```

    ```bash
    [Unit]
    Description=Prometheus exporter for Postgresql
    Wants=network-online.target
    After=network-online.target

    [Service]
    User=postgres
    Group=postgres
    WorkingDirectory=/opt/postgres_exporter
    EnvironmentFile=/opt/postgres_exporter/postgres_exporter.env
    ExecStart=/usr/local/bin/postgres_exporter --web.listen-address=:9187 --web.telemetry-path=/metrics
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

    Enable dan start service `postgres_exporter` 

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable postgres_exporter
    sudo systemctl start postgres_exporter
    sudo systemctl status postgres_exporter
    ```

4. Konfigurasi job `prometheus`
    ```bash
    sudo vim /etc/prometheus/prometheus.yml
    ```

    ```yaml
    ...
    — job_name: ‘postgres_exporter’
      static_configs:
        — targets: [‘127.0.0.1:9187’]
    ...
    ```

    Restart prometheus

    ```
    sudo systemctl restart prometheus
    ```
