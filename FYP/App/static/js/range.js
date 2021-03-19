var slider = document.getElementById("myRange");
var output = document.getElementById("value");
var pos=document.getElementById("pos");
var neg=document.getElementById("neg");
var neu=document.getElementById("neu");

output.innerHTML = slider.value;

slider.oninput = async function (){
    const Data = await getData();
    output.innerHTML=this.value;
    pos.innerHTML=Data.pos[this.value-1];
    neg.innerHTML=Data.neg[this.value-1];
    
}

async function getData(){
    const pos = [];
    const neg = [];
    const neu = [];
    var data =await fetch('http://localhost/App/AppData/test.csv');
    var d = await data.text();
    const table = d.split('\n');
     
    table.forEach(elt => {
        var cols = elt.split(',');
        const p = cols[0];
        const ng = cols[1];
        const nu = cols[2];
        pos.push(p);
        neg.push(ng);
        neu.push(nu);
    });

    return {pos,neg,neu};
}