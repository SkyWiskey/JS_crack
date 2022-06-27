function getApiKey() {
    var t = (new Date).getTime()
      , e = encryptApiKey();
    return t = encryptTime(t),
    comb(e, t)
}

//splice() 方法用于添加或删除数组中的元素。
// 注意：这种方法会改变原始数组。
function encryptApiKey() {
    var t = 'a2c903cc-b31e-4547-9299-b6d07b7631ab'
      , e = t.split("")
      , r = e.splice(0, 8);
    return e.concat(r).join("")
}

function encryptTime(t) {
    var e = (1 * t + 1111111111111).toString().split("")
      , r = parseInt(10 * Math.random(), 10)
      , n = parseInt(10 * Math.random(), 10)
      , o = parseInt(10 * Math.random(), 10);
    return e.concat([r, n, o]).join("")
}


function comb(t, e) {
    var r = "".concat(t, "|").concat(e);
    return btoa(r)
}

console.log(getApiKey())