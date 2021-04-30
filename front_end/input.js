document.getElementById("btn-submit").addEventListener("click", function(){
    var org1 = document.getElementById("org1").value;
    var org2 = document.getElementById("org2").value;
    alert("You've selected the following\n" + "Organism 1: " + org1 + "\nOrganism 2: " + org2);
    window.location.href = "output.html" + "?org1=" + org1 + "&org2=" + org2;
});
