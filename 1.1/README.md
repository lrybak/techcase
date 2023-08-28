# Exercise 1.1
## Bootstrap test VM
Create test VM or use your own

```sh
multipass launch -n techcase --cloud-init ~/.cloud-init.yaml --disk 20G
multipass mount $HOME/code/techcase techcase:/home/ubuntu/techcase
```

# Run
Run ansible playbook inside test VM
To allow non-root user to manage Docker, user who run playbook has been added to the docker group.
To apply these changes, user needs to log out and log back in after executing playbook.
```
ansible-playbook -i localhost -c local site.yml
```