# griddy_snc_project

The first R script is a matching pair analysis + statistical significance test of extra point percentage before and after the extra point distance was moved back.
</br>
</br>
The matching pair analysis identifies wind, score differential, and stadium as potential confounding variables. There was an issue with too many NAs when accounting for stuff like temperature, but the stadium variable takes that into account. I decided to conduct a two-sample t-test to determine statistical significance. The P value was way under zero, and the null hypothesis was rejected.
