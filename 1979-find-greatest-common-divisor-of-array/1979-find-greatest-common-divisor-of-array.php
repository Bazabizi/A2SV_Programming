class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function GCD($a , $b){
        if ($b == 0){
            return $a;
        }
        return $this->GCD($b , $a%$b);
    }
    function findGCD($nums) {
        return $this->GCD(max($nums) , min($nums));
    }
}