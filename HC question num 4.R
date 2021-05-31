
auto <- read.csv("D:\\ROHIKA\\Telco_customer_churn.xlsx")
#categorical encoder
library(caret)
dmy <- dummyVars("~ .",data = auto[c(8,9,11,12)],fullRank = TRUE)
dat_tra <- data.frame(predict(dmy,newdata = auto[c(8,9,11,12)]))
final <- cbind(auto[-c(8,9,11,12)],dat_tra)

#columns for clustering

cls <- final[,c(3,8,9,10,11,13,18)]
summary(cls)

#normalisation

n_data <- scale(cls)
summary(n_data)

#Distance matrix

d <- dist(n_data, method = "euclidian")
fit <- hclust(d, method = "complete")
 
#Displaying dendogram

plot(fit)
plot(fit , hang= -1)


groups <- cutree(fit, k = 3) # Cut tree into 3 clusters

rect.hclust(fit, k = 3, border = "red")

membership <- as.matrix(groups)

final <- data.frame(membership, cls)

aggregate(cls[,], by = list(final$membership), FUN = mean)

library(readr) 
write_csv(final, "hclustoutput.csv")

getwd()
