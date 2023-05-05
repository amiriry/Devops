FROM jenkins/jenkins
# The java option that makes the installation not run plugin installation
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false -Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true"
# Recommended-plugins.txt - the file where plugins are listed
COPY recommended-plugins.txt /usr/share/jenkins/ref/recommended-plugins.txt 
# Run this script with input from the file of list of plugins
#RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/recommended-plugins.txt # Old version
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/recommended-plugins.txt 
