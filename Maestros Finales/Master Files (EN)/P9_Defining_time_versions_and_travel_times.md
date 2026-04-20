---
title: Defining time versions and travel times for operations
shortTitle: Versions and times
intro: 'Learn how to create time versions, define travel and dwell times by day type and time band, and establish a reliable time reference before creating or adjusting services in GoalBus.'
contentType: how-tos
versions:
  - '*'
---

## Creating the time version your case will use

Before defining travel times, you need to create a **time version**. In GoalBus, a version is not just a label: it is the time library that groups the time logic applied to specific routes and specific day types. This matters because Monday morning does not behave like Sunday morning, and the system should not reuse a single time set for the entire year.

Use this quick start when you already have a line and its routes defined and need to build the time foundation that will later be used to calculate trips, validate durations, and compare deviations against the standard.

Before you begin, make sure that:
1. You already prepared the master network in P6.
2. You already reviewed the operational network in P7.
3. You already configured the day-type calendar foundation in P2.
4. You already validated the operational year in P3.
5. You know which line, which routes, and which day type you will use as reference.

For this quick start, use this reference case:

> **I’m going to create a time version for line L1 on workdays and use it as my time reference before creating or adjusting services.**

To create the time version for your case:
1. In GoalBus, open the **Routes view** for the line you will use as reference.
2. Select the icon/option for **Travel and stop time management**.
ref: P9_Imagen1.png | compact
3. At the top of the view, create a new version by selecting **New timetable set**.
ref: P9_Imagen2.png | compact
4. Define a clear **name** for the version.
5. Add a **description** that helps you distinguish the operating context.
6. Select the **day types** this version applies to, for example **Workdays**.
7. Link the **route variations** or specific sequences that will be part of that time version.
8. Save the version.
ref: P9_Imagen3.png | compact
9. Confirm the version is now available as a time reference for that line.

For the reference case, valid names could be:
- **Winter workdays**
- **L1 base workday**

When you finish this section, you should have created a time version the system can use as the time reference for that line’s services, similar to the following image.
ref: P9_Imagen4.png | full

## Defining travel times between key stops

After creating the version, you need to enter **travel times**. In GoalBus, these times are primarily defined between **key stops** or **time points**, not between every intermediate stop. Terminals are key by default, and from there the time logic is built to feed services.

GoalBus also does not work with a single value per segment. The engine uses a **minimum, optimal, and maximum** logic to provide controlled flexibility:
1. **Minimum**: the fastest possible time.
2. **Optimal**: the target time the engine will aim for.
3. **Maximum**: the slowest acceptable time.

Before you start this section, make sure that:
1. You already created the time version.
2. You know which key stops you will use as reference.
3. You identified which direction you want to configure first.

To define travel times for your case:
1. In the time grid, select the **segment** between two key stops.
ref: P9_Imagen5.png | full
2. Create one or more **time bands** to reflect operational reality.
3. For each band, enter:
   1. the **minimum** time,
   2. the **optimal** time,
   3. the **maximum** time.
ref: P9_Imagen6.png | compact
4. Save the segment.
5. Repeat for the next key segment.
6. When you finish one direction, repeat the same logic for the opposite direction.

Time bands must not have gaps or overlaps between them. If they do, the system will not allow saving the times.

For the reference case, a basic logic could be:
1. **North Terminal → Downtown**
   1. 07:00–09:00
      1. Minimum: 12 min
      2. Optimal: 15 min
      3. Maximum: 18 min
   2. 09:00–22:00
      1. Minimum: 5 min
      2. Optimal: 5 min
      3. Maximum: 5 min
   3. 22:00–06:00
      1. Minimum: 8 min
      2. Optimal: 10 min
      3. Maximum: 12 min
2. **Downtown → Hospital**
3. **Hospital → University**
4. **University → South Terminal**

When you finish this section, you should have flexible driving times defined between the route’s main time points.

## Defining dwell times for regulation and recovery

Beyond driving time, GoalBus needs to know how long a vehicle can remain at a key stop. These **dwell times** matter because they allow departure regulation, absorb early arrivals, and create recovery margin at terminals or connection points.

Before you start this section, make sure that:
1. You already defined travel times between key segments.
2. You know which terminals or key points require regulation.
3. You identified where real operational margin is needed.

To define dwell times:
1. In the time grid, select the **column** of a key stop.
ref: P9_Imagen7.png | full
2. Choose a terminal, headway point, or important connection point.
3. Define:
   1. **Minimum** as mandatory waiting time,
   2. **Maximum** as allowed margin for regulation or synchronization.
4. Save the configuration.
5. Repeat for other key stops where you need controlled dwell.

For the reference case, one possible logic is:
1. **North Terminal**
   1. Minimum: 4 min
   2. Maximum: 10 min
2. **South Terminal**
   1. Minimum: 5 min
   2. Maximum: 12 min

When you finish this section, you should have margins the engine can use to recover or regulate without distorting the timetable logic.

## Reviewing time bands, expanded view, and visual consistency

Once you have travel and dwell times, you need to review whether the grid reflects realistic logic. GoalBus includes visual aids to detect errors when you manage many points, many bands, or multiple routes.

Before you continue, make sure that:
1. You configured at least one time band.
2. You entered minimum, optimal, and maximum values.
3. You added dwell times at the relevant points.

To visually review consistency:
1. Review the grid and confirm every key segment has a valid time band.
2. Use the available visual aids to detect anomalous values.
3. Check whether peak hours show higher times than off-peak.
4. Expand the view if you need more detail or more intermediate stops.
5. Fix any anomalous value directly in the view or from the edit panel.
6. Repeat until the time logic reflects a credible operation.

For the reference case, ask yourself:
1. Do peak hours show higher times than night?
2. Do minimum, optimal, and maximum keep a logical relationship?
3. Do terminals have realistic regulation margin?
4. Does the grid already represent a full operating day?

When you finish this section, you should have a time foundation visually reviewed and free of major inconsistencies.

## Applying the time version as the reference for services

The final goal is not only to create time data, but to establish a reference that can be used when creating or modifying services. Each trip should be measured against a **reference time version**, and that reference is used automatically when you create new trips or change a trip’s route. It also helps detect deviations if a trip was imported or modified outside the standard.

Before you finish, make sure that:
1. You already created a valid time version.
2. You already defined travel and dwell times.
3. You reviewed the grid’s consistency.
4. You know which line and case you will use to create services.

To confirm your time foundation is ready for services:
1. Review the time version you just created.
2. Confirm it is linked to the correct day type.
3. Confirm it includes the routes/variations you will use.
4. Verify that this version could already act as the time reference to:
   1. create new trips,
   2. recalculate arrival and departure times,
   3. audit discrepancies against the standard.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, go back and correct the version or its times before proceeding.

When you finish this section, you should be able to state that the line already has a sufficient reference time version to create services coherently.

## Additional reading

- [Creating the base service offer with trips and timetables](P10_Creating_the_base_service_offer_with_trips_and_timetables.md)

