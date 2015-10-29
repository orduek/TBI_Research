src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"
src="jspsych-4.3/jspsych.js"
src="jspsych-4.3/plugins/jspsych-text.js"
src="jspsych-4.3/plugins/jspsych-single-stim.js"


age=prompt("What age are you?");

// Set the variables for each age.
if (age==0) {
	stimExp=1
	maxTime=1
	goTrialNo=2
	nogoTrialNo=2
} else if (0<age<5) {
	stimExp=2
	maxTime=2
	goTrialNo=24
	nogoTrialNo=8
} else if (5<age<=10) {
	stimExp=1
	maxTime=1
	goTrialNo=60
	nogoTrialNo=20
} else if (age>10) {
	stimExp=0.5
	maxTime=1
	goTrialNo=90
	nogoTrialNo=30
}

