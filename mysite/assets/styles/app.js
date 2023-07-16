var myButton = document.getElementById("cta");
var myDiv = document.getElementById("post");

myButton.addEventListener("click", function() {
  myDiv.innerHTML = "New content";
  myDiv.classList.add("highlight");
});