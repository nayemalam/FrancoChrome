'use strict';

var currDate = (getAllDate());


getAllElements(currDate);

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
  var serverIP = "http://127.0.0.1:8080"

  var objectRequest = new XMLHttpRequest();
  objectRequest.open("GET", serverIP + "/image?date="+ date, false);
  objectRequest.withCredentials = true;
  objectRequest.send();
  debugger;
  document.getElementById('bg').src = serverIP + objectRequest.responseText;
  document.getElementById('photo_desc').innerHTML = objectRequest.getResponseHeader("img_description");
  document.getElementById('word').innerHTML  = objectRequest.getResponseHeader("word");
  document.getElementById('meaning').innerHTML = objectRequest.getResponseHeader("translation");
  var audioFile = serverIP + objectRequest.getResponseHeader("audio_file");
  document.getElementById('sound').src = audioFile;


}


document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('sound-btn').addEventListener('click', playAudio);
    document.getElementById('next-btn').addEventListener('click', getNextWord);

});


function playAudio() {
  (sound).play();
}

function getNextWord(){
  debugger;
  getAllElements(currDate);
}

// ADD CURRENT TIME
clock();


function clock() {
  var now = new Date();
  var TwentyFourHour = now.getHours();
  var hour = now.getHours();
  var min = now.getMinutes();
  var mid = 'pm';
  if (min < 10) {
    min = "0" + min;
  }
  if (hour > 12) {
    hour = hour - 12;
  }
  if(hour==0){
    hour=12;
  }
  if(TwentyFourHour < 12) {
     mid = 'am';
  }
  document.getElementById('currTime').innerHTML = hour+':'+min + mid ;
  setTimeout(clock, 1000);
}
