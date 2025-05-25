class Solution 
{
    public int longestPalindrome(String[] words) 
    {
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) 
        {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        int length = 0;
        boolean hasCenter = false;
        for (String word : map.keySet()) 
        {
            String rev = new StringBuilder(word).reverse().toString();
            int freq = map.get(word);

            if (!word.equals(rev) && map.containsKey(rev)) 
            {
                int pair = Math.min(freq, map.get(rev));
                length += pair * 4;
            
                map.put(word, map.get(word) - pair);
                map.put(rev, map.get(rev) - pair);
            }
        }
        for (String word : map.keySet()) 
        {
            if (word.charAt(0) == word.charAt(1)) 
            {
                int freq = map.get(word);
                int pair = freq / 2;
                length += pair * 4;
            
                if (freq % 2 == 1)
                {
                    hasCenter = true;
                } 
            }
        }

        if (hasCenter) 
        {
            length += 2;
        }

        return length;
    }
}