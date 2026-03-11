const apiUrl = "http://localhost:5000/predict";

function runRec(){

const temp = parseFloat(document.getElementById("temperature").value);
const humidity = parseFloat(document.getElementById("humidity").value);
const moisture = parseFloat(document.getElementById("moisture").value);
const light = parseFloat(document.getElementById("light").value);

fetch(apiUrl,{
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