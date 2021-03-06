package autodesk;

import java.util.ArrayList;
import java.util.HashMap;

/*
 * Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
 * Examples:
 * s = "leetcode"
 * return 0.
 * s = "loveleetcode"
 * return 2.
*/
class FirstUnique {
    public int firstUniqChar(String s) {
      HashMap<Character,Integer> map = new HashMap<>();
        
        int n = s.length();
        
        for (int i =0;i<n;i++){
            char c = s.charAt(i);
            map.put(c,map.getOrDefault(c,0)+1);
        }
        for(int i=0;i<n;i++){
            if(map.get(s.charAt(i))==1){
                return i;
            }
        }
               return -1;
               
    }
   
    public static void main(String[] args) {
    	FirstUnique fu = new FirstUnique();
    	System.out.println(fu.checkPerfectNumber(28));
    }
}