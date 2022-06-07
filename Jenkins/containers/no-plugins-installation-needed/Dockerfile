FROM jenkins/jenkins
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
COPY recommended-plugins.txt /usr/share/jenkins/ref/recommended-plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/recommended-plugins.txt
