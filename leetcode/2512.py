class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        p = set(positive_feedback)
        n = set(negative_feedback)
        l = []
        for i in range(len(report)):
            sc = 0
            for w in report[i].split(' '):
                if w in p:
                    sc += 3
                elif w in n:
                    sc -= 1
            l.append((student_id[i], sc))
        l.sort(key=lambda x:(-x[1], x[0]))
        return [x[0] for x in l][:k]