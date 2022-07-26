#!/bin/bash

control_plane_node=$(kubectl get nodes | grep "control-plane" | awk '{print $1}')
myip=$(kubectl get nodes $control_plane_node -o=jsonpath='{.status.addresses[].address}')
#kubectl get nodes $(kubectl get nodes | grep "control-plane" | awk '{print $1}') -o=jsonpath='{.status.addresses[].address}'
myip=$(kubectl get nodes -lnode-role.kubernetes.io/master -o yaml | grep "\- address" | grep -v ip | sed 's/.*: //')
key_token=$(kubeadm token list | tail -1 | awk '{print $1}')
server_token=$(openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //')

echo "sudo kubeadm join $myip:6443 --token $key_token --discovery-token-ca-cert-hash sha256:$server_token"


