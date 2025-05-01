---
title: "Two Paths in the Woods"
date: "2023-02-15"
description: "Steve McGhee and Sal Furino present two independently developed methods for teaching SRE topics to customers"
event: "SLOconf 2023"
location: "Online"
video: "https://www.youtube.com/watch?v=xM7jT5qUJmY"
type: "video"
---

# Two Paths in the Woods

Exploring different approaches to teaching and implementing SRE practices.

{{< youtube "xM7jT5qUJmY" >}}

## Abstract

While the direction and intent of SRE has been established and is becoming better-understood, the details on how to achieve "SRE" is still an exercise left for the reader.

Steve from Google and Sal from Nobl9 present two independently developed methods for teaching SRE topics to customers, which we have discovered are actually quite similar. Huzzah!

Steve presents the "reliability map" and Sal shows Nobl9's SLODLC. Both are essentially sets of documentation presented in a way that allows customers to take a guided path through the dark and scary woods that is today's SRE.

The "reliability map" provides a detailed accounts of what development, infrastructure, operational, observability, and people/culture activities organizations can expect to be practicing to achieve different eras of reliability (99%, 99.9%, 99.99%, 99.999%). The "reliability map" takes it one step further and provides descriptions and references to additional content for all activities.

SLODLC provides a framework of documentation and templates to allow customers to iterate on improving their SLOs. This is especially necessary when customers have high reliability targets in which rely upon automation to execute predetermined playbooks. (rollback, exponential backoff, autoscale, etc) If SLOs are the indicator the performance of a user journey and decide when actions needs to be taken, then customers need a clear and useable way to explain:

- What they are attempting to measure (golden signals?, something else?)
- Why was it decided to measure X in such a way?
- How is X impactful for the targeted user journey?
- When was the last time the SLO objective, metric, time window, etc was changed?
- When the error budget is in danger of being breeched what actions should be take?

In short both projects are approaching the same topic of helping customers improve their reliability from different points of view and they synergize well together.

## Resources

- [Video Recording](https://www.youtube.com/watch?v=xM7jT5qUJmY) 