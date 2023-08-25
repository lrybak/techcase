# Exercise 2.1
## Install

```
make install
```

After executing **make install** make sure to relogin to refresh $PATH envvar or manually update $PATH
```
export PATH=$HOME/.local/bin:$PATH
```

## Uninstall
Uninstall package if no longer required
```
make uninstall
```

## Cleanup
```
make clean
```

## Usage
Note: Program requires nmap to be locally installed. Nmap will be installed by running the playbook site.yml from task 1.1.
Additionally, the program accepts the -v flag, providing verbose output related to the program's runtime statistics.
```
scanner 127.0.0.1
scanner 192.168.1.1/24
scanner 192.168.1.1-30
scanner 192.168.1.4 -v
```
Example output:
```
$ scanner 192.168.1.10,170 -v
192.168.1.10
* 22/tcp ssh: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 111/tcp rpcbind: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 139/tcp netbios-ssn: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 445/tcp microsoft-ds: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 3000/tcp ppp: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 3306/tcp mysql: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 8000/tcp http-alt: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 8080/tcp http-proxy: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)

192.168.1.170
* 22/tcp ssh: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 80/tcp http: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)
* 443/tcp https: open (now), open (36 seconds ago), open (45 seconds ago), open (48 seconds ago)

2 IP address in range (2 hosts up, 0 hosts down) scanned in 0.11 seconds
```


# Exercise 2.2
## Build image
Note: The image has already been built and pushed to: registry.hub.docker.com/lrybak/scanner:dev.
```
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 --push --no-cache -t lrybak/scanner:dev .
```

## Deploy scanner cronjob
Note: Update path in scanner-storage volume definition to fit your setup
```
kubectl apply -f scanner.yaml

# Check scanner
kubectl get cj
```