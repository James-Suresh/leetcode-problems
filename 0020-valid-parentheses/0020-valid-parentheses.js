/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var list = []
    for (let i=0;i<s.length;i++)
        {
             if (s.charAt(i)=="{")
                {
                 list.push("{")               
                }
         if (s.charAt(i)=="(")
                {
                   list.push("(")                       
                }
     if (s.charAt(i)=="[")
                {
                   list.push("[")                        
                }
            
            if (s.charAt(i)=="}")
                {
                 if(list.pop()!="{")
                     {return false}
                }
         if (s.charAt(i)==")")
                {
                   if(list.pop()!="(")
                     {return false}                       
                }
     if (s.charAt(i)=="]")
                {
                   if(list.pop()!="[")
                     {return false}                       
                }
    
        }
    if(list.length==0){
        return true;
     }
    else{
        return false;
    } 
        
   
};