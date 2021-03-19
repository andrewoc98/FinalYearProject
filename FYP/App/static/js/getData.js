//looping through directory

async function getData(){
    const dirnames = ["http://localhost/App/AppData/News/","http://localhost/App/AppData/Sentiment/","http://localhost/App/AppData/Sentiment+News/"];
    const innerFolders = ["SlidingWindow1Day(s)/","SlidingWindow5Day(s)/","SlidingWindow10Day(s)/","SlidingWindow12Day(s)/"];
    const fileName = "prediction.csv";
    var FileData = [];


    var i;
    var j;

    var pos = [];
    var neg = [];
    var neu = [];

    for(i=0; i<dirnames.length; i++){
        for(j=0; j<innerFolders.length; j++){
            //gives list of all files

            data = await fetch(dirnames[i]+innerFolders[j]+fileName);
            var d = await data.text();
            var table = d.split('\n');

            table.forEach(elt => {
                var cols = elt.split(',');
                var p = cols[0];
                var ng = cols[1];
                var nu = cols[2];
                pos.push(p);
                neg.push(ng);
                neu.push(nu);
        });
        FileData.push([pos,neg,neu]);

        }
    }
    
    return FileData;
}


var dropDown = document.getElementById("dropdown");
var otherDropdown = document.getElementById("otherDropdown");
var slider = document.getElementById("myRange");
var output = document.getElementById("value");
var pos=document.getElementById("pos");
var neg=document.getElementById("neg");
var neu=document.getElementById("neu");

output.innerHTML = slider.value;


slider.oninput = async function (){
    const Data = await getData();
    output.innerHTML=this.value;
    pos.innerHTML=Data[parseInt(dropDown.value*4)+parseInt(otherDropdown.value)][0][this.value-1];
    neg.innerHTML=Data[parseInt(dropDown.value*4)+parseInt(otherDropdown.value)][1][this.value-1];
    neu.innerHTML=Data[parseInt(dropDown.value*4)+parseInt(otherDropdown.value)][2][this.value-1];
    
}
