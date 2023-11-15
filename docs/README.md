# Primeira MSG
Eu vou te mandar uma explicacao minha, e tbm 
mando foto do meu caderno e do codigo q eu fiz 
pro trabalho pra te ajudar a entender mehor, blz?
E qualquer coisa q nao ficar claro, pode perguntar.

# Segunda MSG
Seguinte, nessa fatoração, QR completa, a matriz Q
vai ser uma matriz ortogonal e a matriz R vai ser 
triangular superior. Basicamente, vc vai ter que ir,
aos poucos, aniquilando todos os valores de uma certa
linha da matriz A pra ela ir ficando triangular superior
(ai vc encontra R) e a matriz Q vai ser aquilo que, quando
multiplicado por R, vai resultar em A. Pra ir fazendo essa
aniquilacao da matriz A, vc precisa seguir o método de householder
ou de givens. Eu sei mais sobre householder até pq acho
q ele mais facil. O q eu lembro de givens é q ele elemina
um elemento só por vez, enquanto householder ja elimina
todo mundo q vc quer eliminar daquela coluna.
Para calcular a matriz de householder, vc vai ter uma matriz A.
Ai vc vai, usando a primeira linha dessa matriz A,
calcular um vetor u (vou mandar foto de como calcula ele).
Tendo esse vetor u, vc encontra sua matriz de householder
fazendo H = I - 2uu^t. Esse I é uma identidade n por n,
onde n é o número de linhas da matriz A.

Pra encontrar o R final, vc vai primeiro pegar a matriz A
e calcular a matriz de householder dela. Ai vc vai ter uma
matriz R1 (um R parcial, q ainda nao acabou o processo)
que vai ser HA (matriz de householder vezes matriz A).
Dps disso, vc vai pegar uma submatriz da matriz R1 que
nao tenha nem a primeira linha, nem a primeira coluna
e calcular a matriz de householder pra essa submatriz.
Quando vc fizer isso, essa matriz de householder que tu
calcular não vai ter o tamanho certo. Ela vai ter ser
completada com uma coluna e uma linha. Essa coluna e essa
linha vao entrar a esquerda e em cima e vão ser [1000...]
(seja a linha ou a coluna). Basicamente, vc vai pegar essa
matriz de householder pequena e colocar ela dentro de uma
matriz identidade q seja do tamanho certo, sobrescrevendo
os elementos. Ai vc vai ter uma nova matriz H do tamanho
certo. Com isso, pra encontrar R2 basta fazer HR1 (matriz
H vezes a matriz R1 q vc tinha). Dps, vc vai pegar uma
submatriz de R2 que nao tenha nem as duas priemeiras linhas,
nem as duas primeiras colunas. Ai vc repete todo o processo
q vc fez antes até chegar numa R3. E por assim vai até
vc ter uma matriz Rn triangular superior q vai ser sua matriz R final.

A matriz Q vc pode inicializar ela como uma matriz identidade
que tenha o mesmo tamanho da matriz de householder, ou seja,
uma matriz n por n com n sendo o numero de linhas de A.
A cada matriz H que vc encontrar pra ir calculando a matriz R,
vc vai multiplicar a matriz Q q vc tiver pela matriz H transposta.
Ou seja, vc vai ter que fazer, por exemplo, Q3 = Q2H^t
(onde essa matriz H vai ser aquela usada pra encontrar
a matriz R3, mas transposta nesse caso). Ai no final
vc vai ter as matrizes Q e R que são a fatoração de A.

# Terceira MSG
O vetor u vc encontra assim. Vc vai ter uma matriz pra aniquilar,
com householder, os elementos da primeira coluna dela, exceto o
primeiro elemento. Ai vc vai pegar um vetor a1 que seja essa
primeira coluna dessa matriz e vai pegar um vetor bem simples
que é esse e1. O vetor e1 é um vetor da base canonica, que
tem a priemeira coordenada 1 e todo o resto é zero, sendo
que ele tem o mesmo tamanho que o vetor a1. Ai com isso vc
tem o vetor u e pode encontrar a matriz de householder.

# Quarta MSG
Isso é o q teve sobre esse tema naquela aula

e essa é a parte do meu codigo relativa a essa fatoracao

o resto do trabalho ta bem explicadinho no pdf q ele mandou, mas se nao entender algo pode perguntar tbm q eu tento explicar
