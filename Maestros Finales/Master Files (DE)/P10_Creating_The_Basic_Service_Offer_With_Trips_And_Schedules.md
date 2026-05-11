---
title: Creating the basic service offer with trips and schedules
shortTitle: Service offer
intro: Learn how to create a business service, review your journeys by line and sense,
  and leave a valid and executable offer before moving to Schedule at GoalBus.
contentType: how-tos
versions:
- '*'
---
## Creating the commercial service that will act as container of the offer

Before you review individual trips, you need to create the **commercial service** that will act as a container for your offer. In GoalBus, business services are the governance layer of the offer: they link lines and routes, day types and calendar logic, and trips that define the real service. The tool makes it clear that this structure prevents incomplete or unrevised schedules from being used operationally.

Use this quick start when you already have a validated network, a defined time base, and need to transform that structure into a real offer that can then be validated, measured, and consumed in Scheduling.

Before you start, make sure that:

1. You've already set up types of holidays and days in P2.
2. You've already validated the operating year on P3.
3. You've already prepared the base and operational network at P4 and P5.
4. You've already defined parking spaces, warehouses and trips in P6 and P7.
5. You've already defined vehicle types allowed in P8.
6. You've already created the time version and travel times on P9.
7. You're clear what line, what kind of day and what sense you'll use as a reference case.

For this quick start, use this reference case:

> **I'm going to create the L1 business service, review your return trips and leave the offer validated before moving to Schedule.**

To create the commercial service of your case:

1. In GoalBus, go to the **Services** view.
ref: P10_Imagen1.png | compact
2. Find out if there is already a commercial service suitable for your case.
3. If the service already exists, open it and check that it really corresponds to the type of day and the offer you want to prepare.
4. If it doesn't exist, create a new one.
ref: P10_Imagen2.png | compact(2x)
5. Define:
   1. A clear **name** for service,
   2. The **type of day** to be applied,
   3. The **lines** that will be part of that service.
   4. The **description** service if you want to give more detail, although this field is not mandatory.
6. Save the service.
ref: P10_Imagen3.png | compact(x8)
7. Confirm that you can already enter your schedule view or travel grid.

For the reference case, a valid option could be:

- **Standard working day - L1**

It is also possible to create the new service from the GTFS file load. To do this:
1. 1. In GoalBus, go to the **Services** view.
ref: P10_Imagen1.png | compact
2. Import GTFS files from **Import services**.
ref: P10_Imagen11.png | compact
3. If there are no errors in loading, the service will have been created correctly.
4. Entering the service, you can see all the trips created with the import.

When you finish this section, you should have a commercial service that acts as a structured container of the offer.
ref: P10_Imagen4.png  | full



## Accessing the travel grid and changing context

Once the service is created, the next step is to enter the travel grid. This view is a centralized “control tower” for all scheduled trips within the service. From here you can change line, change service and alternate between **Sentido 1** and **Sentido 2** without losing the operating context.

Before starting this section, make sure that:

1. You've already created or validated the commercial service.
2. You know what line you want to check first.
3. You know what sense or direction you'll use as a starting point.

To access and change context in the travel grid:

1. In the service list, click the service identifier or the **View schedules** icon.
2. Once inside, use the line selector to switch between the lines included in the service.
3. Use the service drop-down menu if you want to compare with another commercial service.
4. Switch between **Sentido 1** and **Sentido 2** to separately review round trips.
5. Keep the focus on a single line and one sense while building your base case.

For the reference case:

1. Open the **Standard working day - L1** service.
2. Enter **Sentido 1** first.
3. Check **Sentido 2** later.
ref: P10_Imagen5.png  | full

When you finish this section, you should be able to navigate the offer without losing the context of line, service and address.

## Creating or reviewing service travel

Now yes, enter the detail of the **travel**. The document explains that a schedule is a sequence of events and that each trip must be linked to:

1. a specific route variation,
2. a sequence of stops,
3. and a temporary reference.

This ensures that outputs and arrivals are physically executable. In addition, the grid shows by default only the main stops or time points to keep a clear view, although you can zoom in to see all intermediates.

