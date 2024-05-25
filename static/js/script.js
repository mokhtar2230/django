const dropdown = document.querySelector('.dropdown');

    dropdown.addEventListener('click', () => {
        dropdown.classList.toggle('active');
    });






    
document.getElementById("showCommentsButton").addEventListener("click", function() {
    var commentList = document.getElementById("commentList");
    if (commentList.style.display === "none") {
        commentList.style.display = "block";
    } else {
        commentList.style.display = "none";
    }
});
document.getElementById("showOptionsButton").addEventListener("click", function() {
  var optionsContainer = document.getElementById("optionsContainer");
  if (optionsContainer.style.display === "block") {
    optionsContainer.style.display = "none";
    document.querySelectorAll("#optionsContainer a").forEach(function(link) {
      link.classList.remove("selected");
    });
  } else {
    optionsContainer.style.display = "block";
    var buttonRect = document.getElementById("showOptionsButton").getBoundingClientRect();
    optionsContainer.style.top = (buttonRect.top + buttonRect.height) + "px";
    optionsContainer.style.left = buttonRect.left + "px";
  }
});

document.querySelectorAll("#optionsContainer a").forEach(function(link) {
  link.addEventListener("click", function() {
    document.querySelectorAll("#optionsContainer a").forEach(function(otherLink) {
      otherLink.classList.remove("selected");
    });
    link.classList.add("selected");
  });
});

