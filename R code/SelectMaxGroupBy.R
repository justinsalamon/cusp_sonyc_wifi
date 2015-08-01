library(sqldf)
test<-read.csv("~/Desktop/bklyCT.csv")
id<-unique(test$ssid)
subset<-test[1:length(id),]

start<-Sys.time()
for(i in 1:length(id)){
  index<-which(as.character(test$ssid)==as.character(id[i]))
  temp<-test[index,]
  temp<-temp[which(temp$level==max(temp$level))[1],]
  subset[i,]<-temp
}
end<-Sys.time()
end-start

subset[1:20,]

