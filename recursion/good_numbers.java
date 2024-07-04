class Solution {

  private long MOD = 1_000_000_007;

  public int countGoodNumbers(long n) {
      long even = (n+1)/2;
      long odd = n/2;
      long first = pow(5, even)%MOD;
      long second = pow(4, odd)%MOD;
      return (int)((first*second)%MOD);
  }

  private long pow(long x, long n) {
      if(n == 0) return 1;
      long res = pow(x, n/2);

      if(n % 2 == 0) {
          return (res * res)%MOD;
      } else {
          return (res * res * x)%MOD;
      }
  }
}

/*
 * Lets consider any number of length 5.
 * There will be (n+1)/2 even indices, there will be n/2 odd indices.
 * Also, every position can have at most 5 even digits, and 4 prime digits.
 * There the number of good even numbers will be 5^((n+1)/2) and number of good odd numbers will be 4^(n/2)
 */