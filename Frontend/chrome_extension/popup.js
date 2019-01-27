'use strict';

var todayDate = (getAllDate());


var cookieRequest = new XMLHttpRequest();
cookieRequest.open("GET", "http://35.203.43.62:8080/register", false);
cookieRequest.withCredentials = true;
cookieRequest.send(null);


getAllElements(todayDate);

function getAllDate() {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; //January is 0!
  var yyyy = today.getFullYear();

  if (dd < 10) {
    dd = '0' + dd;
  }
  if (mm < 10) {
    mm = '0' + mm;
  }
  today = mm + '/' + dd + '/' + yyyy;
  return today;
}

function getAllElements(date){
  var objectRequest = new XMLHttpRequest();
  debugger;
  objectRequest.open("GET", "http://35.203.43.62:8080/image?date="+ date, false);
  objectRequest.send();
  document.getElementById('bg').src = "http://35.203.43.62:8080" + objectRequest.responseText;
  document.getElementById('photo_desc').innerHTML = objectRequest.getResponseHeader("img_description");
  document.getElementById('word').innerHTML  = objectRequest.getResponseHeader("word");
  document.getElementById('meaning').innerHTML = objectRequest.getResponseHeader("translation");
  var audioFile = "http://35.203.43.62:8080" + objectRequest.getResponseHeader("audio_file");
  document.getElementById('sound').src = audioFile;


}


document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('sound-btn').addEventListener('click', playAudio);
    document.getElementById('next-btn').addEventListener('click', getNextWord);

});


function playAudio() {
  (sound).play();
}

// ADD CURRENT time
var display=setInterval(function(){Time()},0);
var date=new Date();
var time=date.toLocaleTimeString();
document.getElementById("time").innerHTML=time;
