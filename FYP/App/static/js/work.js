async function getData(){
    const xs = [];
    const ys =[];
    
    
    const x = await fetch('http://localhost/App/static/js/Price.csv'); 
    const data = await x.text();
    const table = data.split('\n').slice(1);

    table.forEach(elt => {
        const cols =elt.split(',');
        const Date = cols[0];
        const price = cols[1];
        xs.push(Date);
        ys.push(price);
    });
    return {xs,ys};

}

    async function chartIt(){
    const data = await  getData();
    const ctx = document.getElementById('PriceChart').getContext('2d');
    
    const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: data.xs,
        datasets: [{
            fill: false,
            label: 'Price of Djia',
            data: data.ys,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
            }]
        }
    });
}
chartIt();
