const { getStates, getCities, getPostcodes, findPostcode } = require("../index");

// console.log(getStates());
// console.log(getCities("Wilayah Persekutuan Putra Jaya"));
// console.log(getPostcodes("Wilayah Persekutuan Kuala Lumpur", "Bangunan Bangkok Bank"));
// console.log(findPostcode("62988"));
    
test('Should contain city Jerteh', () => 
{ 
    expect(findPostcode("22020").city === "Jerteh").toBe(true);
});
