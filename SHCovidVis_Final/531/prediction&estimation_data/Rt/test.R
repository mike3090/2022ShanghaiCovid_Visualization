library("EpiEstim")

setwd("D:/ARTS1422/Final/531/positive_location_data/district_data")
data <- read.csv("../district_data/city_dist_merged_date.csv", encoding="UTF-8")
columns <-list("Shanghai",'Shanghai','PudongNew','Huangpu','Jingan',
            'Xuhui','Changning','Putuo','Hongkou',
            'Yangpu','Baoshan', 'Minhang', 'Jiading',
            'Jinshan', 'Songjiang', 'Huangpu', 'Fengxian',
            'Chongming')
config <- make_config(
  mean_si = 4,
  std_si = 2
)

for (each in columns) {
    cases <- data[each]
    res <- estimate_R(
        incid = cases,
        method = "parametric_si",
        config = config
    )
    res.r<-res$R %>% 
    as_tibble() %>%
    rename(mean=`Mean(R)`,std=`Std(R)`,lbd=`Quantile.0.025(R)`,ubd=`Quantile.0.975(R)`) %>%
    mutate(date=cases$dates[res$R$t_end])
    rt <- res.r$mean
    setwd("D:/ARTS1422/Final/608/608_new/531/prediction&estimation_data/Rt")
    filename <- paste(each,"Rt.csv",sep='_')
    write.csv(rt,filename)
}