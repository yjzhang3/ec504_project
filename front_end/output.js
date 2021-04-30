function getPics(org1, org2){
    document.getElementById("img-l").src = "pics\\" + org1 + ".jpg";
    document.getElementById("img-r").src = "pics\\" + org2 + ".jpg";
}

window.onload = function(){
    var info = document.location.search.replace(/^.*?\?org1=/, '');
    var orgs = info.split("&org2=");
    var org1 = orgs[0].replace("%20", ' ');
    var org2 = orgs[1].replace("%20", ' ');
    getPics(org1, org2);
}

document.getElementById("btn-back").addEventListener("click", function(){
    window.location.href = "input.html";
});
