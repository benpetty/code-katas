import { gcd } from './gcd';


const cases = [
  [10, 20, 10],
  [2, 4, 2],
  [5, 10, 5],
  [3, 4, 1],
  [0, 0, 0],
  [461952, 116298, 18],
  [7966496, 314080416, 32],
  [24826148, 45296490, 526],
  [12, 0, 12],
  [0, 9, 9],
];

describe('test gcd', () => {
  test.each(cases)(
    "given %p and %p as arguments, returns %p",
    (arg1, arg2, expected) => {
      const result = gcd(arg1, arg2);
      expect(result).toBe(expected);
    });
});
