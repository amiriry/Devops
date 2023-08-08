## Jenkikns Shared Lib Projec
This project is for using shared lib in jenkins.
You can modify and use the config files in configfiles/ directory.<br>
<br>
The way to use it:<br>
##### Create a directory for the shared library project
```
>> mkdir projectdir
>> cd projectdir
```

##### Clone only sharedlib dir with sparse checkout
```
>> git init .
>> git remote add origin https://github.com/amiriry/Devops.git
>> git sparse-checkout init
>> echo "Jenkins/SharedLibraryProject/" >> .git/info/sparse-checkout
>> git pull origin master
```

##### Get into directory and create all the git repos needed
```
>> cd SharedLibraryProject/
>> for d in $(ls);do cd $d;git init .;git add .;git commit -m "nothing";cd ../;done
```

##### Run the container
the container from [here](https://github.com/amiriry/Devops/tree/main/Jenkins/containers/no-plugins-installation-local-repo) with another plugin installed named: <b>pipeline-utility-steps</b>
```
docker run --name myjenkins -td -p 8085:8080 -v $(pwd)/pipelines/:/var/pipelines -v $(pwd)/sharedLib/:/var/sharedLib -v $(pwd)/configfiles:/var/configfiles jenkins:
```

Define the pipelime as ```pipeline script from SCM``` and choose the path as one of your volumes, where the pipeline is ```/var/pipelines```.<br>

Now you can run it and just change the ```configfiles/file.yaml``` how ever you want.<br>
<br>
When you run the pipeline you can see that it reads from the yaml in the line:<br>
```
variable value: somevalue
```
which is the value that we are reading in the pipeline from the yaml file.
