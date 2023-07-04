document.addEventListener("DOMContentLoaded", function() {
 

  flatpickr('#dob', {
    dateFormat: 'Y-m-d',
  });

 
  
});

function showTab(tabId) {
  var tabs = document.getElementsByClassName('tab-content');
  for (var i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove('active');
  }
  document.getElementById(tabId).classList.add('active');
}