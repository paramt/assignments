ports = []
components = []
images = []

index = 0;

function previous(){
    if(index > 0){
        index--;
    } else {
        index = 30;
    }

    document.getElementById("port").innerHTML = ports[index];
    document.getElementById("component").innerHTML = components[index];
    document.getElementById("image").src = images[index];
}

function next(){
    if(index  <30){
        index++;
    } else {
        index = 0;
    } 

    document.getElementById("port").innerHTML = ports[index];
    document.getElementById("component").innerHTML = components[index];
    document.getElementById("image").src = images[index];
}
