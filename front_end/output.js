function getPics(org1, org2){
    // document.getElementById("img-l").src = "pics\\" + org1 + ".jpg";
    // document.getElementById("img-r").src = "pics\\" + org2 + ".jpg";
    document.getElementById("img").src = "pics\\" + org1 + "_" + org2 + ".png";
}

function getResults(org1, org2){
    var json_3a_3b = {"result": [["0", "5"], ["3", "6"], ["4", "7"], ["1", "3"], ["2", "4"]], "edge_correctness": 1.0, "LCCS": ["0", "1", "2", "3", "4"], "LCCS_len": 5};
    var json_3a_6b = {"result": [["0", "1"], ["3", "14"], ["4", "5"], ["1", "27"], ["2", "33"]], "edge_correctness": 0.8, "LCCS": ["0", "1", "2", "3", "4"], "LCCS_len": 5};
    var json_3a_7b = {"result": [["0", "0"], ["1", "4"], ["2", "3"], ["3", "2"], ["4", "5"]], "edge_correctness": 0.8, "LCCS": ["0", "1", "2", "3", "4"], "LCCS_len": 5};
    var json_6a_3b = {"result": [["5", "17"], ["3", "4"], ["4", "11"], ["6", "2"], ["7", "15"], ["8", "5"]], "edge_correctness": 0.7142857142857143, "LCCS": ["3", "4", "5"], "LCCS_len": 3};
    var json_6a_6b = {"result": [["13", "1"], ["1", "7"], ["6", "22"], ["2", "18"], ["18", "6"], ["5", "21"], ["9", "30"], ["11", "8"], ["17", "0"], ["4", "3"], ["12", "29"], ["16", "15"], ["14", "11"], ["3", "5"], ["19", "9"], ["8", "38"], ["7", "27"], ["10", "33"], ["15", "17"], ["0", "19"]], "edge_correctness": 0.5172413793103449, "LCCS": ["0", "2", "17", "13", "1", "6", "18", "11", "7", "16", "19", "4", "12", "15", "3", "9", "14", "5", "8", "10"], "LCCS_len": 20};
    var json_6a_7b = {"result": [["8", "13"], ["0", "9"], ["2", "6"], ["7", "5"], ["3", "18"], ["4", "7"], ["1", "11"], ["9", "3"], ["5", "15"], ["6", "16"]], "edge_correctness": 0.6190476190476191, "LCCS": ["0", "2", "8", "1", "4", "9", "6", "7", "5", "3"], "LCCS_len": 10};
    var json_7a_3b = {"result": [["1", "5"], ["2", "6"], ["0", "7"], ["4", "3"], ["3", "4"]], "edge_correctness": 0.5714285714285714, "LCCS": ["0", "1", "2", "4", "3"], "LCCS_len": 5};
    var json_7a_6b = {"result": [["1", "1"], ["2", "23"], ["0", "11"], ["4", "5"], ["3", "33"]], "edge_correctness": 0.5714285714285714, "LCCS": ["0", "1", "2", "3"], "LCCS_len": 4};
    var json_7a_7b = {"result": [["1", "8"], ["2", "0"], ["0", "1"], ["4", "9"], ["3", "3"]], "edge_correctness": 0.8571428571428571, "LCCS": ["0", "1", "2", "4", "3"], "LCCS_len": 5};

    var json;

    if (org1 == "3a") {
        if (org2 == "3b") {
            json = json_3a_3b;
        } else if (org2 == "6b") {
            json = json_3a_6b;
        } else {
            json = json_3a_7b;
        }
    } else if (org1 == "6a") {
        if (org2 == "3b") {
            json = json_6a_3b;
        } else if (org2 == "6b") {
            json = json_6a_6b;
        } else {
            json = json_6a_7b;
        }
    } else {
        if (org2 == "3b") {
            json = json_7a_3b;
        } else if (org2 == "6b") {
            json = json_7a_6b;
        } else {
            json = json_7a_7b;
        }
    }

    var i;
    var out = "";
    for (i = 0; i < json.result.length; i++) {
        out += "[" + json.result[i] + "] ";
    }

    document.getElementById("result").textContent = "Result: " + out;
    document.getElementById("edge correctness").textContent = "Edge Correctness: " + json.edge_correctness;
    document.getElementById("LCCS_len").textContent = "LCCS_len: " + json.LCCS_len;
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
