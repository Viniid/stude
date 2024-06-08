## ----eval=FALSE---------------------------------------------------------------
#  install.packages("naivebayes")

## ----eval=FALSE---------------------------------------------------------------
#  install.packages("path_to_tar.gz", repos = NULL, type = "source")

## ----eval=FALSE---------------------------------------------------------------
#  library(naivebayes)

## ----fig.width=6,fig.height=6/1.618-------------------------------------------
# Section: General usage - Training with formula interface
library(naivebayes)

# Simulate data
n <- 100
set.seed(1)
data <- data.frame(class = sample(c("classA", "classB"), n, TRUE),
                   bern = sample(LETTERS[1:2], n, TRUE),
                   cat  = sample(letters[1:3], n, TRUE),
                   logical = sample(c(TRUE,FALSE), n, TRUE),
                   norm = rnorm(n),
                   count = rpois(n, lambda = c(5,15)))

# Split data into train and test sets
train <- data[1:95, ]
test <- data[96:100, -1]

# General usage via formula interface
nb <- naive_bayes(class ~ ., train, usepoisson = TRUE)

# Show summary of the model
summary(nb)

# Classification
predict(nb, test, type = "class") # nb %class% test

# Posterior probabilities
predict(nb, test, type = "prob") # nb %prob% test

# Tabular and visual summaries of fitted distributions for a given feature
tables(nb, which = "norm")
plot(nb, which = "norm")

# Get names of assigned class conditional distributions
get_cond_dist(nb)

## -----------------------------------------------------------------------------
# Section: Model fitting and classification using matrix/data.frame - vector interface
library(naivebayes)

# Simulate data
n_vars <- 10
n <- 1e6
y <- sample(x = c("a", "b"), size = n, replace = TRUE)

# Discrete features
X1 <- matrix(data = sample(letters[5:9], n * n_vars, TRUE),
             ncol = n_vars)
X1 <- as.data.frame(X1)

# Fit a Naive Bayes model using matrix/data.frame - vector interface
nb_cat <- naive_bayes(x = X1, y = y)

# Show summary of the model
summary(nb_cat)

# Classification
system.time(pred2 <- predict(nb_cat, X1))
head(pred2)

## ----fig.width=6,fig.height=6/1.618-------------------------------------------
# Section: Model estimation through a specialized fitting function
library(naivebayes)

# Prepare data (matrix and vector inputs are strictly necessary)
data(iris)
M <- as.matrix(iris[, 1:4])
y <- iris$Species

# Train the Gaussian Naive Bayes
gnb <- gaussian_naive_bayes(x = M, y = y)
summary(gnb)

# Parameter estimates
coef(gnb)
coef(gnb)[c(TRUE, FALSE)] # show only means
tables(gnb, 1)

# Visualization of fitted distributions
plot(gnb, which = 1)

# Classification
head(predict(gnb, newdata = M, type = "class")) # head(gnb %class% M)

# Posterior probabilities
head(predict(gnb, newdata = M, type = "prob")) # head(gnb %prob% M)

# Equivalent calculation via naive_bayes
gnb2 <- naive_bayes(M, y)
head(predict(gnb2, newdata = M, type = "prob"))

