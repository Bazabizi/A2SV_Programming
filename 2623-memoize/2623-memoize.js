/**
 * @param {Function} fn
 */
function memoize(fn) {
    var count = {}
    return function(...args) {
        var key = String(args);
        if(!(key in count)){
            count[key] = fn(...args);
        }
        return count[key];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */