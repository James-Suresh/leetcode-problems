/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    var longestIndex = 0;
    var longestNum = String(strs[0].length)
    for(let i =0;i<strs.length;i++)
    {
 var strlen = String(strs[i]).length
        if(strlen>longestNum)
        {
       longestNum = strlen;
       longestIndex = i;
        }
    }

    var sIndex = 0;
    var sNum = String(strs[0].length)
    for(let i =0;i<strs.length;i++)
    {
 var strlen = String(strs[i]).length
        if(strlen<sNum)
        {
       sNum = strlen;
       sIndex = i;
        }
    }
    let output = ""
    let complete = false
    let check = String(strs[sIndex]);
    for (let i =0;i<strs.length;i++)
    { 
        let word = String(strs[i])
        if(word=="")
        {
            check=""
            break;
        }
        
        for(let j=0;j<word.length;j++)
        {
          if(word[j] != check[j])
        {
            check = check.substring(0,j);
            break;
        }   
        }
        
    }
    
    return check
};

