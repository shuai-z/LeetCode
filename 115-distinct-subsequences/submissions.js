/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
  var cache = [[]];
  for (var i = 0; i < s.length; i++) {
    cache.push(new Array(t.length+1));
  }
  return f(s, 0, t, 0, cache);
};

function f(s, i, t, j, cache) {
  if (cache[i][j] !== undefined) return cache[i][j];
  if (j === t.length) return 1;
  if (s.length - i < t.length - j) return 0;
  cache[i+1][j] = f(s, i+1, t, j, cache);
  if (s[i] === t[j]) {
    cache[i+1][j+1] = f(s, i+1, t, j+1, cache);
    return (cache[i][j] = cache[i+1][j+1] + cache[i+1][j]);
  }
  return (cache[i][j] = cache[i+1][j]);
}
