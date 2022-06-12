library(tidyverse)
library(EpiEstim)
library(patchwork)

setwd("D:\\ARTS1422\\Final\\608\\608_new\\531\\ref")
## load data
case.asym.wider.sh<-read.csv('case.asym.wider.sh.csv')

# observation
cases<-case.asym.wider.sh %>%
  select(date,pos) %>%
  mutate(date=as.Date(date)) %>%
  rename(I=pos,dates=date)
print(cases)
## make config
config <- make_config(
  mean_si = 4,
  std_si = 2
)


## estimate
res <- estimate_R(
  incid = cases,
  method = "parametric_si",
  config = config
)


#plot(res)

res.r<-res$R %>% as_tibble() %>%
  rename(mean=`Mean(R)`,std=`Std(R)`,lbd=`Quantile.0.025(R)`,ubd=`Quantile.0.975(R)`) %>%
  mutate(date=cases$dates[res$R$t_end])

#print(res.r$mean)

res.si <- as_tibble(list(time=as.integer(str_sub(names(res$si_distr),2)),
                         frequency=as.vector(res$si_distr)))

p1<-ggplot(data = cases,aes(x=dates,y=I))+
  geom_col(fill= "#AD002AFF")+
  scale_x_date(date_breaks = "2 days",date_labels = "%m/%d",expand = c(0,0.5))+
  labs(x="",y="每日新增阳性数",title="Epidemic curve")+
  theme_bw()+
  theme(axis.text.x = element_text(angle=45,vjust=0.5,hjust = 0.5))

p2<-ggplot(data = res.r,aes(x=date,y=mean))+
  geom_ribbon(aes(ymin=lbd,ymax=ubd),fill= "#AD002AFF",alpha=0.2)+
  geom_line(size=1,colour= "#AD002AFF")+
  geom_hline(yintercept = 1,size=1,lty=2)+
  scale_x_date(date_breaks = "2 days",date_labels = "%m/%d",expand = c(0,0.5),limits = c(as.Date('2022-03-09'),Sys.Date()-1))+
  labs(x="",y="时变再生数Rt",title='')+
  theme_bw()+
  theme(axis.text.x = element_text(angle=45,vjust=0.5,hjust = 0.5))

p3<-ggplot(data = res.si,aes(x=time,y=frequency))+
  geom_line()+
  labs(x="Time",y="Frequency",title='Assumptive Serial Interval Distribution')+
  theme_bw()

p1+p2+plot_layout(ncol = 1)
p3