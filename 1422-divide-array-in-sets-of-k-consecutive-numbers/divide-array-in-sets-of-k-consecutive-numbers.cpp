class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        if (nums.size() % k != 0) {
            return false;
        }
        map<int, int> cards;
        for (int n : nums) {
            cards[n]++;
        }
       
        while (!cards.empty()) {
            
            int minCard = cards.begin()->first; 

            for (int i = 0; i < k; i++) {
                int current = minCard + i;

                if (cards.find(current) == cards.end()) {
                    return false;
                }
                cards[current]--;
                if (cards[current] == 0) {
                    cards.erase(current);
                }
            }
        }
        
        return true;
    }
};
