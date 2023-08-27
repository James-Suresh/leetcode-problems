class Solution {
    public int myAtoi(String s) {
    
        double num=0;
        int Atoi=0;
        boolean neg=false;
        boolean numeric=true;
        boolean sign=false;
        boolean numbefore=false;
      
        for (int i=0;i<s.length();i++)
        {
          
            // if(s.charAt(i))
        try {
            num = (10*num) + (Double.parseDouble(String.valueOf(s.charAt(i))));
            System.out.println(num);
        } catch (NumberFormatException e) {
            numeric = false;
        }
             
            if(numeric==false)
            {
                numeric=true;
                if(sign==true)
                {break;}
                if(s.charAt(i)=='-')
                {
                    sign=true;
                    neg=true;
                }
                else if(s.charAt(i)!=' '&&s.charAt(i)!='+')
                {
                
                    break;
                }
                
                if(s.charAt(i)=='+'||s.charAt(i)=='-')
                {
                    sign=true;
                    
                    if(numbefore==true)
                    {
                        neg=false;
                        break;
                    }
                }
                 if(s.charAt(i)==' ')
                {
                    
                    if(numbefore==true)
                    {
                        break;
                    }
                }
   
            }
            else{
                numbefore=true;
            }
            
            
        }
        if(neg==true)
           {
               num*=-1;
           }
            
            if(num<-1*(Math.pow(2,31)))
            {
                num=-1*(Math.pow(2,31));
                Atoi=(int) num;
            }
            else if(num>=(Math.pow(2,31)))
            {
                num=Math.pow(2,31)-1;
                Atoi=(int) Math.pow(2,31);
            }
            else{
                Atoi=(int) num;
            }
           
        
        return Atoi;
    }
}