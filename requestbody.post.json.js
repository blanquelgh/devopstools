var nodeParent = companyhome.childByNamePath("sites/PMO/documentLibrary");

//Busca el template
var templateResults = companyhome.childrenByXPath("*[@cm:name='Data Dictionary']/*[@cm:name='Space Templates']/*[@cm:name='PMO']/*");

//Obtiene el nombre del template
var templateNameFolder = templateResults[0].properties.name;
var newContentFolder = templateResults[0].copy(nodeParent,true);
newContentFolder.name = json.get("request");
newContentFolder.title= json.get("request");
newContentFolder.properties.encoding = "UTF-8";
newContentFolder.save();

//model.requestcontent = newContentFolder.name;
//newContentFolder.setName(requestbody.content);
//newContentFolder.properties.encoding = "UTF-8";
//newContentFolder.properties["cm:description"] ="prueba 123";
//newContentFolder.properties["cm:title"] = "titulo prueba 123";
model.requestcontent = newContentFolder;
//model.requestcontent = resultsqry;
