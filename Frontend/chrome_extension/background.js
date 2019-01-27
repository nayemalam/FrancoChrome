'use strict';

var todayDate = (getAllDate());
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
  playAudio(audioFile);
}


function playAudio(audioFile) {
  document.getElementById('sound').src = audioFile;
  (sound).play();
}
