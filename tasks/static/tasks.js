class Task{
  constructor(id, content, created_date, due_date, completed, deleted){
    this.id = id;
    this.content = content;
    this.created_date = created_date;
    this.due_date = due_date;
    this.completed = completed;
    this.deleted = deleted;
  }
}

function attachCallbacks(taskId){
  $("edit_button_" + taskId).unbind();
  $("edit_button_" + taskId).bind(function(){

  });
  $("complete_button_" + taskId).unbind();
  $("complete_button_" + taskId).bind(function(){
    
  });
  $("delete_button_" + taskId).unbind();
  $("complete_button_" + taskId).bind(function(){
    
  });
}

$(document).ready(function(){
  let idList = tasks.map(t => t.id);
  for(var i = 0; i<idList.length; i++){
    attachCallbacks(idList[i]);
  }
});