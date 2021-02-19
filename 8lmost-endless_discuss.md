#### temporary from Discussing-platforms 
such as https://stackshare.io/ https://www.reddit.com/ etc 
### pagerduty_vs_victorops_vs_opsgenie 

comparision PD-vs-VO-vs-OG: {

	https://www.reddit.com/r/devops/comments/g34drp/pagerduty_vs_victorops_vs_opsgenie/: {
		- whether or not you have a mature incident management procedures,,
		- [ Victor Ops (prior to Splunk acquiring them) was very no frills, cost was good, but features; Ops Genie (prior to them getting acquired by Atlassian) was a good middle ground ],,
		- [ 10 months ago We switched from Pagerduty to Opsgenie about 2 years ago. The main driver was price, Opsgenie was about half the cost of Pagerduty; In PagerDuty you had every alert received turn into a page. With Opsgenie you can autoclose, filter to different teams etc. It also means you can share an API endpoint between different levels of alerts or even different teams; Possibly PagerDuty has improved since but they mostly seemed to concentrate on the reporting tools (probably because the senior managers were the ones making the buying decisions). ],,
		- I’d take a look at xMatters as well, they’re in the same category and have some decent features and you can do all sorts of cool tricks with the calendaring/shifts.,,
		- You should definitely check out Squadcast - https://www.squadcast.com/
		Its way better than PD or OpsGenie for a bunch of reasons. Completely free to use for up to 10 users - Their platform is the easiest to work with, and their team truly empathises with the pains of being on-call.,,
		- reducing lot of oncall noise,,
		- We use OpsGenie and we haven't had any problems. We have integrations going with Azure, Prometheus, and PRTG (among others).,,
		- We were a PagerDuty shop and within the last 6 months moved to OpsGenie. There are definitely a few things I miss from PD - like auto refresh on the alerts page or reassigning an alert to a different team, but overall there's just way more flexibility with OpsGenie, and the price is much nicer.,,
		- One thing I can vouch for in terms of PagerDuty is the API they provide - building internal tools such as Slack bots from their API is really nice and seamless.,,
		- Do also check out Zenduty if you're looking for a more end-to-end incident alerting and response solution,,
		- I work for OnPage ( https://www.onpage.com/incident-alert-management-for-it/ ) and we operate within IT alerting and incident orchestration.,,
	},

        https://stackshare.io/stackups/opsgenie-vs-pagerduty {
		- OpsGenie: Alerting and On-Call Management for Dev&Ops Teams. OpsGenie is a cloud-based service for dev & ops teams, providing reliable alerts, on-call schedule management, and escalations. OpsGenie integrates with monitoring tools & services and ensures that the right people are at the right time; 
		- PagerDuty: Incident management with powerful visibility, reliable alerting, and improved collaboration. PagerDuty is an alarm aggregation and dispatching service for system administrators and support teams. It collects alerts from your monitoring tools, gives you an overall view of all of your monitoring alarms, and alerts an on duty engineer if there's a problem.,,
		- 
	}

}
