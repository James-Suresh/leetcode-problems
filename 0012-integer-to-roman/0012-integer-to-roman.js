/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let Roman = "";
    let num2 = 0;// number of multiples
    if(num>= 1000)
    {
        num2 = Math.trunc(num/1000)
     for(let i = 0;i<num2;i++)
    {
        Roman +="M"
    }
    num = num - (1000*num2)
    }
   
    if(num >=500)
    {
    num2 = Math.trunc(num/100)
     if(num2==9)
     {
         Roman += "CM"
        num = num - 900
     }
     else{
         Roman +="D"
        num = num - 500
     }
        
    }

    if(num>=100)
    {
    num2 = Math.trunc(num/100)
     if(num2==4)
     {
         Roman += "CD"
         num =num -400
     }
     else{
         for(let i = 0;i<num2;i++)
    {
        Roman +="C"
    }
    num=num-(100*num2)
    }
    }

    if(num>=50)
    {
    num2 = Math.trunc(num/10)
     if(num2==9)
     {
         Roman += "XC"
        num = num - 90
     }
     else{
        Roman +="L"
        num = num - 50
     }
    }

    if(num>=10)
    {
     num2 = Math.trunc(num/10)
     if(num2==4)
            {
                Roman += "XL"
            }
     else
     {
          for(let i = 0;i<num2;i++)
            {
                Roman +="X"
            }

     }
   
    num=num-(10*num2)
    }

    if(num>=5)
    {
        if(num==9)
            {
                Roman += "IX"
                num = num - 9
            }
        else{
            
        Roman +="V"
        num = num -5 
        }
    }

    if(num>=1)
    {
     num2 = Math.trunc(num/1)
     
     if(num2==4){
         Roman += "IV"
        num = num -4
     }
     else{
                
            for(let i = 0;i<num2;i++)
            {
                Roman +="I"
            }
            }
            num=num-(1*num2)
    }

    return Roman;

};