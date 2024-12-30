# To Go for Two or Not to Go for Two? A Statistical Analysis of the Biggest Prisoner’s Dilemma in the National Football League
Wharton Sports Analytics Journal Fall 2024 Submission
## Description
The first R script is a matching pair analysis + statistical significance test of extra point percentage before and after the extra point distance was moved back.
</br>
</br>
Basic details: Looked at 9-year samples before and after the rule (2015-2023 and 2006-2014). Filtered out extra point attempts that weren't 33 and 20 yards respectively. Used the MatchIt package to match the data.
</br>
</br>
The matching pair analysis identifies wind, score differential, and stadium as potential confounding variables. There was an issue with too many NAs when accounting for stuff like temperature, but the stadium variable takes that into account. I decided to conduct a two-sample t-test to determine statistical significance. The P value was way under zero, and the null hypothesis was rejected.
</br>
</br>
The analysis includes examining the extra-point and two-point conversion probabilities on a team-by-team basis to determine whether teams would be better off going for two. Additionally, a game theory is applied to this conclusion. Under the current extra-point distance, teams would be better off going for two. A Monte Carlo simulation was run to determine the proper extra-point distance.