Before starting this section, make sure that:

1. You already have a valid time version in P9.
2. You know what route variation corresponds to the trip you want to create or review.
3. You know what line and what sense you're editing.

To create or review service trips:

1. Within the service, select a line and a sense.
2. Check the trips that already exist in the grid.
3. If you need to create a new trip, use the corresponding action to add a new exit.
ref: P10_Imagen9.png | compact
4. Assigns the trip:
   1. the correct **path or variation**,
   2. the **time of departure**,
   3. and the **temporary reference** consistent with the version created in P9.
ref: P10_Image10.png
5. If the journey already exists, pass the cursor over your identifier to check which route variation you are using.
6. Check that the calculated total duration makes sense compared to the defined travel times.
7. Expand the sequence if you need to check all intermediate stops.
8. Repeat the process until you have a minimum base of journeys per sense.

For the reference case, you can start with a minimum structure like this:

1. L1 - Sentido 1
   1. Travel 1: departure 06:00
   2. Travel 2: exit 06:20
2. L1 - Sentido 2
   1. Travel 1: exit 06:10
   2. Travel 2: departure 06:30

When you finish this section, you should have a basic travel offer already linked to route, sense, and time reference.

## Reviewing intervals, total duration and balance of supply

After creating or reviewing trips, you need to check that the offer makes sense as a whole. The grid allows you to keep an eye on:

1. the **total duration** for each trip,
2. the **interval** with respect to the previous journey,
3. and global KPIs per line, such as travel count, total distance and total driving time. This makes it possible to assess whether the offer is balanced, symmetrical and economically viable.

Before continuing, make sure that:

1. You already have at least some trips created or reviewed.
2. You can already see the total length of those trips.
3. You can already compare senses and frequencies.

To validate the balance of supply:

1. In the grid, check the **total duration** for each trip.
2. Check that it reasonably matches the expected travel times.
3. Check the **interval** with respect to the previous journey and see if there are excessive gaps or outputs too close together.
4. Compare the number of **Sentido 1** trips to the **Sentido 2**.
5. Check the line's global KPIs:
   1. **Travel account**,
   2. **Total distance**,
   3. **Total time**.
ref: P10_Imagen6.png | compact
6. Corrects any obvious imbalance before giving the service for ready.

For the reference case, ask yourself:

1. Is the round trip and round trip balanced?
2. Do travel intervals correspond to the level of offer you want to build?
3. Is the total duration of each trip consistent with the time reference?
4. Does the offer seem economically reasonable or is it oversized?

When you finish this section, you should have an offer not only created, but also revised from the point of view of frequency, duration and balance.

## Validating the service to leave it ready for calculation

The last step is **validate** service. Validating blocks travel data and enables it for programming, while an unvalidated service is still in editing phase and is not ready for calculation. It also indicates that a validated service becomes restricted for editing, ceases to be removable and is ready for programming use.

Before you finish, make sure that:

1. You've already checked the service trips.
2. You've already checked routes, durations and intervals.
3. You've already confirmed that the offer responds to the case you want to build.

To validate the service and leave it ready for Scheduling:

1. Check the service's travel grid one last time.
2. Confirm that you don't need to edit the service anymore.
3. Run the **Validate** action on the service or on the corresponding travel set.
ref: P10_Imagen7.png | full
4. Check that the status of the service changes to **Validation**.
ref: P10_Imagen8.png | compact(2x)
5. Confirms that:
   1. travel is blocked for accidental changes,
   2. the service is now **ready for calculation**,
   3. and Scheduling can read it in the next steps.
6. If you still need to make changes, use the **Do not validate** logic only to return the service to editing and finish adjusting it before validating it again.

For the reference case, do not continue to Schedule until you can state:

1. Line L1 has a consistent workable offer.
2. Travels are associated with the correct route variation.
3. The total duration and intervals make sense.
4. The service is already in **Validation** status.

When you finish this section, you should have an already structured, revised and validated business offer ready for Scheduling to consume.

## Additional readings

- [Validating operational structure: warehouses, units and groups](P11_Validating_The_Operational_Structure_And_Status_Of_The_Service.md)
