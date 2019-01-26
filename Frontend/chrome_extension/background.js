'use strict';


console.log("hello ali bsdfj");

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

console.log("Date:" + today);

var imageRequest = new XMLHttpRequest();
debugger;
imageRequest.open("GET", "http://35.203.43.62:8080/image?date="+ today, false);
imageRequest.send();
var image = imageRequest.response;
var imageDescription = imageRequest.responseText;
console.log("Image Description" + imageDescription);
// var response = alert("hello");

var wordRequest = new XMLHttpRequest();
wordRequest.open("GET", "http://35.203.43.62:8080/word?date=" + today, false);
wordRequest.send();
var newWord = wordRequest.responseText;
console.log(newWord);

document.getElementById(bg).src=image;
