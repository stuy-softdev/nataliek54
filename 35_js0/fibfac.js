//Team cerulean
//SoftDev pd5
//K35 - Basic functions in JavaScript
//2026-01-08r

//JavaScript implementations of recursive Scheme functions

//factorial:
function fact(n) {
  if (n == 0){
    return 1;
  }
  else {
    return n * fact(n - 1)
  }
}

//TEST CALLS
// (writing here beforehand will facilitate EZer copy/pasting into dev console now and later...)

console.log(fact(1))
console.log(fact(5))
console.log(fact(10))
console.log('YIPPEE!!')

//fib:

function fib(n) {
    if (n == 0){
        return 0;
    }
    else {
        return n + fib(n - 1)
    }
}

//TEST CALLS
// (writing here beforehand will facilitate EZer copy/pasting into dev console now and later...)

console.log(fib(1))
console.log(fib(5))
console.log(fib(10))
console.log('YIPPEE!!')
