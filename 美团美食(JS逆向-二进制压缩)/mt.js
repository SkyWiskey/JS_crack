var jv = 'https://hz.meituan.com/meishi/api/poi/getPoiList?cityName=杭州&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=2&userId=2513934978&uuid=9ffd2bba19834bad9443.1656047928.1.0.0&platform=1&partner=126&originUrl=https://hz.meituan.com/meishi/pn2/&riskLevel=1&optimusCode=10'
iP.reload = function(jv) { //jv => 请求地址 拼接参数（不带token）
    var jw;
    var jx = {};
    // 判断生成jx
    if (typeof jv === _$_543c[91]) {
        jx = iO.parse(jv.split(_$_543c[146])[1])
    } else {
        if (typeof jv === _$_543c[2]) {
            jx = jv
        }
    }

    //iJ
    var iJ = function(je) {
        var jd = [];
        var ck = Object.keys(je).sort();
        ck.forEach(function(jf, bx) {
            if (jf !== _$_543c[136] && jf !== _$_543c[137]) {
                jd.push(jf + _$_543c[122] + je[jf])
            }
        });
        jd = jd.join(_$_543c[121]);
        return iI(jd)
    };
    // iI
    var iI = function(jc) {
        jc = cD.deflate(JSON.stringify(jc));
        jc = iD(jc);
        // 返回ip.sign
        return jc
    };

    // ip
    var iP = {
        rId: Rohr_Opt.Flag,
        ver: _$_543c[138],
        ts: new Date().getTime(),
        cts: new Date().getTime(),
        brVD: iN(),
        brR: iM(),
        bI: iL(),
        mT: [],
        kT: [],
        aT: [],
        tT: [],
        aM: iK()
    };

    // iJ处理jx
    iP.sign = iJ(jx);
    // 生成时间戳
    iP.cts = new Date().getTime();

    // iI处理ip
    jw = iI(iP);
    // 判断
    if (Rohr_Opt.LogVal && typeof (window) !== _$_543c[0]) {
        window[Rohr_Opt.LogVal] = encodeURIComponent(jw)
    }
    // 最后jw就是_token
    ;return jw
}
