# [Gold IV] 트리 순회 - 22856 

[문제 링크](https://www.acmicpc.net/problem/22856) 

### 성능 요약

메모리: 56760 KB, 시간: 368 ms

### 분류

그래프 이론, 그래프 탐색, 트리

### 문제 설명

<p>노드가 $N$개인 이진 트리가 있다. 트리를 중위 순회와 유사하게 순회하려고 한다. 이를 <strong>유사 중위 순회</strong>라고 하자.</p>

<p>순회의 시작은 트리의 루트이고 순회의 끝은 중위 순회할 때 마지막 노드이다. 이때 루트 노드는 항상 1번 노드이다.</p>

<p>유사 중위 순회는 루트 노드에서 시작하며, 다음과 같이 진행된다.</p>

<ol>
	<li>현재 위치한 노드의 왼쪽 자식 노드가 존재하고 아직 방문하지 않았다면, 왼쪽 자식 노드로 이동한다.</li>
	<li>그렇지 않고 현재 위치한 노드의 오른쪽 자식 노드가 존재하고 아직 방문하지 않았다면, 오른쪽 자식 노드로 이동한다.</li>
	<li>그렇지 않고 현재 노드가 유사 중위 순회의 끝이라면, 유사 중위 순회를 종료한다.</li>
	<li>그렇지 않고 부모 노드가 존재한다면, 부모 노드로 이동한다.</li>
	<li>유사 중위 순회를 종료할 때까지 1 ~ 4를 반복한다.</li>
</ol>

<p style="text-align: center;"><img alt="" src="" style="height: 392px; width: 600px;"></p>

<p>위 그림에 있는 트리에서 중위 순회를 한다면 $4 \rightarrow 2 \rightarrow 5 \rightarrow 1 \rightarrow 6 \rightarrow 3 \rightarrow 7$ 순으로 순회를 한다.</p>

<p>따라서, <strong>유사 중위 순회의 끝</strong>은 노드 7이 된다.</p>

<p style="text-align: center;"><img alt="" src="" style="height: 421px; width: 600px;"></p>

<p><strong>유사 중위 순회</strong>는 위 그림과 같이 루트인 노드 $1$에서 시작하여 노드 $7$에서 끝나고 $1 \rightarrow 2 \rightarrow 4 \rightarrow 2 \rightarrow 5 \rightarrow 2 \rightarrow 1 \rightarrow 3 \rightarrow 6 \rightarrow 3 \rightarrow 7$ 이와 같은 순서로 순회를 진행한다. <strong>유사 중위 순회</strong>를 진행하면서 총 10번 이동하였다.</p>

<p>여기서 이동이라는 것은 하나의 노드에서 다른 노드로 한번 움직이는 것을 의미한다. 예를 들면, 노드 1에서 노드 2로 가는 것을 한번 이동하였다고 한다.</p>

<p><strong>유사 중위 순회</strong>를 하면서 이동한 횟수를 구하려고 한다.</p>

### 입력 

 <p>첫 번째 줄에 트리를 구성하는 노드의 개수 $N$이 주어진다.</p>

<p>두 번째 줄부터 $N + 1$ 번째 줄까지 현재 노드 $a$, 현재 노드의 왼쪽 자식 노드 $b$, 현재 노드의 오른쪽 자식 노드 $c$가 공백으로 구분되어 주어진다. 만약 자식 노드의 번호가 -1인 경우 자식 노드가 없다는 것을 의미한다.</p>

### 출력 

 <p>유사 중위 순회를 하면서 이동한 총 횟수를 출력한다.</p>

