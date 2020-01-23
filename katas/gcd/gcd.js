

/**
 * In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an
 * efficient method for computing the greatest common divisor (GCD) of two
 * numbers, the largest number that divides both of them without leaving a
 * remainder. It is named after the ancient Greek mathematician Euclid, who
 * first described it in his Elements (c. 300 BC). It is an example of an
 * algorithm, a step-by-step procedure for performing a calculation according
 * to well-defined rules, and is one of the oldest algorithms in common use.
 * It can be used to reduce fractions to their simplest form, and is a part of
 * many other number-theoretic and cryptographic calculations.
 *
 * https://en.wikipedia.org/wiki/Euclidean_algorithm
 *
 * @param {Number} x
 * @param {Number} y
 */
export const gcd = (x, y) => {

  let z;

  while(y) {
    z = y;
    y = x % y;
    x = z;
  }

  return x;
}

