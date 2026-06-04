class Solution {
public:

    string encode(vector<string>& strs) {
        int n = strs.size();
        string encoded = "";
        for(int i=0;i<n;i++){
            encoded += strs[i];
            encoded += "\n";
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> ans;

        int m = s.size();
        string cur="";
        for(int i=0;i<m;i++){
            
            if(s[i]=='\n'){
                ans.push_back(cur);
                cur="";
            }
            else{
                cur += s[i];
            }
        }
        
        return ans;
    }
};
