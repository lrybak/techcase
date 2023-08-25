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

## Usage
Note: Program requires nmap to be locally installed. Nmap will be installed by running the playbook site.yml from task 1.1.
Additionally, the program accepts the -v flag, providing verbose output related to the program's runtime statistics.
```
scanner 127.0.0.1
scanner 192.168.1.1/24
scanner 192.168.1.1-30
scanner 192.168.1.4 -v
```

## Cleanup
```
make clean
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