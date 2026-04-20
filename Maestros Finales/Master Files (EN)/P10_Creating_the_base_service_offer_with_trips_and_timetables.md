---
title: Creating the base service offer with trips and timetables
shortTitle: Service offer
intro: "Learn how to create a commercial service, review its trips by line and direction, and leave a validated, executable offer before moving on to Scheduling in GoalBus."
contentType: how-tos
versions:
  - "*"
---

## Creating the commercial service that will contain the offer

Before reviewing individual trips, you need to create the **commercial service** that will act as the container for your offer. In GoalBus, commercial services are the governance layer for the offer: they link lines and routes, day types and calendar logic, and the trips that define the real service. This structure helps prevent incomplete or unreviewed timetables from being used operationally.

Use this quick start when you already have a validated network, a defined time foundation, and you need to turn that structure into a real offer that can be validated, measured, and consumed in Scheduling.

Before you begin, make sure that:
1. You already configured day types and holidays in P2.
2. You already validated the operational year in P3.
3. You already prepared the master and operational networks in P6 and P7.
4. You already prepared parkings and depots in P5.
5. You already defined allowed vehicle types in P4.
6. You already loaded deadhead trips and driver repositioning in P8.
7. You already created the time version and travel times in P9.
8. You know which line, day type, and direction you will use as the reference case.

For this quick start, use this reference case:

> **I’m going to create the workday commercial service for line L1, review its outbound and inbound trips, and leave the offer validated before moving on to Scheduling.**

To create the commercial service for your case:
1. In GoalBus, go to the **Services** view.
ref: P10_Imagen1.png | compact
2. Check whether a suitable commercial service already exists for your case.
3. If it exists, open it and confirm it truly matches the day type and offer you want to prepare.
4. If it does not exist, create a new one.
ref: P10_Imagen2.png | compact
5. Define:
   1. A clear **name** for the service,
   2. The **day type** that applies,
   3. The **lines** that will be included in that service,
   4. The **description** if you want to provide more detail (optional).
6. Save the service.
ref: P10_Imagen3.png | compact
7. Confirm you can enter its timetable view or trip grid.

For the reference case, a valid option could be:
- **Standard workday - L1**

It is also possible to create the new service by importing GTFS files. To do so:
1. In GoalBus, go to the **Services** view.
ref: P10_Imagen1.png | compact
2. Import the GTFS files via **Import services**.
ref: P10_Imagen11.png | compact
3. If there are no upload errors, the service will be created successfully.
4. Open the service to see all trips created by the import.

When you finish this section, you should have a commercial service that acts as a structured container for the offer.
ref: P10_Imagen4.png  | full

## Accessing the trip grid and switching context

Once the service is created, the next step is to open the trip grid. This view is a central “control tower” for all scheduled trips within the service. From here you can switch lines, switch services, and alternate between **Direction 1** and **Direction 2** without losing operational context.

Before you start this section, make sure that:
1. You already created or validated the commercial service.
2. You know which line you want to review first.
3. You know which direction you will use as your starting point.

To access and switch context in the trip grid:
1. In the services list, click the service identifier or the **View timetables** icon.
2. Use the line selector to switch between lines included in the service.
3. Use the services dropdown if you want to compare with another commercial service.
4. Switch between **Direction 1** and **Direction 2** to review outbound and inbound trips separately.
5. Keep the focus on one line and one direction while you build your base case.

For the reference case:
1. Open **Standard workday - L1**.
2. Start with **Direction 1**.
3. Then review **Direction 2**.
ref: P10_Imagen5.png  | full

When you finish this section, you should be able to navigate the offer without losing line, service, and direction context.

## Creating or reviewing the service trips

Now go into trip details. A timetable is a sequence of events, and each trip should be linked to:
1. a specific route variation,
2. a stop sequence,
3. and a time reference.

This ensures departures and arrivals are physically executable. The grid shows only key stops/time points by default to keep a clear view, but you can expand the view to see all intermediate stops.

