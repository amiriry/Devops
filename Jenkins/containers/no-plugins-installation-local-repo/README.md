## Jenkikns container - no need plugins instllation needed & enable use of local repo
<br>

#### When you want to check things on jenkins, and want to use local repository
<br>
I used that for jenkins container that have shared volume that contains all the jenkins code.<br>
Can be used for any local mount that you want to do, for jenkins to use.<br>

commands to make it work:<br>
`docker build -t <name>:<tag>`<br>
`docker run --name <cont_name> --rm -p 8080:8080 <img_name>:<img_tag>`<br><br>

### Basic Explanation
First of all the basic image is `jenkins/jenkins` - the official jenkins image<br>

`ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false ` - Define an environment variable <br>
`COPY recommended-plugins.txt /usr/share/jenkins/ref/recommended-plugins.txt` - Copy the file that contains plugins names to the container<br>
`RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/recommended-plugins.txt` - Use the plugins text file as an input to the script that installs plugins<br>

## Add the option for local repo
`ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false -Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true"`

###  In general, when you want to add java options
Just put quotes sign on the string after JAVA_OPTS and add the options you want.<br>
