class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        String s1="";
        int count1=0;
        int count2=0;
        int count3=0;
        
            for(int i=0;i<s.length();i++)
            {
                if (!s1.contains(String.valueOf(s.charAt(i))))
                {
                    s1+=String.valueOf(s.charAt(i));
                    count1++;                    
                }
                else
                {
                    count3++;
                    i=count3-1;
                    if(count1>count2)
                    {
                        count2=count1;
                    }
                    count1=0;
                    s1="";
                }
            }
                
        System.out.print(s1);
            if(count1>count2)
            return count1 ;
                    
            else
            return count2 ;           
    }
}