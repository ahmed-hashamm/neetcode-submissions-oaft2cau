class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        int maxProf=INT_MIN;
        int l=0,r=1;
        while(r<n){
            if(prices[l]<prices[r]){
                int currProf=prices[r]-prices[l];
                maxProf=max(currProf,maxProf);
            }
            else{
                l=r;
            }
            r++;
        }
    if(maxProf>0){
        return maxProf;
    }
    else{
        return 0;
    }
    }
};
