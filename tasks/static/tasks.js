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

function deleteTask(taskId){
  $.ajax({
    url: taskId + "/delete/",
    data: {
    csrfmiddlewaretoken : csrfToken
    }
  }).done(function(data){
    if(data["result"] === "success"){
      $("#task_" + taskId).remove();
    }
  });
}

function createTask(content, due_date, completed){
    $.ajax({
        url: "create/",
        method: "POST",
        data:{
            csrfmiddlewaretoken: csrfToken,
            task_content: content,
            task_due_date: due_date,
            task_completed: completed
        }
    }).done(function(data){
        task = new Task(data.id, data.content, data.created_date, data.due_date, data.completed, data.deleted);
        tasks.push(task);
        console.log(task);
        window.location.reload();
    });
}

function strikeTask(taskId){

}

function completeTask(taskId){
  $.ajax({
    url: taskId + "/complete/",
    method: "POST",
    data: {
    csrfmiddlewaretoken: csrfToken
    }
  }).done(function(data){
    if(data["result"] === "success"){
      let currentAnswer = $("#task_completed_" + taskId).text();
      if(currentAnswer === "Yes"){
        $("#task_completed_" + taskId).text("No");
        $("#completed_input_" + taskId).val("No");
      }else{
        $("#task_completed_" + taskId).text("Yes");
        $("#completed_input_" + taskId).val("Yes");
        strikeTask(taskId);
      }
    }
  });
}

function editTask(taskId){
  let updateDetails = {};
  updateDetails["content"] = $("#content_input_" + taskId).val();
  updateDetails["due_date"] = $("#due_date_input_" + taskId).val();
  updateDetails["completed"] = $("#completed_input_" + taskId).val();
  updateDetails["csrfmiddlewaretoken"] = csrfToken;
  $.ajax({
    url: taskId + "/edit/",
    data: updateDetails,
    method: 'POST'
  }).done(function(data){
    updateTaskElements(data);
  });
}

function updateTaskElements(data){
    task = tasks.filter(function(t){
        return t.id === data.id;
    });
    task[0].content = data.content;
    task[0].due_date = data.due_date;
    task[0].completed = data.completed ? "Yes" : "No";
    $("#task_content_" + task[0].id).text(task[0].content);
    $("#task_due_date_" + task[0].id).text(task[0].due_date);
    $("#task_completed_" + task[0].id).text(task[0].completed);
}

function attachCallbacks(taskId){
  $("#edit_" + taskId).unbind();
  $("#edit_" + taskId).click(function(){
    editTask(taskId);
  });
  $("#edit_button_" + taskId).unbind();
  $("#edit_button_" + taskId).click(function(){
    insertInformation(taskId);
  });
  $("#complete_button_" + taskId).unbind();
  $("#complete_button_" + taskId).click(function(){
    completeTask(taskId); 
  });
  $("#delete_" + taskId).unbind();
  $("#delete_" + taskId).click(function(){
    deleteTask(taskId);
  });
}

function insertInformation(taskId){
    var task = tasks.filter(function(t){
        return t.id === taskId;
    });
    $("#content_input_" + taskId).val(task[0].content);
    $("#due_date_input_" + taskId).val(task[0].due_date);
    $("#completed_input_" + taskId).val(task[0].completed);
}

$(document).ready(function(){
  let idList = tasks.map(t => t.id);
  for(var i = 0; i<idList.length; i++){
    attachCallbacks(idList[i]);
  }
  $("#add_task_button").click(function(){
    $("#new_content").val("");
    $("#new_due_date").val("");
    $("#new_completed").val("No");
  });
  $("#create_new_task").click(function(){
    let content = $("#new_content").val();
    let due_date = $("#new_due_date").val();
    let completed = $("#new_completed").val();
    createTask(content, due_date, completed);
  });
});