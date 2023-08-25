# Exercise 1.1
## Bootstrap test VM
Create test VM or use your own

```sh
multipass launch -n techcase --cloud-init ~/.cloud-init.yaml --disk 20G
multipass mount $HOME/code/techcase techcase:/home/ubuntu/techcase
```

# Run
Run ansible playbook inside test VM

```
ansible-playbook -i localhost -c local site.yml
```