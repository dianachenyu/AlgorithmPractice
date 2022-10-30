class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # {creator : [total, highest_view, id]}
        count = dict()
        for creator, id, view in zip(creators, ids, views):
            if creator not in count:
                count[creator] = [view, view, id]
            else:
                count[creator][0] += view
                if view > count[creator][1] or (view == count[creator][1] and id < count[creator][2]):
                    count[creator][1] = view
                    count[creator][2] = id
        
        max_total_view = max(count[creator][0] for creator in count)
        res = []
        for creator, (total_view, max_view, id) in count.items():
            if max_total_view == total_view:
                res.append([creator, id])
        return res 
                
