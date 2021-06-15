// a key map of allowed keys
var allowedKeys = {
  37: 'left',
  38: 'up',
  39: 'right',
  40: 'down',
  65: 'a',
  66: 'b',
  79: 'o',
  82: 'r',
  68: 'd',
  69: 'e',
  54: '6',
  80: 'p',
  84: 't',
  89: 'y',
  73: 'i',
  77: 'm',
  13: 'enter'
};

// the 'official' Konami Code sequence
var konamiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a', 'enter'];

// a variable to remember the 'position' the user has reached so far.
var konamiCodePosition = 0;

// add keydown event listener
document.addEventListener('keydown', function(e) {
  // get the value of the key code from the key map
  var key = allowedKeys[e.keyCode];
  // get the value of the required key from the konami code
  var requiredKey = konamiCode[konamiCodePosition];

  // compare the key with the required key
  if (key == requiredKey) {

    // move to the next key in the konami code sequence
    konamiCodePosition++;

    // if the last key is reached, activate cheats
    if (konamiCodePosition == konamiCode.length) {
      activateCheats();
      konamiCodePosition = 0;
    }
  } else {
    konamiCodePosition = 0;
  }
});

function activateCheats() {
  document.body.style.background = "url('../../static/cheatBackground.jpg') repeat center center fixed";
  document.body.style.backgroundSize = "cover";
  
  var audio = new Audio('../static/audio/1up.mp3');
  audio.play();

  $('.easter').empty();

  alert("KONAMI CODE");
}


// ORDER 66
// a key map of allowed keys
var order66 = ['o', 'r', 'd', 'e', 'r', '6', '6', 'enter'];

// a variable to remember the 'position' the user has reached so far.
var order66Position = 0;

// add keydown event listener
document.addEventListener('keydown', function(e) {
  // get the value of the key code from the key map
  var key = allowedKeys[e.keyCode];
  // get the value of the required key from the konami code
  var requiredKey = order66[order66Position];

  // compare the key with the required key
  if (key == requiredKey) {

    // move to the next key in the konami code sequence
    order66Position++;

    // if the last key is reached, activate cheats
    if (order66Position == order66.length) {
      executeCheats();
      order66Position = 0;
    }
  } else {
    order66Position = 0;
  }
});

function executeCheats() {
  document.body.style.background = "url('../../static/order66.gif') repeat center center fixed";
  document.body.style.backgroundSize = "35%";
  document.body.style.fontcolor = "red";

  
  var delayInMilliseconds = 4000;

  var audio66 = new Audio('../static/audio/order66.mp3');
  audio66.play();

  setTimeout(function() {
    var audio = new Audio('../static/audio/younglings.mp3');
    
    audio.play();
  }, delayInMilliseconds);


  $('.easter').empty();

  $('.welcome').empty();
  $('.welcome66').append('YOU WERE THE CHOSEN ONE!!');

  alert("EXECUTE ORDER 66");
}





// Party
// a key map of allowed keys
var party = ['p', 'a', 'r', 't', 'y', 't', 'i', 'm', 
'e', 'enter'];

// a variable to remember the 'position' the user has reached so far.
var partyPosition = 0;

// add keydown event listener
document.addEventListener('keydown', function(e) {
  // get the value of the key code from the key map
  var key = allowedKeys[e.keyCode];
  // get the value of the required key from the konami code
  var requiredKey = party[partyPosition];

  // compare the key with the required key
  if (key == requiredKey) {

    // move to the next key in the konami code sequence
    partyPosition++;

    // if the last key is reached, activate cheats
    if (partyPosition == party.length) {
      partyCheats();
      partyPosition = 0;
    }
  } else {
    partyPosition = 0;
  }
});

function partyCheats() {
  var duration = 15 * 1000;
  var animationEnd = Date.now() + duration;
  var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

  function randomInRange(min, max) {
    return Math.random() * (max - min) + min;
  }

  var interval = setInterval(function() {
    var timeLeft = animationEnd - Date.now();

  if (timeLeft <= 0) {
    return clearInterval(interval);
  }

  var particleCount = 50 * (timeLeft / duration);
  // since particles fall down, start a bit higher than random
  confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
  confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
}, 250);
}