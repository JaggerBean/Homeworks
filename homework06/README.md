# Using Flask and Redis on Kubernetes
This repository details how to deploy flask applications to kuberneters.
## How to get it Running
Once the git repository is pulled, access the homework06 directory and start every pod. to do this you will need to execute this command in your terminal:

    kubectl apply -f <filename>.yml
changing the filename with each execution. Complete this task for every .yml file.

Next you will need the ips of the services. to do that type:

    kubectl get services
Then execute:

    kubectl get pods
to get the name of your debug deployment.
Now, execute:

    kubectl exec -it <pod_name> -- /bin/bash
using the name of your debug deployment pod. Once you are within that pod you are ready to make curl requests.
## How to Make Curl Requests
First we must edit our `app.py` file. Lets change the line that is similar to `rd = redis.Redis(host='10.10.10.10', port=6379)`to have the IP match out redis service IP from before. Now run the Makefile to push it to DockerHub.

How to execute the curl requests within the terminal:

	curl -X POST <IP_of_flask_service>:5000/data
and

	curl <IP_of_flask_service>:5000/data

The first request pushes data to the redis server. The second outputs all of the meteorite data to the terminal in json form.
