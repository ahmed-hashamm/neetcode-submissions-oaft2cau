class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen  = new Set()  //using hash set
        for(let i of nums){
            if(seen.has(i)) return true
            seen.add(i)
        }
        return false
    }
}
