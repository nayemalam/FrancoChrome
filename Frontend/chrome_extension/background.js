// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

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
document.getElementById('bg').src = "http://35.203.43.62:8080" + imageRequest.responseText;
document.getElementById('photo_desc').innerHTML = imageRequest.getResponseHeader("Description");
console.log(imageDescription);

var wordRequest = new XMLHttpRequest();
wordRequest.open("GET", "http://35.203.43.62:8080/word?date=" + today, true);
wordRequest.send();
document.getElementById('word').innerHTML  = wordRequest.responseText;
document.getElementById('translation').innerHTML = wordRequest.getResponseHeader("Translation");
//var newWord = wordRequest.responseText;
console.log(newWord);
