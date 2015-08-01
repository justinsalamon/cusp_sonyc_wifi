test<-read.csv("/Users/xq277/Desktop/ct52.csv")
dim(test)
test[grep("5g",rownames(test)),]
require(sqldf)
test[grep("5g",test$ssid),"ssidnew"]

length(grep("5g",test$ssid))
length(grep("5ghz",test$ssid))
length(grep("guest",test$ssid))

flag<-0
test<-cbind(test,flag)
test<-data2

for(i in 1:(length(test$ssid)-1)){
  temp<-length(grep(test$ssid[i],test$ssid[i+1]))
  if(temp==1){
    test$flag[i+1]<-1
    test$FREQUENCY[i]<-test$FREQUENCY[i]+test$FREQUENCY[i+1]
  }
}
data2<-test[which(test$flag!=1),]
dim(data2)
write.csv(data2, file = "~/Desktop/MyData.csv")
