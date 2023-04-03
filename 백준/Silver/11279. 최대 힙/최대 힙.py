import sys
import heapq
heap = []
for _ in range(int(input())):
    cmd = int(sys.stdin.readline())
    if cmd:#삽입
        heapq.heappush(heap,-cmd)
    else:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)