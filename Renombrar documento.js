
function main()
{
   
var versionHistory = document.versionHistory;


if (versionHistory != null)
{

  var version =versionHistory[versionHistory.length - 1] ;
  var label=version.label;
  var arrVersion=label.split(".")
  var unitat=arrVersion[0];
  var decimal=arrVersion[1];
  var sumVersion=1;
 
  
  var subStrFilename=String(document.name);
  var arrSplitFilename=subStrFilename.split(".");
  var strFilename=arrSplitFilename[0];
  var strExtension=arrSplitFilename[1];
  //var strFilename=subStrFilename.substring(0, 15);
  //var strExtension=subStrFilename.substring(17, 20);
  
//Busqueda de ficheros
var logFile = userhome.childByNamePath("alf docs.txt");
 //logger.log(logFile);
if (logFile == null)
{
   logFile = userhome.createFile("alf docs.txt");
   logger.log(logFile);
}


if (logFile != null)
{
  logger.log("logFile !=null: " + logFile);
   // execute a lucene search across the repo for the text 'alfresco'
   // ejecuta una busqueda Lucenea través del repositorio para el texto 'alfresco'
  var documentos = search.luceneSearch("workspace://SpacesStore","@cm\\:name:\""+strFilename+"\"");
   if(documentos.length > 0 ){
     sumVersion= 1+ documentos.length;
   }
   
  //logger.log(logFile.content);
}
//Fin Busqueda ficheros

   document.name = strFilename +"-v"+ sumVersion+"."+ strExtension;
   document.save();

}

}

main();