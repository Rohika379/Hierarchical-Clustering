# Load the dataset

library(readxl)
ea <- read_excel(file.choose())
ea1 <- ea[,c (2,4,7:11)]
mydata <- as.data.frame(ea1)

summary(mydata)
str(mydata)

# Normalize the data
normalized_data <- scale(mydata[, ]) 
summary(normalized_data)

# Distance matrix

d <- dist(normalized_data, method = "euclidean") 

fit <- hclust(d, method = "complete")

# Display dendrogram
plot(fit) 
plot(fit, hang = -1)



groups <- cutree(fit, k = 3) # Cut tree into 10 clusters

rect.hclust(fit, k = 3, border = "red")

membership <- as.matrix(groups)

final <- data.frame(membership, mydata)

aggregate(mydata[,], by = list(final$membership), FUN = mean)

library(readr)
write_csv(final, "hclustoutput.csv")

getwd()
