const deleteReportModal = new bootstrap.Modal(document.getElementById("deleteReportModal"));
const deleteReportBtn = document.getElementsByClassName("delete-report-btn");
const deleteReportConfirm = document.getElementById("deleteReportConfirm");

console.log('js connected');

for (let button of deleteReportBtn) {
    button.addEventListener("click", (e) => {
      console.log('click');
      let reportId = e.target.getAttribute("report_id");
      let slug = e.target.getAttribute("slug");
      if (slug === null) {
        deleteReportConfirm.href = `delete/${reportId}`;
      } else
      deleteReportConfirm.href = `${slug}/delete/${reportId}`;
      deleteReportModal.show();
    });
  }