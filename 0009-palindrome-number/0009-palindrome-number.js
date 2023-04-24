/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let arr = x.toString().split('');
    console.log(arr)
    let i = 0;
    let j = arr.length - 1;
    
    while (i < arr.length) {
        if (arr.at(i) !== arr.at(j)) {
            return false;
        } else {
            i++;
            j--;
        }
    }
    return true;
    
};