## ----eval=FALSE---------------------------------------------------------------
#  library(naivebayes)
#  
#  # Prepare data: --------------------------------------------------------
#  data(iris)
#  iris2 <- iris
#  N <- nrow(iris2)
#  n_new_factors <- 3
#  factor_names <- paste0("level", 1:n_new_factors)
#  
#  # Add a new categorical feature, where one level is very unlikely
#  set.seed(2)
#  iris2$new <- factor(sample(paste0("level", 1:n_new_factors),
#                             prob = c(0.005, 0.7, 0.295),
#                             size = 150,
#                             replace = TRUE), levels = factor_names)
#  
#  # Define class and feature levels: -------------------------------------
#  Ck <- "setosa"
#  level1 <- "level1"
#  level2 <- "level2"
#  level3 <- "level3"
#  
#  # level1 did not show up in the sample but we know that it
#  # has 0.5% probability to occur.
#  table(iris2$new)
#  
#  # Parameter estimation: ------------------------------------------------
#  
#  # ML-estimates
#  ck_sub_sample <- table(iris2$new[iris$Species == Ck])
#  ck_mle <-  ck_sub_sample / sum(ck_sub_sample)
#  
#  # Bayesian estimation via symmetric Dirichlet prior with concentration parameter 0.5
#  # (corresponds to the Jeffreys' uninformative prior)
#  
#  laplace <- 0.5
#  N1 <- sum(iris2$Species == Ck & iris2$new == level1) + laplace
#  N2 <- sum(iris2$Species == Ck & iris2$new == level2) + laplace
#  N3 <- sum(iris2$Species == Ck & iris2$new == level3) + laplace
#  N <-  sum(iris2$Species == Ck) + laplace * n_new_factors
#  ck_bayes <- c(N1, N2, N3) / N
#  
#  # Compare estimates
#  rbind(ck_mle, ck_bayes)
#  
#  # Unlike MLE, the Bayesian estimate for level1 assigns positive probability
#  # but is slightly overestimated. Compared to MLE,
#  # estimates for level2 and level3 have been slightly shrunken.
#  
#  # In general, the higher value of laplace, the more resulting
#  # distribution tends to the uniform distribution.
#  # When laplace would be set to infinity
#  # then the estimates for level1, level2 and level3
#  # would be 1/3, 1/3 and 1/3.
#  
#  # Comparison with estimates obtained with naive_bayes function:
#  nb_mle <- naive_bayes(Species ~ new, data = iris2)
#  nb_bayes <- naive_bayes(Species ~ new, data = iris2, laplace = laplace)
#  
#  # MLE
#  rbind(ck_mle,
#        "nb_mle" = tables(nb_mle, which = "new")[[1]][ ,Ck])
#  
#  # Bayes
#  rbind(ck_bayes,
#        "nb_bayes" = tables(nb_bayes, which = "new")[[1]][ ,Ck])
#  
#  
#  # Impact of 0 probabilities on posterior probabilities:
#  new_data <- data.frame(new = c("level1", "level2", "level3"))
#  
#  # The posterior probabilities are NaNs, due to division by 0 when normalization
#  predict(nb_mle, new_data, type = "prob", threshold = 0)
#  
#  # By default, this is remediated by replacing zero probabilities
#  # with a small number given by threshold.
#  # This leads to posterior probabilities being equal to prior probabilities
#  predict(nb_mle, new_data, type = "prob")

## ----eval = FALSE-------------------------------------------------------------
#  # Prepare data: --------------------------------------------------------
#  data(iris)
#  
#  # Define the feature and class of interest
#  Xi <- "Petal.Width" # Selected feature
#  Ck <- "versicolor"  # Selected class
#  
#  # Build class sub-sample for the selected feature
#  Ck_Xi_subsample <- iris[iris$Species == Ck, Xi]
#  
#  # Maximum-Likelihood Estimation (MLE)
#  mle_norm <- cbind("mean" = mean(Ck_Xi_subsample),
#                    "sd" = sd(Ck_Xi_subsample))
#  
#  # MLE estimates obtained using the naive_bayes function
#  nb_mle <- naive_bayes(x = iris[Xi], y = iris[["Species"]])
#  rbind(mle_norm,
#        "nb_mle" = tables(nb_mle, which = Xi)[[Xi]][ ,Ck])

## ----eval=FALSE---------------------------------------------------------------
#  # Prepare data: --------------------------------------------------------
#  data(iris)
#  
#  # Selected feature
#  Xi <- "Sepal.Width"
#  
#  # Classes
#  C1 <- "setosa"
#  C2 <- "virginica"
#  C3 <- "versicolor"
#  
#  # Build class sub-samples for the selected feature
#  C1_Xi_subsample <- iris[iris$Species == C1, Xi]
#  C2_Xi_subsample <- iris[iris$Species == C2, Xi]
#  C3_Xi_subsample <- iris[iris$Species == C3, Xi]
#  
#  # Estimate class conditional densities for the selected feature
#  dens1 <- density(C1_Xi_subsample)
#  dens2 <- density(C2_Xi_subsample)
#  dens3 <- density(C3_Xi_subsample)
#  
#  # Visualisation: -------------------------------------------------------
#  plot(dens1, main = "", col = "blue", xlim = c(1.5, 5), ylim = c(0, 1.4))
#  lines(dens2, main = "", col = "red")
#  lines(dens3, main = "", col = "black")
#  legend("topleft", legend = c(C1, C2, C3),
#         col = c("blue", "red", "black"),
#         lty = 1, bty = "n")
#  
#  # Compare to the naive_bayes: ------------------------------------------
#  nb_kde <- naive_bayes(x = iris[Xi], y = iris[["Species"]], usekernel = TRUE)
#  plot(nb_kde, prob = "conditional")
#  
#  dens3
#  nb_kde$tables[[Xi]][[C3]]
#  tables(nb_kde, Xi)[[1]][[C3]]
#  
#  
#  # Use custom bandwidth selector: ---------------------------------------
#  ?bw.SJ
#  nb_kde_SJ_bw <- naive_bayes(x = iris[Xi], y = iris[["Species"]],
#                        usekernel = TRUE, bw = "SJ")
#  plot(nb_kde, prob = "conditional")
#  
#  
#  # Visualize all available kernels: -------------------------------------
#  kernels <- c("gaussian", "epanechnikov", "rectangular","triangular",
#              "biweight", "cosine", "optcosine")
#  iris3 <- iris
#  iris3$one <- 1
#  
#  sapply(kernels, function (ith_kernel) {
#      nb <- naive_bayes(formula = Species ~ one, data = iris3,
#                        usekernel = TRUE, kernel = ith_kernel)
#      plot(nb, arg.num = list(main = paste0("Kernel: ", ith_kernel),
#                              col = "black"), legend = FALSE)
#      invisible()
#  })

