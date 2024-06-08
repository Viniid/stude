# Vetores

cidade <- c("Brasilia",
            "São Paulo",
            "Rio de Janeiro",
            "Porto Alegre"
            )

cidade

temperatura <- c(32,22,35,17)

regiao <- c(1,2,2,3)

temperatura

regiao

?c() # Combine Values into a Vector or List

# Acessando o Primeiro Elemento

cidade[1]

# A1cessando Interevalos

cidade[2:4]
cidade[2:1]

# Copiando um Vetor

cidade2 <- cidade
cidade2

# Excluindo um elemento FOgo no Rio

cidade2[-3] # apaga para consulta

cidade2[3] <- "Belo Horizonte" # define a posição e o novo elemento a ser adicionado

# Adicionando um novo elemento define a possição e em seguida o novo valor  

cidade2[5] <- "Curitiba"

cidade2

# Deletando um vetor teste para elementos tbm, teste realizado e não, esta função só apaga os valores do vetor

cidade <- NULL

cidade2 <- cidade 

cidade2 <- NULL

?NULL
cidade[3] <- "Belo Horizonte"

cidade[5] <- "Curitiba"

# Fator ---------------------------------------------------------------------------------------------------------------

?factor

UF <- factor(c("DF","SP","MG","SC","PR"))

UF

grau.instrucao <- factor(c("Nível Médio",
                           "Superior",
                           "Nível Médio",
                           "Fundamental"),
               levels = c("Fundamental",
                          "Nível Médio",
                          "Superior"),
               ordered = TRUE)

grau.instrucao

# Lista----------------------------------------------------------------------------------------------------------

?list #Lists – Generic and Dotted Pairs

pessoa <- list(sexo = "M", cidade = "Brasilia", idade = 20)

pessoa

pessoa[1] <- "F"
pessoa[2] <- "São Paulo"
pessoa[3] <- 22

pessoa

# É possivel apagar as variaveis com null e especifica-las por string ou numeros ex: ""pessoa [["idade"]]

pessoa[4] <- NULL

# Filtrando elementos da lista 

pessoa[c("cidade","idade")]

# Lista de Listas

cidades <- list(cidade = cidade, temperatura = temperatura , regiao = regiao)

cidades 

# Criando um data frame com vetores-------------------------------------------------------------------------------------

?df

df <- data.frame(cidade,temperatura)# deu erro a primeira vez pois não tinham a mesma quantidade de elementos


temperatura[5] <- 21 # ao que me parece é necessario ter a mesma quantidade de elementos para realizar o cruzamento de informação


df <- data.frame(cidade,temperatura)


# exato é necessario ter a mesma quantidade

df

df2 <- data.frame(cidades)

df2

# Filtrando valores do data frame

df[1, 1] # ex: Matriz, com retorno de dois valores

df[1,] # com um retorno só, uma coluna inteira ou uma linha

df2 [,1]

# selecionando as 3 primeiras linhas da primeira e ultima coluna

df2[c(1:3), c(1,3)]

# é possivel selecionar qual coluna  e a quantidade de linha a serem exebidas
 df2[c(1:5), c(1,3)]
       # primeiro se trata da onde inicia o intervalo
         # segundo se trata da onde termina o intervalo da quantidade de linhas
               # terceiro valor estipulado se trata de qual coluna ira aparecer 
                 # quarto se trata da qual coluna sera exibida
 regiao[5] <- 1
temperatura[5] <- 19

# é possivel verificar o nome da colunas

names(df2)

#é possivel verificar a quantidade de colunas e linhas dimensão

dim(df2)

# é possivel verificar quais são os tipos de dados


str(df2)

# acessando uma coluna do dataframe

df$cidade

df['cidade']


# Matriz-------------------------------------------------------------------

?matrix()

m <- matrix(seq(1:9), nrow = 3)

m

# armazena dados tabulares e um unico tipo de dado

m2 <- matrix(seq(1:25),
             ncol = 5, # determina a quantidades de colunas de uma matriz
             byrow = TRUE, # determina que será prenchidas por linhas 
             dimnames = list(c(seq(1:5)), # especifica quais são os nomes das linhas e colunas
                             c("A","B","C","D","E")
                             )
             )
             
m2

# Tambem é possivel filtrar a matriz 

m2[c(1:2),c("B","C")] # para isso é preciso especificar as linhas e as colunas em conchetes 

#---------------------------------------------------------------------------------------------------------------------------

#Estrutura de repetiçâo

# Loop

# For
# For (valor in sequencia){
#   codigo...
# }

