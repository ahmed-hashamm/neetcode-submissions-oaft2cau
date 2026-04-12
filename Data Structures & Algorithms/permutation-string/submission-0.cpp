class Solution {
public:

    bool isSameFreq(int freq[], int winFreq[]){
        for(int i=0 ; i<26; i++){
            if(freq[i]!=winFreq[i]){
                return false;
            }
            
        }
        return true;
    }
    bool checkInclusion(string s1, string s2) {
        int freq[26]={0};
        for(int i=0; i< s1.length(); i++){
            freq[s1[i]-'a']++;
        }
        int windSize=s1.length();
    for(int i=0 ; i<s2.length(); i++){
        int windIdx=0,idx=i;
        int winFreq[26]={0};
        while(windIdx < windSize && idx < s2.length()){
            winFreq[s2[idx]-'a']++;
            idx++; windIdx++;
        }

    if(isSameFreq(freq, winFreq)){
        return true;
    }
    }
    return false;
    }
};
