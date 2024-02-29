const editBtn = document.getElementsByClassName("edit-btn");

const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteBtn = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Iterate over each edit button
* Add click event listener to each edit button
* Get the comment ID from the clicked button's attributes
* Get the content of the comment corresponding to the clicked button
* Set the value of the comment text input field to the content of the comment
* Change the text of the submit button to "Update"
* Set the action attribute of the comment form to the edit URL with the comment ID
*/

for (let button of editBtn) {
  
  button.addEventListener("click", (e) => {
      
      let commentId = e.target.getAttribute("data-comment_id");
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}



/**
* Iterate over each delete button
* Add click event listener to each delete button
* Get the comment ID from the clicked button's attributes
* Set the href attribute of the delete confirmation link to the delete URL with the comment ID
* Show the delete confirmation modal
*/

for (let button of deleteBtn) {
  
  button.addEventListener("click", (e) => {
      
      let commentId = e.target.getAttribute("data-comment_id");
      
      deleteConfirm.href = `delete_comment/${commentId}`;
      
      deleteModal.show();
  });
}
