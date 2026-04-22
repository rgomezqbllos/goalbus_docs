---
title: Defining versions of time and travel times for the operation
shortTitle: Versions and Times
intro: Learn how to create time versions, define travel and permanency times by day
  type and time slot, and leave a reliable time reference before creating or adjusting
  services in GoalBus.
contentType: how-tos
versions:
- '*'
---
## Creating the version of time your case will use

Before you define travel times, you need to create an **time version**. In GoalBus, a version is not just a tag: it is the time library that groups together the time logic that will apply to specific routes and specific day types. This is important because on a Monday morning it does not behave like a Sunday morning, and the system should not reuse a single set of times for the whole year.

Use this quick start when you already have a line and its defined routes, and you need to build the time base that will then be used to calculate travel, validate durations and compare deviations against the standard.

Before you start, make sure that:
1. You've already prepared the master network at P6.
2. You've already checked the operating network at P7.
3. You've already set the time base of day types to P2.
4. You've already validated the operating year on P3.
5. You know what line, what routes and what kind of day you're going to use as a reference.

For this quick start, use this reference case:

> **I will create a time version for the L1 line on working days and use it as a temporary reference before creating or adjusting services.**

To create the time version of your case:
1. In GoalBus, open the **Paths view** of the line you will use as a reference.
2. Select the **Management of travel and stop times** icon or option.
ref: P9_Imagen1.png | compact
3. At the top of the view, create a new version by selecting **New set of schedules**.
ref: P9_Imagen2.png | compact
4. Defines a clear **name** for the version.
5. Add an **description** to help you distinguish the operating context.
6. Select the **types of day** to which that version applies, for example **Working days**.
7. Link the **route variations** or specific sequences that will be part of that temporary version.
8. Save the version.
ref: P9_Imagen3.png | compact(x8)
9. Check that the version is already available as a temporary reference for that line.

For the reference case, a valid version could be called:
- **Working days of winter**
- **L1 working base**

When you finish this section, you should have created a time version that the system can use as a temporary reference for the services of that line similar to that of the image below.
ref: P9_Imagen4.png | full

## Defining travel times between main stops

After creating the version, you need to enter the **travel times**. In GoalBus, these times are mainly defined between **Main stops** or **time points**, not between all intermediate stops. Headers are the main by default, and from there you build the temporary logic that will then feed the services.

In addition, GoalBus does not work with a single value per segment. The engine uses an **minimum, optimal and maximum** logic to give control flexibility to the calculation:
1. **Minimum**: the fastest time possible.
2. **Optimal**: the target time the engine will set to.
3. **Maximum**: the slowest time acceptable.

Before starting this section, make sure that:
1. You've already created the time version.
2. You know what major stops you'll use as a reference.
3. You've already identified the direction you want to configure first.

To define the travel times of your case:
1. Within the time grid, select the **segment** between two main stops.
ref: P9_Imagen5.png | full
2. Create one or more **slots** to reflect operational reality.
3. For each stripe, enter:
   1. the time **minimum**,
   2. the time **optimal**,
   3. time **maximum**.
ref: P9_Imagen6.png | compact
4. Save the segment.
5. Repeat the process for the next main segment.
6. When you finish a sense, repeat the same logic for the opposite sense.

The strips created should not have gaps or overlaps between them. In case there were, it will not be possible to save the times.

For the reference case, a basic logic could be:
1. **Terminal North → Center**
   1. 07:00–09:00
      1. Minimum: 12 min
      2. Optimal: 15 min
      3. Maximum: 18 min
   2. 09:00-22:00
      1. Minimum: 5 min
      2. Optimal: 5 min
      3. Maximum: 5 min
   3. 22:00–06:00
      1. Minimum: 8 min
      2. Optimal: 10 min
      3. Maximum: 12 min
2. **Center → Hospital**
3. **Hospital → University**
4. **University → South Terminal**

When you finish this section, you should have defined elastic driving times between the main time points of the route.

## Defining retention times for regulation and recovery

In addition to driving time, GoalBus needs to know how long a vehicle can stay at a main stop. These **Scale times** are important because they allow you to regulate the output, absorb early arrivals and leave room for recovery at terminals or connection points.

Before starting this section, make sure that:
1. You've already defined travel times between the main segments.
2. You know which terminals or important points need regulation.
3. You've already identified where real operational space is needed.

To define the scale times:
1. In the time grid, select the **column** from a main stop.
ref: P9_Imagen7.png | full
2. Choose an important terminal, header or connection point.
3. Define:
   1. **Minimum**, as mandatory waiting time.
   2. **Maximum**, as an allowed margin for regulation or synchronization.
4. Save the settings.
5. Repeat the process for other main stops where you need controlled permanence.

For the reference case, a possible logic would be:
1. **North Terminal**
   1. Minimum: 4 min
   2. Maximum: 10 min
2. **South Terminal**
   1. Minimum: 5 min
   2. Maximum: 12 min

When you finish this section, you should have defined the margins that the engine can use to recover or regulate without deforming the logic of the schedule.

## Checking slots, extended view and visual consistency

Once you already have travel and permanency times, you need to check if the grid reflects a realistic logic. The document highlights that GoalBus includes visual aids to detect errors when you handle many data points, many strips, or multiple paths.

Before continuing, make sure that:
1. You've set up at least one slot.
2. You've already introduced minimum, optimal and maximum values.
3. You've already added retention times at the relevant points.

To visually review the consistency of the configuration:
1. Check the grid and confirm that each main segment has a valid time slot.
2. Use available visual aids to detect abnormal values.
3. Check if peak hours show times higher than valley hours.
4. Expand the view if you need to see more detail or more intermediate stops.
5. Corrects any anomalous value directly from the view or from the editing panel.
6. Repeat the review until the time logic reflects a credible operation.

For the reference case, ask yourself:
1. Does rush hour show up with times higher than night?
2. Do the minimum, optimal and maximum times have a logical relationship?
3. Do terminals have realistic regulatory space?
4. Does the grid already represent a full working day?

When you finish this section, you should have a visually revised time base free of major inconsistencies.

## Applying the time version as a reference for services

The ultimate goal of this quick start is not only to create temporary data, but to leave a reference that can then be used when creating or modifying services. The document indicates that each trip must be measured against an **temporary reference version**, and that this reference is used automatically when you create new trips or change the route of a trip. It also allows to detect deviations if a trip was imported or modified outside the standard.

Before you finish, make sure that:
1. You've already created a valid temporary version.
2. You've already defined travel and stay times.
3. You've already checked the consistency of the grid.
4. You know what line and case you'll use to create services.

To check that your temporary base is ready for the services:
1. Check the version of time you just created.
2. Confirms that it is linked to the correct type of day.
3. Confirm that it includes the routes or variations you are going to use.
4. Checks that such a version could already act as a temporary reference for:
   1. create new trips,
   2. recalculate arrival and departure times,
   3. audit discrepancies against the standard.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, go back and correct the version or its times before continuing.

By the time you finish this section, you should be able to say that the line already has a reference time version sufficient to create services in a coherent way.

## Additional readings

- [Creating the basic service offer: travel or service groups by line, route and meaning](P10_Creating_The_Basic_Service_Offer_With_Trips_And_Schedules.md)
