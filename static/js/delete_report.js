/*jshint esversion: 6 */ 

const deleteReportModal = document.getElementById("deleteReportModal");
const deleteReportBtn = document.getElementsByClassName("delete-report-btn");
const deleteReportConfirm = document.getElementById("deleteReportConfirm");

/** Iterate over each delete button
* Add click event listener to each delete button
* Get the report ID from the clicked button's attributes
* Get the slug from the clicked button's attributes
* Check if the slug attribute is null
* If slug is null, construct the delete URL without slug
* If slug is not null, construct the delete URL with slug
* Show the delete report confirmation modal
*/

for (let button of deleteReportBtn) {

  button.addEventListener("click", (e) => {
      
      let reportId = e.target.getAttribute("data-report_id");
      let slug = e.target.getAttribute("data-slug");

      if (slug === null) {
          deleteReportConfirm.href = `delete/${reportId}`;
      } else {
          deleteReportConfirm.href = `${slug}/delete/${reportId}`;
      }

      deleteReportModal.show();
  });
}