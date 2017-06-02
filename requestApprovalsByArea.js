function startWorkflow2(assigneeGroup, approver_group)
{
    var workflow = actions.create("start-workflow");
	var groupmo="PMO";
    workflow.parameters.workflowName = "activiti$activitiReviewPooled";	
    workflow.parameters["bpm:workflowDescription"] = "El documento " + document.name + " requiere validacion de " + approver_group ;
	workflow.parameters["bpm:groupAssignee"] = assigneeGroup;
    var futureDate = new Date();
    futureDate.setDate(futureDate.getDate() + 5);
    workflow.parameters["bpm:workflowDueDate"] = futureDate; 
    return workflow.execute(document);
}

function startWorkflow(assigneeGroup)
{
    var workflow = actions.create("start-workflow");
	
    workflow.parameters.workflowName = "activiti$activitiReviewPooled";	
    workflow.parameters["bpm:workflowDescription"] = "El documento " + document.name + " requiere validacion ";
	workflow.parameters["bpm:groupAssignee"] = assigneeGroup;
    var futureDate = new Date();
    futureDate.setDate(futureDate.getDate() + 5);
    workflow.parameters["bpm:workflowDueDate"] = futureDate; 
    return workflow.execute(document);
}

function main()
{
  
   var name = document.name;
   var siteName = document.siteShortName;
   
   if (siteName == null)
   {
     if (logger.isLoggingEnabled())
         logger.log("Did not start workflow as the document named " + name + " is not located within a site.");
         
      return;
   }
  

  var emisor = ""
  var reviewGroup = "";
  if (name.search("DES") !=-1) {
     emisor ="DES";  
     reviewGroup="GROUP_pmo_deploy";	 
  }
  
  if (name.search("DIS") !=-1) {
     emisor ="DIS"; 
     reviewGroup="GROUP_pmo_design";	 
  }
   
  
  
  // make sure the group exists
  var group = people.getGroup( reviewGroup);

   if (group != null)
   {
     logger.log("group: " + group);
     
      if (logger.isLoggingEnabled())
         logger.log("Starting pooled review and approve workflow for document named " + name + " assigned to group " + reviewGroup);

      //startWorkflow2(group,grupoAprobador);
       startWorkflow(group);

      if (logger.isLoggingEnabled())
         logger.log("Started pooled review and approve workflow for document named " + name + " assigned to group " + reviewGroup);
   }
   else if (logger.isLoggingEnabled())
   {
      logger.log("Did not start workflow as the group " + reviewGroup + " could not be found.");
   }
  
  
}

main();