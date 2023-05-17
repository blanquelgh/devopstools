A continuacion se da una breve descripcion de los ficheros que permiten la ejecucion del bot en telegram mediante la invocacion a las funcionalidades declaradas en python mediante 
un webhoock.


1.- confbotservpy.yml: Archivo con la configuracion del entorno y de los valores de conexion hacia los font ends que se requieren validar. Tambien se cuenta con las rutas de los 
                        drivers y las llaves de conexion al telegram
2.- initbotPOO.py: Fichero de python con la funcionalidad establecida en funciones para el tratamiento de los screenshots y la seleccion de la invocacion de las url a probar

3.- requeriments.txt: Fichero con la definicion de las librerias de python necesarias para la ejecucion del fichero py

4.- python_docker_build: en la carpeta dockerfile se encuentra el fichero generado para la imagen docker utilizado en la construccion de la imagen que se encuentra corriendo
                         en cto2 dentro del ambiente desarrollo de obpymes
                         
                         <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                              https://maven.apache.org/xsd/settings-1.0.0.xsd">
                              
mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.consolidation -DartifactId=imatch-consolidation -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-consolidation.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.transformer -DartifactId=imatch-data-transformer -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-data-transformer.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.gateway -DartifactId=imatch-gateway -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-gateway.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.classifier -DartifactId=imatch-generic-classifier -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-generic-classifier.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.importer -DartifactId=imatch-importer -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-importer.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.license -DartifactId=imatch-license -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-license.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.metrics -DartifactId=imatch-metrics -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-metrics.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.pipeline.executor -DartifactId=imatch-pipeline-executor -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-pipeline-executor.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.publisher -DartifactId=imatch-publisher -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-publisher.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.resource.manager -DartifactId=imatch-resource-manager -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-resource-manager.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.search -DartifactId=imatch-search -Dversion=2.4.15-RELEASE -Dpackaging=jar -Dfile=imatch-search.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X


mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.ui -DartifactId=imatch-ui -Dversion=2.4.15-RELEASE -Dpackaging=zip -Dfile=imatch-ui.zip -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X


#####################################################v2.4.14-Pandora##################################################################################################

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.bankstatement -DartifactId=iex-mex-bankstatement -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-bankstatement.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.cfe -DartifactId=iex-mex-cfe -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-cfe.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.constitution -DartifactId=iex-mex-constitution -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-constitution.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.ife -DartifactId=iex-mex-ife -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-ife.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.ine -DartifactId=iex-mex-ine -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-ine.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.passport -DartifactId=iex-mex-passport -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-passport.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.rfc -DartifactId=iex-mex-rfc -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-rfc.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.mex.telmex -DartifactId=iex-mex-telmex -Dversion=2.4.14-RELEASE -Dpackaging=jar -Dfile=iex-mex-telmex.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.idlc.front.confd -DartifactId=idlc-confd -Dversion=2.4.14-RELEASE -Dpackaging=zip -Dfile=confd.zip -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

#########################################v2.4.16###########################################################################################################

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.ui -DartifactId=imatch-ui -Dversion=2.4.16-RELEASE -Dpackaging=zip -Dfile=imatchui.zip -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X

mvn deploy:deploy-file -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true -Dmaven.wagon.http.ssl.ignore.validity.dates=true -DgroupId=com.taiger.imatch.license -DartifactId=imatch-license -Dversion=2.4.16-RELEASE -Dpackaging=jar -Dfile=imatch-license.jar -DrepositoryId=nexus_mexico -Durl=https://nexus.pro.pandora.mx.corp/repository/maven-release/ -X


node('taurus')
    {
        deleteDir()
        
        dir('demo-test') {
        stage 'Build' 
        task 'Copying base code repository'
        git branch: 'master',
            credentialsId: 'pandora-gitlab-ssh-id',
            url: 'ssh://git@gitlab.pro.pandora.mx.corp:2220/devsecops/piloto.git'
        }
        
        dir('Blazemeter') {
        stage 'Passfail criteria' 
        task 'Copying passfail criteria\'s repository'
        git branch: 'master',
            credentialsId: 'pandora-gitlab-ssh-id',
            url: 'ssh://git@gitlab.pro.pandora.mx.corp:2220/devsecops/Blazemeter.git'
        }
        
        dir('demo-test') {
        stage 'Change analysis'
        task 'Executing Blazemeter test on latest edited test file(s)'
        sh ''' #!/bin/bash
        
                num=1
  
                for commit in `git log | grep commit | awk '{print $2}' | head -n 2`
                do
                    export commit$num=$commit
                    let num++
                done

                for blazemeter in `git diff --name-only ${commit1} ${commit2}`
                do
		            bzt $blazemeter ../Blazemeter/Demo/passfail_config.yml -cloud
                done '''
        }
    }
    
 1839  docker tag firejava:latest registry.cto1.paas.gsnetcloud.corp/mxsre/firejava:latest
 1840  docker push registry.cto1.paas.gsnetcloud.corp/mxsre/firejava:latest
