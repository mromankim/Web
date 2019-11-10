console.log('here - ive just changed the JS')

function myFunction(x) {
  x.classList.toggle("change");
}


/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementByClass("openbtn").style.marginLeft = "250px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementByClass("openbtn").style.marginLeft = "0";
}


var coll = document.getElementsByClassName("collapsible");
debugger;

var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    console.log('we are getting to the code')
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