## ----eval = FALSE-------------------------------------------------------------
#  # Simulate data: -------------------------------------------------------
#  cols <- 2
#  rows <- 10
#  set.seed(11)
#  M <- matrix(rpois(rows * cols, lambda = c(0.1,1)), nrow = rows,
#              ncol = cols, dimnames = list(NULL, paste0("Var", seq_len(cols))))
#  y <- factor(sample(paste0("class", LETTERS[1:2]), rows, TRUE))
#  Xi <- M[ ,"Var1", drop = FALSE]
#  
#  # MLE: -----------------------------------------------------------------
#  # Estimate lambdas for each class
#  tapply(Xi, y, mean)
#  
#  # Compare with naive_bayes
#  pnb <- naive_bayes(x = Xi, y = y, usepoisson = TRUE)
#  tables(pnb, 1)
#  
#  # Adding pseudo-counts via laplace parameter: --------------------------
#  laplace <- 1
#  Xi_pseudo <- Xi
#  Xi_pseudo[y == "classB",][1] <- Xi_pseudo[y == "classB",][1] + laplace
#  Xi_pseudo[y == "classA",][1] <- Xi_pseudo[y == "classA",][1] + laplace
#  
#  # Estimates
#  tapply(Xi_pseudo, y, mean)
#  
#  # Compare with naive_bayes
#  pnb <- naive_bayes(x = Xi, y = y, usepoisson = TRUE, laplace = laplace)
#  tables(pnb, 1)

## ----eval = FALSE-------------------------------------------------------------
#  # Prepare data for an artificial example: --------------------------------------
#  set.seed(1)
#  cols <- 3       # words
#  rows <- 100     # all documents
#  rows_spam <- 10 # spam documents
#  
#  # Probability of no-spam for each word
#  prob_non_spam <- prop.table(runif(cols)) # C_1
#  
#  # Probability of spam for each word
#  prob_spam <- prop.table(runif(cols)) # C_2
#  
#  # Simulate counts of words according to the multinomial distributions
#  M1 <- t(rmultinom(rows - rows_spam, size = cols, prob = prob_non_spam))
#  M2 <- t(rmultinom(rows_spam,        size = cols, prob = prob_spam))
#  M <- rbind(M1, M2)
#  colnames(M) <- paste0("word", 1:cols) ; rownames(M) <- paste0("doc", 1:rows)
#  head(M)
#  
#  # Simulate response with spam/no-spam
#  y <- c(rep("non-spam", rows - rows_spam), rep("spam", rows_spam))
#  
#  # Additive smoothing
#  laplace <- 0.5
#  
#  # Estimate the multinomial probabilities p_{ik} (i is word, k is class)
#  # p1 = (p_11, p_21, p_31) (non-spam)
#  # p2 = (p_12, p_22, p_32) (spam)
#  
#  N_1 <- sum(M1)
#  N_i1 <- colSums(M1)
#  p1 <- (N_i1 + laplace) / (N_1 + cols * laplace)
#  
#  N_2 <- sum(M2)
#  N_i2 <- colSums(M2)
#  p2 <- (N_i2 + laplace) / (N_2 + cols * laplace)
#  
#  # Combine estimated Multinomial probabilities for each class
#  cbind("non-spam" = p1, "spam" = p2)
#  
#  # Compare to the multinomial_naive_bayes
#  mnb <- multinomial_naive_bayes(x = M, y = y, laplace = laplace)
#  coef(mnb)
#  # colSums(coef(mnb))

