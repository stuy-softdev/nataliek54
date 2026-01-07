#lang racket

; Natalie Keiger
; cerulean
; 01-07-2026
; K-34
; 10ish minutes

(define (fact n)
  (if (< n 0)
      "Cannot use negative numbers"
      (if (= n 0)
          1
           (* n (fact (- n 1))))))

(define (fib n)
    (if (< n 0)
      "Cannot use negative numbers"
      (if (= n 0)
          0
          (+ n (fib (- n 1))))))

(fact 4)
(fact 7)
(fact 1)
(fact 2)
(fact -3)
(fib 1)
(fib 5)
(fib 3)
(fib 10)
(fib -1)