Before you start this section, make sure that:
1. You already have a valid time version in P9.
2. You know which route variation corresponds to the trip you want to create or review.
3. You know which line and direction you are editing.

To create or review the service trips:
1. Within the service, select a line and a direction.
2. Review the trips that already exist in the grid.
3. If you need to create a new trip, use the action to add a new departure.
ref: P10_Imagen9.png | compact
4. Assign to the trip:
   1. the correct **route/variation**,
   2. the **departure time**,
   3. and a **time reference** consistent with the version created in P9.
   ref: P10_Imagen10.png
5. If the trip already exists, hover over its identifier to check which route variation it uses.
6. Confirm the computed total duration makes sense versus the travel times defined.
7. Expand the sequence if you need to review all intermediate stops.
8. Repeat until you have a minimum trip base per direction.

For the reference case, you can start with a minimal structure like:
1. L1 - Direction 1
   1. Trip 1: departure 06:00
   2. Trip 2: departure 06:20
2. L1 - Direction 2
   1. Trip 1: departure 06:10
   2. Trip 2: departure 06:30

When you finish this section, you should have a basic offer of trips already linked to route, direction, and time reference.

## Reviewing headways, total duration, and offer balance

After creating or reviewing trips, you need to verify the offer makes sense as a set. The grid lets you continuously monitor:
1. the **total duration** of each trip,
2. the **headway** vs. the previous trip,
3. and global KPIs per line such as trip count, total distance, and total driving time.

This helps you evaluate whether the offer is balanced, symmetric, and economically reasonable.

Before you continue, make sure that:
1. You have at least a few trips created or reviewed.
2. You can see their total duration.
3. You can compare directions and frequencies.

To validate offer balance:
1. In the grid, review the **total duration** for each trip.
2. Confirm it reasonably matches the expected travel times.
3. Review the **headway** vs. the previous trip and detect excessive gaps or departures too close together.
4. Compare the number of trips in **Direction 1** vs. **Direction 2**.
5. Review the line’s global KPIs:
   1. **Trip count**,
   2. **Total distance**,
   3. **Total time**.
ref: P10_Imagen6.png | compact
6. Fix any obvious imbalance before considering the service ready.

For the reference case, ask yourself:
1. Are outbound and inbound balanced?
2. Do headways match the service level you want to build?
3. Is each trip’s total duration coherent with the time reference?
4. Does the offer look economically reasonable, or is it oversized?

When you finish this section, you should have an offer that is not only created, but also reviewed from the perspective of frequency, duration, and balance.

## Validating the service so it is ready for calculation

The last step is to **validate** the service. Validation locks trip data and enables the service for scheduling, while a non-validated service remains in editing and is not ready for calculation. A validated service becomes restricted for editing, can no longer be deleted, and is ready for use in scheduling.

Before you finish, make sure that:
1. You already reviewed the service trips.
2. You already checked routes, durations, and headways.
3. You already confirmed the offer matches the case you want to build.

To validate the service and leave it ready for Scheduling:
1. Review the trip grid one last time.
2. Confirm you do not need to keep editing the service.
3. Run the **Validate** action on the service (or the relevant trip set).
ref: P10_Imagen7.png | full
4. Confirm the service status changes to **Validated**.
ref: P10_Imagen8.png | compact
5. Confirm that:
   1. trips are locked against accidental changes,
   2. the service is now **ready for calculation**,
   3. Scheduling will be able to read it in the next steps.
6. If you still need changes, use **Unvalidate** only to return the service to editing, finish adjustments, and validate again.

For the reference case, do not continue to Scheduling until you can state:
1. Line L1 has a coherent workday offer.
2. Trips are linked to the correct route variation.
3. Total duration and headways make sense.
4. The service is in **Validated** status.

When you finish this section, you should have a commercial offer structured, reviewed, and validated—ready for Scheduling to consume.

## Additional reading

- [Validating the operational structure and service status](P11_Validating_operational_structure_and_service_status.md)

