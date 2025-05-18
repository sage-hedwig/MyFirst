from collections import Counter
import heapq as he
class Solution:
    def longestSubarray(self, arr, k):
        add = []
        for x in range(len(arr)):
            for y in range(x+1,len(arr)+1):
                i = arr[x:y]
                if len(i) > k and len([j for j in i if j<=k]) < k:
                    add.append(i)
        return len(max(add, key = len))
    



    def findMissing(self, arr):
        cnt = Counter([arr[x]-arr[x-1] for x in range(1,len(arr))])
        diff = cnt.most_common(1)[0][0]
        for x in range(1,len(arr)):
            if arr[x]-arr[x-1] != diff:
                return (arr[x-1] + diff)
            
            

    def findSubString(self, str):
        set1 = set(str)
        req = len(set1)
        lis=[]
        for x in range(len(str)):
            for y in range(x+1,len(str)+1):
                i = len(str[x:y])
                if i >= req:
                    if set(str[x:y]) == set1:
                        lis.append(i)
        return min(lis)
    

    def findMaximumNum(self, s, k):
        lis = [int(x) for x in s]
        larg = he.nlargest(len(lis),lis)
        for x in range (k):
            new = lis[:]
            i= x
            j = new.index(larg[x])
            if j<i:
                j = len(new) - 1 - next(i for i, val in enumerate(reversed(new)) if val == larg[x])
            new[i], new[j] = new[j], new[i]
            
            if new != lis:
                lis = new[:]
            else:
                cnt = 1
                while x+cnt<len(lis):
                    new = lis[:]
                    i = x+cnt
                    j = new.index(larg[x])
                    if j<i:
                        j = len(new) - 1 - next(i for i, val in enumerate(reversed(new)) if val == larg[x+cnt])
                    new[i], new[j] = new[j], new[i]
                    if new != lis:
                        lis = new[:]
                        cnt = len(lis)
                    cnt+=1
        return (str(lis)[1:-1].replace(', ',''))


    def mostBooked(self, n, meeting):
        room = [0 for _ in range(n)]  # Tracks room availability (0 = free, 1 = occupied)
        pair = {}  # Maps end times to room indices
        wait_pair = []  # Queue for waiting meetings
        t = 0  # Current time
        meeting.sort()  # Sort meetings by start time
        cnt = {}  # Tracks the number of bookings for each room
        start = [x[0] for x in meeting]  # List of start times
        end = [x[1] for x in meeting]  # List of end times
        max_end = max(end)  # Maximum end time of all meetings
        while t<max_end:  # Iterate through time up to the latest end time
            # Free up rooms whose meetings have ended
            while t in pair.keys():
                room[pair[t]] = 0  # Mark the room as free
                del pair[t]  # Remove the room from the pair dictionary
    
            # Assign rooms to waiting meetings or new meetings
            while 0 in room:
                rom = room.index(0)  # Find the first available room
                if wait_pair:  # If there are waiting meetings
                    x = wait_pair.pop(0)  # Get the first waiting meeting
                    room[rom] = 1  # Mark the room as occupied
                    pair[x[1] + (t - x[0])] = rom  # Update the end time for the room
                    max_end = max(max_end, x[1])  # Update the maximum end time
                    cnt[rom] = cnt.get(rom, 0) + 1  # Increment the booking count
                elif t in start:  # If a new meeting starts at this time
                    idx = start.index(t)  # Find the index of the meeting
                    x = meeting[idx]  # Get the meeting details
                    start[idx] = -1  # Mark the meeting as processed
                    room[rom] = 1  # Mark the room as occupied
                    pair[x[1]] = rom  # Update the end time for the room
                    cnt[rom] = cnt.get(rom, 0) + 1  # Increment the booking count
                else: 
                    break  # No more meetings to process at this time
    
            # Add meetings to the waiting queue if no rooms are available
            while 0 not in room and t in start:
                idx = start.index(t)  # Find the index of the meeting
                wait_pair.append(meeting[idx])  # Add the meeting to the waiting queue
                start[idx] = -1  # Mark the meeting as processed
    
        # Return the room with the maximum bookings (tie-breaking by smallest index)
        return max(cnt.items(), key=lambda x: (x[1], -x[0]))[0] if cnt else -1


    def subarraySum(self, arr, target):
        l=0
        sum_of_num = 0
        for r in range(len(arr)):
            sum_of_num += arr[r]
            while sum_of_num > target:
                sum_of_num -= arr[l]
                l += 1 
            if sum_of_num == target:
                return [l+1,r+1]
        return [-1]


    
    def sort012(self, arr):
        one = two = three = 0

        # First pass: Count number of 0s, 1s, and 2s — O(n)
        for x in arr:
            if x == 0:
                one += 1
            elif x == 1:
                two += 1
            else:
                three += 1

        # Second pass: Overwrite arr in-place — O(n)
        i = 0
        for _ in range(one):
            arr[i] = 0
            i += 1
        for _ in range(two):
            arr[i] = 1
            i += 1
        for _ in range(three):
            arr[i] = 2
            i += 1


    

    def findLargest(self,arr):
        sepp = []
        for x in arr:
            for y in x:
                sepp.append(y)
        sepp.sort(reverse=True)
        return ''.join(map(str,sepp))




    def minJumps(self, arr):
        curr = 0
        avai = []
        steps = 0
        while curr!=len(arr)-1:
            if curr == 0:
                return -1
            elif curr + arr[curr] >= len(arr)-1:
                return steps + 1
            avai = {arr[x]+x:arr[x] for x in range(curr+1, curr+arr[curr]+1)}
            best_opt = max(avai.keys())
            curr = best_opt-arr[avai[best_opt]]
            steps += 1
        return steps



    def countSubarray(self,arr, n, k):
        l=0
        cnt=0
        bigger = []
        for r in range (n):
            bigger.append(arr[r])
            while max(bigger)<=k:
                bigger.remove(arr[l])
                l+=1
                
                
            cnt+=1
        return cnt

    def kTop(self,a, N, K):
        dic = {}
        ret=[]
        for x in a:
            dic[x] = dic.get(x,0)+1
            sorted_dic = sorted(dic.items(), key=lambda x: (-x[1],x[0]))
            print(type(sorted_dic))
            try:
                re = []
                for y in range(K):
                    re.append(sorted_dic[y][0])
                ret.append(re)
            except:
                re =[]
                for y in sorted_dic:
                    re.append(y[0])
                ret.append(re)
        return ret




sol = Solution()
print(sol.kTop([5,2,1,2],4,3))
            
