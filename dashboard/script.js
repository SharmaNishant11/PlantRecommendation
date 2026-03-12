// API endpoints
const predictUrl = "http://127.0.0.1:5000/predict";
const dataUrl = "http://127.0.0.1:5000/data";
const simulateUrl = "http://127.0.0.1:5000/simulate";

// RUN MANUAL PLANT RECOMMENDATION


function runRec(){

const temp = parseFloat(document.getElementById("temperature").value);
const humidity = parseFloat(document.getElementById("humidity").value);
const moisture = parseFloat(document.getElementById("moisture").value);
const light = parseFloat(document.getElementById("light").value);

fetch(predictUrl,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
temperature:temp,
humidity:humidity,
soil_moisture:moisture,
light_intensity:light
})
})
.then(res=>res.json())
.then(data=>{

let plants=[];

if(data.final_recommendations){
plants=data.final_recommendations;
}
else if(data.ml_recommendations){
plants=data.ml_recommendations;
}

const list=document.getElementById("results");
list.innerHTML="";

plants.forEach(p=>{
const li=document.createElement("li");
li.textContent=p;
list.appendChild(li);
});

})
.catch(err=>{
console.error(err);
alert("API connection failed");
});

}


// LIVE SENSOR DASHBOARD


const labels=[];
const moistureData=[];
const tempData=[];

const ctx=document.getElementById("sensorChart").getContext("2d");

const sensorChart=new Chart(ctx,{
type:"line",
data:{
labels:labels,
datasets:[
{
label:"Soil Moisture",
data:moistureData
},
{
label:"Temperature",
data:tempData
}
]
},
options:{
responsive:true,
animation:false
}
});



// UPDATE DASHBOARD FROM FLASK


function updateDashboard(){

// simulate sensor values for demo
fetch(simulateUrl)
.then(()=>fetch(dataUrl))
.then(res=>res.json())
.then(data=>{

document.getElementById("tempValue").textContent=data.temperature;
document.getElementById("humidityValue").textContent=data.humidity;
document.getElementById("moistureValue").textContent=data.soil_moisture;
document.getElementById("lightValue").textContent=data.light;

const time=new Date().toLocaleTimeString();

labels.push(time);
moistureData.push(data.soil_moisture);
tempData.push(data.temperature);

if(labels.length>20){
labels.shift();
moistureData.shift();
tempData.shift();
}

sensorChart.update();

})
.catch(err=>{
console.log("Dashboard update failed",err);
});

}


// AUTO REFRESH EVERY 3 SECONDS
setInterval(updateDashboard,10000);