#!/bin/bash

# Database credentials
user_repo=$1
passwd_repo=$2
url_repo=$3
port_repo=$4
folder_name=$5
input_path=$6


cd $input_path

while IFS="|" read -r sitio_n region_n;
do

#echo "$sitio_n"
#echo "$region_n"

   if !(echo "${sitio_n}" | grep -qF "NOMBRECOMUN_SITIO"); then

        echo "$sitio_n"
        echo "${a}"                              | awk -v OFS=" | " '{print $0, "Nuevo"}' >> uploadstatus.log
        counter=$((counter+1))

      request_createfolderstmt=`curl -u$user_repo:$passwd_repo -H "Content-Type: application/json" --data-binary "{\"region\":\"$region_n\", \"sitio\":\"$sitio_n\"}" $url_repo:$port_repo/alfresco/service/requestbody | awk '{split($0,a,": "); print a[3]}' | awk '{gsub(/<[^>]*>/,"")}NF{$1=$1;print}'`

      echo $sitio_n "|" $request_createfolderstmt >> temp_uploadstatus.log
   fi
done < $folder_name



counter=0
countR=0
countT=0
while read a;
do


    if echo "${a}" | grep -q "workspace"; then
        echo "${a}"                              | awk -v OFS=" | " '{print $0, "Nuevo"}' >> uploadstatus.log
        counter=$((counter+1))

    fi

    if echo "${a}" | grep -q "already"; then
        echo "${a}                              " | awk -v OFS=" | " '{print $0, "Rechazado"}' >> uploadstatus.log
        countR=$((countR+1))
    fi


    countT=$((countT+1))
done < temp_uploadstatus.log

#rm -rf temp_uploadstatus.log

echo "Total registros procesados: $countT " >> uploadstatus.log
echo "            Sitios creados: $counter " >> uploadstatus.log
echo "         Sitios rechazados: $countR " >> uploadstatus.log

sed  -i '1i SITIOS                                      |                    RESULTADO UPLOAD                         | ESTADO ' uploadstatus.log
cat uploadstatus.log
exit 0
