### Mongo Deployment

You have to first apply `mongo-config-map.yaml` - so it can be used in `mongo-express.yaml` and `mongo-secrets.yaml` so it can be used in `mongo.yaml`
```
kubectl apply -f mongo-config-map.yaml
kubectl apply -f mongo-secrets.yaml
```
