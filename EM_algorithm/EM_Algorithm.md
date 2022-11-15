# EM Algorithm

EM(**E**xpectation-**M**aximization) algorithm은 MLE(Maximum Likelihood Estimator)를 찾기위한 알고리즘 중 하나다.
MLE를 찾는 가장 단순한 방법은 Likelihood function을 계산하고 미적분학을 이용해 해석적으로 최적해를 찾는 것이다.
그러나, 복잡한 모델에서는 Likelihood function을 이용해 최적해를 찾는 일은 어려울때가 많다.
EM algorithm은 이 문제를 비교적 쉬운 최대화 문제의 반복으로 대체하여 해결한다.
이러한 최대화 문제를 반복적으로 풀면 그 해는 결국 MLE로 수렴하게 되는 것이 기본적인 아이디어다.

EM algorithm을 개념적으로 이해하기 어렵게 만드는 것은 **missing data** 개념이다. 
Missing data는 머신러닝에서는 **latent variable**이라고도 불린다.
EM algorithm은 이러한 missing data 또는 latent variable을 이용하는 문제에 적합하다.


## Statistical Example

$X_1, \ldots, X_n$와 $Y_1, \ldots, Y_n$은 서로 독립이고 각각의 확률변수는 $X_i \tilde Poisson(\tau_i)$, $Y_i \tilde Poisson(\beta \tau_i)$를 따른다고 하자.
