# Load the dataset

library(readxl)
telco <- read_excel(file.choose())

#dummy variable creatio

library(fastDummies)
dmy <- dummyVars("~ .",data =telco[c(22,24)],fullRank = TRUE )
dat_transformed <- data.frame(predict(dmy,newdata = telco[c(22,24)]))
finaldata <- cbind(telco[c(22,24)],dat_transformed)
#Choosing columns for clustering
te <- telco[,c(9,13,25,26,29,30)]
mydata <- as.data.frame(te)

summary(mydata)
str(mydata)

# Normalize the data
normalized_data <- scale(mydata[, ]) 
summary(normalized_data)

# Distance matrix by daisy method and gower distance

d <- cluster::daisy(normalized_data, metric = "gower" ,stand = FALSE) 


fit <- hclust(d, method = "complete")

# Display dendrogram
plot(fit) 
plot(fit, hang = -1)

#Grouping of dendogram

groups <- cutree(fit, k = 3) # Cut tree into 3 clusters

rect.hclust(fit, k = 3, border = "red")

membership <- as.matrix(groups)

final <- data.frame(membership, mydata)

aggregate(mydata[,], by = list(final$membership), FUN = mean)

library(readr) 
write_csv(final, "hclustoutput.csv")

getwd()
