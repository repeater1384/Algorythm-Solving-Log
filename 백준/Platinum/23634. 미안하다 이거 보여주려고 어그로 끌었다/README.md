# [Platinum V] 미안하다 이거 보여주려고 어그로 끌었다 - 23634 

[문제 링크](https://www.acmicpc.net/problem/23634) 

### 성능 요약

메모리: 415012 KB, 시간: 3416 ms

### 분류

너비 우선 탐색(bfs), 자료 구조(data_structures), 분리 집합(disjoint_set), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>난 나뭇잎 마을의 초대 호카게인 센쥬 하시라마의 동생, 센쥬 토비라마라고 한다. 지금 우리 마을은 크나큰 위기에 빠져있다. 우리와 끊이지 않는 악연을 지닌 우치하 가문의 수장 우치하 마다라가 구미를 끌고 마을을 습격했기 때문이지. 형은 호카게로서 마다라와 전투를 벌이고 있고 마을 주민들에게 피해가 갈까 봐 제대로 전투하지 못하고 있어. 지금 놈의 화둔이 마을로 넘어오지 못하게 우리 형의 목둔이 막아주고 있으니 나무가 크게 불타기 전에 미리 주민들을 대피시켜야 해. 나뭇잎 마을을 지키려면 네 도움이 필요해. </p>

<p>현재 상황은 마을 뒷산에서 전투가 일어나고 있고, 형의 나무가 불길을 막아서고 있어. 지도를 통해 살펴보면 마을 뒷산은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span></mjx-container>의 직사각형의 격자에 해당하는 형태임을 알 수 있지. 아, 지도의 밖은 돌로 둘러싸여 있어 불이 퍼질 수 없으니 걱정하지 마.</p>

<p>불은 상하좌우로 인접한 나무를 통해서만 퍼져나갈 수 있고, 어떤 날에서 그다음 날로 넘어갈 때, 각 불은 동시에 퍼지게 돼. 불과 접촉한 나무는 다음 날 전부 불에 타서 불길이 되어버려. 하지만, 돌이 있는 지역은 불이 붙지 않아. </p>

<p>너도 알다시피 대피에는 시간이 굉장히 중요해. 우리는 주민들이 안전히 대피할 수 있도록 만날 수 있는 모든 불이 합쳐지는 최소 시간과 그때의 불의 크기를 구해야만 해. 불이 돌에 막혀 모든 불이 하나로 합쳐지지 않을 수도 있는데, 그럴 땐 합쳐질 수 있는 모든 불이 합쳐지는 최소 시간과 그때의 불의 크기의 합을 구하면 돼.</p>

<p>불이 합쳐진다는 것은 불이 다른 불과 상하좌우로 인접하게 되는 것을 뜻하고, 불의 크기는 불이 붙은 칸의 개수를 말해.</p>

<p>부탁해! 어서! 문제를 해결해서 우리 마을과 형에게 도움을 줘!</p>

### 입력 

 <p>첫 번째 줄에 지도의 크기를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mtext class="mjx-n" space="2"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>,</mo><mtext> </mtext><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N,~ M$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>2</mn><mo>,</mo><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N, M \leq 2,000$</span></mjx-container>)</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N + 1$</span></mjx-container>번째 줄까지 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0, 1, 2$</span></mjx-container>로 이루어진 첫날 지도가 표시된다. (불 = <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>, 나무 = <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>, 돌 = <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>)</p>

### 출력 

 <p>만날 수 있는 모든 불이 만나는 최소 시간과 그때의 불의 크기의 합을 출력한다. 첫날은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>일차이다. 즉, 처음부터 합칠 수 있는 모든 불이 합쳐져 있다면 최소 시간은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>이다.</p>

<p>만약 퍼질 불이 없다면, "<code>0 0</code>"을 출력한다.</p>

