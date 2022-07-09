class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        sp = set(passengers)
        buses.sort()
        passengers.sort()
        bus_cap = [0] * len(buses)
        bp = 0
        last_pass = 0
        for i, p in enumerate(passengers):
            while bp < len(buses) and p > buses[bp]:
                bp += 1
            if bp == len(buses):
                break
            last_pass = p
            bus_cap[bp] += 1
            if bus_cap[bp] == capacity:
                bp += 1
        start = last_pass-1
        if bus_cap[-1] != capacity:
            start = buses[-1]
        for i in range(start, 0, -1):
            if i not in sp:
                return i