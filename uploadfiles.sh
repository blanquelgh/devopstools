#!/bin/bash

#credentials
user_repo=$1
passwd_repo=$2
url_repo=$3
port_repo=$4
inputfile_name=$5

inputfile_path="/home/sshuser/scripts/uploadlist/"
#cd $input_path

while IFS="|" read -r u_region u_sitename u_path u_filename u_filedata;
do

p_region=`echo "${u_region}" | awk '{gsub(" ", "%20", $0); print}'`
p_sitename=`echo "${u_sitename}" | awk '{gsub(" ", "%20", $0); print}'`
p_path=`echo "${u_path}" | awk '{gsub(" ", "%20", $0); print}'`
p_filename=`echo "${u_filename}" | awk '{gsub(" ", "%20", $0); print}'`
p_filedata=`echo "${u_filedata}" | awk '{gsub(" ", "%20", $0); print}'`

#echo "$sitio_n"
#echo "$region_n"

#ejecutar consulta previa a subida para obtener el id del folder para saber si existe
#echo "http://$url_repo:$port_repo/alfresco/service/slingshot/doclib/doclist/folders/site/$u_sitename/documentLibrary/$u_region/$u_path"

query_folder=`curl -u$user_repo:$passwd_repo "http://$url_repo:$port_repo/alfresco/service/slingshot/doclib/doclist/folders/site/PMO/documentLibrary/$p_region/$p_sitename/$p_path"`

#validar la salida del json
result_queryfolder=""

#extrae el identificador del forlder
if echo "${query_folder}" | grep -qF "workspace"; then

   result_queryfolder=`echo "$query_folder" | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["metadata"]' | awk -F"," -v k="workspace" '{ gsub(/{|}/,""); for(i=1;i<=NF;i++){  if ( $i ~ k ){ print $i } } }' | awk '{print $3}' | awk '{gsub(/u\047/,"");gsub(/\047/,"")}NF{$1=$1;print}'`
   echo $p_region"|"$p_sitename"|"$p_path"|"$p_filename"|"$p_filedata"|"$result_queryfolder >> logs/output_searchfolder.tmp

else

  result_queryfolder=`echo "$query_folder" | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["status"]' | awk -F"," -v k="description" '{ gsub(/{|}/,""); for(i=1;i<=NF;i++){  if ( $i ~ k ){ print $i } } }' |  awk '{gsub(/u\047/,"");gsub(/\047/,"")}NF{$1=$1;print}'`
  echo $p_region"|"$p_sitename"|"$p_path"|"$p_filename"|"$p_filedata"|"$result_queryfolder >> logs/output_searchfoldererrors.tmp
fi

done < $inputfile_path$inputfile_name


#inicia  ciclo de subida de ficheros
path_filesu=repositoryfiles/

cd repositoryfiles

u_link="http://$url_repo:$port_repo/share/page/site/pmo/document-details?nodeRef="

while IFS="|" read -r l_region l_sitename l_path l_filedata l_filename l_urifolder;
do

f_region=`echo "${l_region}" | awk '{gsub("%20", " ", $0); print}'`
f_sitename=`echo "${l_sitename}" | awk '{gsub("%20", " ", $0); print}'`
f_path=`echo "${l_path}" | awk '{gsub("%20", " ", $0); print}'`
f_filedata=`echo "${l_filedata}" | awk '{gsub("%20", " ", $0); print}'`
f_filename=`echo "${l_filename}" | awk '{gsub("%20", " ", $0); print}'`
upload_result=`curl -v -X POST -u$user_repo:$passwd_repo http://$url_repo:$port_repo/alfresco/service/api/upload -F filedata="@$f_filedata"  -F destination="$l_urifolder" -F filename=$f_filename`

echo $upload_result
#extrae el identificador del ficehro que sube a alfresco
result_updateFile=""
if echo "${query_folder}" | grep -qF "workspace"; then

  result_updateFile=`echo "$upload_result" | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["nodeRef"]'`
  echo $f_region"|"$f_sitename"|"$f_path"|"$f_filedata"|"$f_filename"|"$u_link$result_updateFile >> ../logs/output_uploadprocsuccess.log
fi


#extrae el o el mensaje de error
if echo "${query_folder}" | grep -qF "message"; then
   result_updateFile=`echo "$upload_result" | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["message"]'`
   echo $f_region"|"$f_sitename"|"$f_path"|"$f_filedata"|"$f_filename"|"$u_link$result_updateFile >> ../logs/output_uploadprocfailed.log
fi


done < ../logs/output_searchfolder.tmp
#termina ciclo de subida de ficheros
#echo $result_updateFile

exit 0
