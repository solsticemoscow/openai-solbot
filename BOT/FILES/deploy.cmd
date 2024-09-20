




docker build -f Dockerfile -t solbot .


docker tag solbot europe-west10-docker.pkg.dev/eureka-429515/reg/solbot:v3

docker push europe-west10-docker.pkg.dev/eureka-429515/reg/solbot:v3