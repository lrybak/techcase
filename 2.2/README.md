# Exercise 2.2

## Build image

```
docker buildx build --platform linux/amd64,linux/arm64 --push --no-cache -t lrybak/scanner:dev .
```

## Deploy scanner

Update path in scanner-storage volume to fit your setup

```
kubectl apply -f scanner.yaml
```