/*
  your PPTASK:
  
  First, familiarize yourself with the given html file for this work.

      then...

  Test drive each bit of code in this file,
  and insert comments galore, indicating anything
  you discover,
  have questions about,
  or otherwise deem notable.

  Have the given html file open as you work.
  
  Write with your future self or teammates in mind.
  
  If you find yourself falling out of flow mode, consult 
  - other teams
  - MDN

  A few comments have been pre-filled for you...
  
  (delete this block comment once you are done)
*/





// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K37 -- Getting more comfortable with the dev console and the DOM
// 2026-01-12m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

addItem('Hello');

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

removeItem(8);

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
// FAC
// GCD

function fact(n) {
  if (n == 0){
    return 1;
  }
  else {
    return n * fact(n - 1)
  }
}

function fib(n) {
    if (n == 0){
        return 0;
    }
    else {
        return n + fib(n - 1)
    }
}

function gcd(a, b) {
    let min = Math.min(a, b);

    while (min > 0) { 
        // just go through each number and check if both are divisible
        if (a % min == 0 && b % min == 0) {               
            return min;
        }
        else {
            min--;
        }
        return 1;
    }

}

addItem('Fact of 6: ' + String(fact(6)))
addItem('Fib of 6: ' + String(fib(6)))
addItem('GCD of 6 and 12: ' + String(gcd(6, 12)))

stripe()


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    // body
    return retVal;
};


