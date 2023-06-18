class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int len = flowerbed.length;
        if (len == 1 && flowerbed[0] == 0){
            return true;
        }
        if (len >= 2 && flowerbed[0] == 0 && flowerbed[1] == 0){
            count++;
        }
        if (len >= 2 && flowerbed[len-1] == 0 && flowerbed[len-2] == 0){
                        if (len == 2){
                count--;
            }
            count++;
        }  
        for (int i = 1; i < len-3; i++){
            if (flowerbed[i] == 0 && flowerbed[i+1] == 0){
                if (flowerbed[i+2] == 0){
                    count++;
                    i++;
                }
            }
        }
        return count >= n;
    }
}