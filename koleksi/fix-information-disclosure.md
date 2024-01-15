# Apache
1. Install apache module security2
2. Enable mod security2
3. Edit konfigurasi `httpd.conf`
```
ServerTokens Full
```
4. Edit konfigurasi `mod_security2.conf`
```
SecRuleEngine DetectionOnly // menghilangkan nama apache version
SecServerSignature "" // mengganti signature webserver
```
## Catatan
Server Apache tidak dapat full di hilangkan Server Header nya

# IIS
1. Hapus Server Header IIS di
```
Configuration Editor -> 
system.webServer/security/requestFiltering ->
removeServerHeader -> True
```
2. Hapus X-Powered-By ASP di
```
HTTP Response Header ->
Hapus X-Powered-By ASP
```

3. Hapus X-Powered-By PHP di
```
PHP Manager ->
php_expose -> Off
```
