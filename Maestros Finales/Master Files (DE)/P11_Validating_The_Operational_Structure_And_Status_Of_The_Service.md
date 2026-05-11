---
title: Validating the operational structure and status of the service
shortTitle: Operational structure
intro: Learn how to review deposits, units and operating groups, and validate the
  service created to make it really eligible for Scheduling before moving on to rules
  and calculation.
contentType: how-tos
versions:
- '*'
---
## Reviewing the operating structure that supports your service

Before moving on to rules and the Scheduling scenario, you need to check that your offer not only exists, but is supported by a coherent operating structure. At this stage you need to check whether the line, deposit, operating unit and related groups belong to the same business and operating context.

Use this quick start when you have already created the base service offer and need to confirm that the organizational environment that supports it is correct before calculating.

Before you start, make sure that:
1. You already created the service offer at P10.
2. You've already set up parking lots and warehouses in P6.
3. You've already defined fleet and base line restrictions at P8.
4. You're clear what line and service you'll use as a reference.

For this quick start, use this reference case:

> **I'm going to validate that line L1, the North Depot, the associated operating unit and the related groups form a coherent basis before taking the service to Scheduling.**

To review the operating structure of your case:
1. Opens the configuration or operating view related to the service you have just created.
2. Identify which **deposit** supports the service.
3. Check that deposit matches the physical basis you defined earlier.
4. Check which **operational unit** the line or service belongs to.
5. Check if that unit fits the infrastructure, geography, and organization of the case.
6. Check the related **groups** that affects that context, if they exist.
7. Confirms that the line, unit and deposit do not belong to incompatible structures.
8. If you detect an inconsistency, correct it before continuing.

For the reference case, check:
1. That line L1 is associated with the North Depot.
2. That deposit belongs to the right unit.
3. That linked groups do not point to another operational area.

When you finish this section, you should be clear that the service offer lives within a consistent operating structure.

## Confirming that the service is already validated and ready for programming

After reviewing the operating structure, you need to confirm something critical: that the service created in P10 is already in **Validation** status. It is not enough to have created trips, intervals and routes. In order for Scheduling to read the service and consider it eligible, the service must have gone through the validation action.

Before starting this section, make sure that:
1. You've already checked the commercial service and their P10 trips.
2. You've already checked intervals, routes and durations.
3. You no longer need to edit the service at this stage.

To confirm that the service is ready for programming:
1. Open the commercial service you will use as a reference.
2. Check your current **status**.
3. If the status is already **Validation**, confirm that there is nothing pending before continuing.
4. If the service is still in editing or in a previous state, run the **Validate** action.
5. Check that the state changes correctly.
6. Check that:
   1. the service is no longer a draft,
   2. travel is protected against accidental changes,
   3. and the service can already be consumed by Scheduling.
7. If you detect a structure error, correct it before revalidating.

For the reference case, do not continue until you can state:
1. Line L1 already has its revised workable offer.
2. The service has already changed to **Validation** status.
3. The system can now be used as a programming input.

When you finish this section, you should have a service really prepared to be read by the engine.

## Checking consistency between structure, service and eligibility

Now you need to do a final joint review. The goal is not only to have a validated service, but to confirm that the validated service lives in the correct structure and does not drag organizational inconsistencies that then complicate the calculation.

Before continuing, make sure that:
1. You've already checked warehouse, unit and groups.
2. You've already validated the service or confirmed its validation.
3. You know what case you're gonna take next.

To validate full eligibility before Scheduling:
1. Check the validated service and confirm which line you use.
2. Check that line is still linked to the correct deposit.
3. Check that the operational unit and the groups do not contradict the context of the service.
4. Ask yourself if the system could already take that service as a valid and consistent input for calculation.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, correct the structure or return the service to editing only if you need to redo part of the base before revalidating it.

For the reference case, make sure that:
1. L1 belongs to the correct organisational context.
2. The North Deposit is really the basis for the service.
3. The workable service is already validated and has no contradictions with its structure.

When you finish this section, you should be able to state that the offer is not only created, but also structurally aligned and eligible for Scheduling.

## Additional readings

- [Defining Vehicle Rules for Scheduling](P12_Defining_Vehicle_Rules_For_Scheduling.md)
