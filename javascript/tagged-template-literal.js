// Adapted from http://exploringjs.com/es6/ch_template-literals.html#_escaping-in-tagged-template-literals-cooked-versus-raw
function describe(tmplObj, ...substs) {
    return {
        Cooked: merge(tmplObj, substs),
        Raw: merge(tmplObj.raw, substs),
        Substs: substs
    };
}
function merge(tmplStrs, substs) {
    // There is always at least one element in tmplStrs
    let result = tmplStrs[0];
    substs.forEach((subst, i) => {
        result += String(subst);
        result += tmplStrs[i+1];
    });
    return result;
}
