library(sqldf)
test<-red.csv("~/Desktop/ceshi1.csv")
df1<-sqldf("SELECT lat, lng, GROUP_CONCAT(DISTINCT ssid) AS ssid_list, level  FROM test GROUP BY test.pair ORDER BY test.pair")
write.csv(df1,file="test.csv")
df2<-data.frame(unique(df$ssid))
length(df2$unique.df.ssid.)

