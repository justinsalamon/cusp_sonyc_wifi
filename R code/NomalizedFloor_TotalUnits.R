test<-read.csv(Users/xq277/Desktop/ct1522.csv)
test<-read.csv(ct1522.csv)
test<-ct1522
test

head(test)
for (i in 1:length(test$fid)){
  if(test$NumFloors[i] > 3.00){
    test$UnitsTotal[i] <- (3/test$NumFloors[i]*test$UnitsTotal[i])
  }
  else (test$UnitsTotal[i]<-test$UnitsTotal[i])
}
head(test)
sum(test$UnitsTotal)