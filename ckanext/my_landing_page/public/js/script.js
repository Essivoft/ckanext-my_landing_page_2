document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".group").forEach(function (group) {
    group.addEventListener("click", function () {
      var groupName = this.getAttribute("data-group-name");
      window.location.href = "/group/" + groupName;
    });
  });
});
