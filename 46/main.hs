import Data.List

-- A sieve to produce prime numbers up to 'n'
sieve [] = []
sieve (p:xs) = p : sieve [x | x <- xs, rem x p > 0]
primesieve n = sieve [2..n]

---- Perform set diff on two sorted arrays
--listdiff [] _ =  []
--listdiff xs [] = xs
--listdiff (x:xs) (y:ys) = case 

-- 2 * sqr
doubleSqrs n = [2 * (x^2) | x <- [1..n]]

main = let dsqrs = doubleSqrs 10000
           primes = primesieve 1000000
           odds = [x | x <- [3..1000000], rem x 2 > 0]
       in print odds

