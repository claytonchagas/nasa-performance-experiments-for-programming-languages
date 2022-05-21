#!/usr/bin/env Rscript

library(rbenchmark)
library(binaryLogic)
library(stringr)
n = (150)

# Get the number num of the Pernicious numbers to find from the command line.
if (length(n) == 0) {
  stop("At least one argument must be supplied n", call.=FALSE)
} else if (length(n) == 1) {
  num <- as.integer(n[1])
}


get_number_of_ones <- function(n) {
  # Find the number of ones in the binary representation of a number.
  #
  # Args:
  #   n: Integer value
  # 
  # Returns:
  #   The number of ones.
  n_bin <- as.binary(n)
  n_str <- toString(n_bin)
  count_ones <- sum(str_count(n_str, "1"))
  return(count_ones)
}


is_prime_number <- function(n) {
  # Determine if a number is a prime.
  #
  # Args:
  #   m: The number to check.
  # 
  # Returns:
  #   True/False
  flag = FALSE
  if (n < 2) {
    flag = FALSE
  } else if (n == 2) {
    flag = TRUE
  } else if (any(n %% 2:(n-1) == 0)) {
    flag = FALSE
  } else { 
    flag = TRUE
  }
  
  return(flag)
}


find_pernicious_numbers <- function(n) {
  # Find the first n pernicious numbers.
  i <- 1
  counter <- 0
  while (counter < n) {
    if (is_prime_number(get_number_of_ones(i))) {
      counter <- counter + 1
      #cat("Pernicious ", n, ":", counter, i, get_number_of_ones(i), '\n')
    }
    i <- i + 1
  }
  return(i-1)
}
print(find_pernicious_numbers(n))


cat('---------------------------------------------\n')
cat(' Determine the Pernicious numbers \n')
cat('---------------------------------------------\n')

benchmark("find_pernicious_numbers" = { find_pernicious_numbers(n) },
          replications = 1,
          columns = c("test", "replications", "elapsed", "relative", "user.self", "sys.self"))
print(benchmark(find_pernicious_numbers(n)))



