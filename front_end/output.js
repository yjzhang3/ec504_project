function getPics(org1, org2){
    // document.getElementById("img-l").src = "pics\\" + org1 + ".jpg";
    // document.getElementById("img-r").src = "pics\\" + org2 + ".jpg";
    document.getElementById("img").src = "pics\\" + org1 + "_" + org2 + ".png";
}

function getResults(org1, org2){
    // var dir = "/results/" + org1 + "_" + org2 + ".json";
    // alert(dir);

    var fileName = org1 + "_" + org2 + ".json";
    // alert(fileName);

    // parse in the JSON and name it results

    document.getElementById("result").textContent = "Result: " + results.LCCS_len;
    document.getElementById("edge correctness").textContent = "Edge Correctness: " + results.edge_correctness;
    document.getElementById("LCCS_len").textContent = "LCCS_len: " + results.LCCS_len;
}

window.onload = function(){
    var info = document.location.search.replace(/^.*?\?org1=/, '');
    var orgs = info.split("&org2=");
    var org1 = orgs[0].replace("%20", ' ');
    var org2 = orgs[1].replace("%20", ' ');
    getPics(org1, org2);
    getResults(org1, org2);
}

document.getElementById("btn-back").addEventListener("click", function(){
    window.location.href = "input.html";
});