for (i in seq(12)){ # i é o valor estipulado, in = dentro, seq é a sequencia a ser alcançadae em {} é o metodo ou função. 
  print(i)
}


# while
# while (codificao){
    # codigo
#                   }

# While similar a python

i <- 0
while (i <= 10) {
  print(i)
  i = i + 1
}

# Controle de fluxo "if"

#Controle de fluxo

# if(condição){}
#   código...
# }

x = 10
if (x>0){
  print("Numero Positivo")
}

# exemplo 2

nota = 5
if (nota >= 7) {
  print("Aprovado")
} else if (nota >= 5 && nota < 7 ) {
  print("Recuperação")
} else {
  print("Reprovado")
}


#---------------------------------------------------------------------------------------------------------------------
# Funções

par.impar <- function(num){
  if((num %% 2)==0){         # %% = divido
    return("Par")
  }else
    return("Impar")
}
  
  
num = 3
par.impar(num)

#---------------------------------------------------------------------------------------------------
# funções Apply

# Apply 

?apply

x <- seq(1:9)
matriz <- matrix(x,ncol=3)
matriz

result1 <- apply(matriz, 1, sum) # soma da linha 
result1

result2 <- apply(matriz , 2, sum) # soma da coluna 
result2

#---------------------------------------------------------------------------------------------------

?list

numeros.p <- c(2,4,6,8,10,12)
numeros.i <- c(1,3,5,7,9,11)
numeros <- list(numeros.p,numeros.i)

numeros

#----------------------------------------------------------------------------------------------------

?lapply

lapply(numeros, mean) #$ apresenta os valores separados

?sapply
sapply(numeros, mean) # apresenta os valores juntos

#-----------------------------------------------------------------------------------------------------

# Graficos

?mtcars

carros <- mtcars[c(1,2,9)]

head(carros)

hist(carros$mpg) # histograma

plot(carros$mpg,carros$cyl) # dispersão

library(ggplot2)
 
install.packages("ggplot2")

ggplot(carros,aes(am))+
  geom_bar()

#---------------------------------------------------------------------------------------------

# junções join

install.packages("dplyr")
library(dplyr)

dfv <- data.frame(Produto = c(1,2,3,5), Preco = c(15,10,25,20))
head(dfv)

dfp <- data.frame(Produto = c(1,2,3,4), Nome = c("A","B","C","D"))
head(dfp) # imprimir na tela a tabela

dfvp1 <- left_join(dfv,dfp,"Produto")
head(dfvp1)


dfvp2 <- right_join(dfv,dfp,"Produto")
head(dfvp2)


dfvp <- inner_join(dfv,dfp,"Produto")
head(dfvp)

#----------------------------------------------------------------------------------
# selecionando dados com R

#DPLYR
?iris

head(iris) # apresntar as informações em tabelas

glimpse(iris) # apresenta informações

# Filter - filtrando os dados - apenas versicolor
 
versicolor <- filter(iris,Species == "versicolor")
dim(versicolor)

# Slice - selecionando algumas linhas especificas

slice(iris, 5:10)

# Select - selecionando algumas colunas

select(iris,2:4)

# Select- todas colunas exceto Spal width

select(iris, -Sepal.Width)

# é possivel manipular as colunas  # MUTAGE

iris2 <- mutate(iris, nova.coluna = Sepal.Length + Sepal.Width)

iris2[,c("Sepal.Length","Sepal.Width","nova.coluna")]

#------------------------------------------------------------------------------------


# Arrenge - Ordenar

?arrange
select(iris,Sepal.Length) %>%
arrange(Sepal.Length)  

# Group by
iris %>% group_by(Species) %>% # para executar mais de um operador é necessario adicionar percentual maior que percentual "%>%"
  summarise(mean(Sepal.Length))

#-----------------------------------------------------------------------------------


#Tidyr

library(tidyr)

install.packages("tidyr")

# Quantidade de vendas por ano e produto

dfData <- data.frame(Produto=c("A","B","C"),
                     A.2015 = c(10,12,20),
                     A.2016 = c(20,25,35),
                     A.2017 = c(15,20,30)
                     )
head(dfData)

?gather

dfDate2 <- gather(dfData, "Ano", "Quantidade", 2:4)

head(dfDate2)

?separate
dfDate3 <- separate(dfDate2, Ano, c("A","Ano"))

dfDate3 <- dfDate3[-2]
dfDate3

# Acrescentando uma coluna Mes

dfDate3$Mes <- c('01','02','03')

dfDate3

?unite # une colunas

dfDate4 <-dfDate3 %>%
  unite(Date, Mes, Ano, sep='/')

head(dfDate4)
















