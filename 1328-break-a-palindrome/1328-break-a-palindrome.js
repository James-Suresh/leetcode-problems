/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    function palindromeCheck(palindrome){
        let str = palindrome
        let start = 0
        let end = str.length-1
        
        while (start<end)
        {
            if(str.charAt(end)!==str.charAt(start))
            {
                return false
            }
            start++
            end--
        }
        return true
    }

    
        let str = ""
        let counter=0;
        let letter='a'
        let a_count=0
        //lol
        //aba
        //
        while((palindromeCheck(str))&&palindrome.length>1){
            if(letter==='a'){
            str = palindrome
            let strArray = str.split("")
            if(strArray[counter]==='a'){
                a_count=counter
            }
            strArray[counter]=letter
            counter++
            if(counter===str.length)
            {
                letter='b'
                counter=0
            }
            str = strArray.join("")
            }
            else{
            str = palindrome
            let strArray = str.split("")
            strArray[a_count]=letter;
            str = strArray.join("")
            }
        }
        return str
    
};