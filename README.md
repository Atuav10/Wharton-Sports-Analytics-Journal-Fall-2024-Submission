# griddy_snc_project

The first R script is a matching pair analysis + statistical significance test of extra point percentage before and after the extra point distance was moved back.
</br>
</br>
Basic details: Looked at 9-year samples before and after the rule (2015-2023 and 2006-2014). Filtered out extra point attempts that weren't 33 and 20 yards respectively. Used the MatchIt package to match the data.
</br>
</br>
The matching pair analysis identifies wind, score differential, and stadium as potential confounding variables. There was an issue with too many NAs when accounting for stuff like temperature, but the stadium variable takes that into account. I decided to conduct a two-sample t-test to determine statistical significance. The P value was way under zero, and the null hypothesis was rejected.
