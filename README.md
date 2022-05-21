# The finder of the free and perspective domains

## List of modules

The project suppose to have modules:
- Creator: create domain names with respective technique
- Checker: check availability of domain name in given zone
- Estimator: estimate available domains and produce rating of most perspective domains

## CREATOR module

The simplest module.

It creates domains:
- At first stages, we consider only `ru` zone
- Get name from DomainName and create record in Domain table with given zone

It checks domains:
- Get not checked or not checked for a long time domain
- Get from whois info and write it in db

