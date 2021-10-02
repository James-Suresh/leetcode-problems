//https://leetcode.com/problems/zigzag-conversion/ 

class Solution {
    public String convert(String s, int numRows) {
        
        ArrayList<String> z = new ArrayList<String>();
        int zig=0; // Used for alternating between adding alphabets vertically. 
        int offset=0;     
        int itr=1; // Keeps track of iterations.
        String temp;
        
        for(int i=0;i<s.length(); i++){
            if(zig<numRows) // Creates and appends to rows vertically. 
            {
                if(itr==1){ // First iteration creates rows based on numRows.
                 
                    z.add(String.valueOf(s.charAt(i)));
                }
                else{ // Future iteration appends to the corresponding row.
                
                    temp=z.get(zig);
                    temp+=String.valueOf(s.charAt(i));
                    z.set(zig,temp);
                    
                }
                zig++;
            }
            else { // The following code appends alphabets to the rows diagonally.
                offset++;
               
                if(offset<=numRows-2)
                {    
                    temp=z.get((numRows)-offset-1);
                    temp+=String.valueOf(s.charAt(i));
                    z.set(((numRows)-offset-1),temp);
                   
                    
                }
                else // Resets variables to append vertically
                {
                    itr++;
                    offset=0;
                    zig=0;
                    i--;
                }
                
            
            }
           
        }
            s="";
         for(String zi:z)
            {
             s+=zi;        
            }
        return s;
    }
}