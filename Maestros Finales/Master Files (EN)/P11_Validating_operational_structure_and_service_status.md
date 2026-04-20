---
title: Validating the operational structure and service status
shortTitle: Operational structure
intro: 'Learn how to review depots, operating units, and operational groups, and validate the created service so it is truly eligible for Scheduling before moving on to rules and calculation.'
contentType: how-tos
versions:
  - '*'
---

## Reviewing the operational structure that supports your service

Before moving on to rules and the Scheduling scenario, you need to confirm that your offer not only exists, but is supported by a coherent operational structure. At this stage you should review whether the line, depot, operating unit, and any related groups belong to the same business and operating context.

Use this quick start when you have already created the base service offer and need to confirm that the organizational environment supporting it is correct before calculating.

Before you begin, make sure that:
1. You already created the service offer in P10.
2. You already configured parkings and depots in P5.
3. You already defined fleet and line-level base constraints in P4.
4. You know which line and which service you will use as reference.

For this quick start, use this reference case:

> **I’m going to validate that line L1, North Depot, the associated operating unit, and the related groups form a coherent foundation before taking the service into Scheduling.**

To review the operational structure for your case:
1. Open the configuration or operational view related to the service you just created.
2. Identify which **depot** supports the service.
3. Confirm that depot matches the physical base you defined earlier.
4. Review which **operating unit** the line or service belongs to.
5. Confirm that unit fits the infrastructure, geography, and organization of the case.
6. Review any related **groups** that affect that context, if they exist.
7. Confirm the line, unit, and depot do not belong to incompatible structures.
8. If you find an inconsistency, fix it before proceeding.

For the reference case, verify:
1. Line L1 is associated with North Depot.
2. That depot belongs to the correct operating unit.
3. Linked groups do not point to a different operational scope.

When you finish this section, you should be confident the service offer lives within a consistent operational structure.

## Confirming the service is validated and ready for scheduling

After reviewing the operational structure, you need to confirm something critical: the service created in P10 is already in **Validated** status. It is not enough to have created trips, headways, and routes. For Scheduling to read the service and consider it eligible, the service must have been validated.

Before you start this section, make sure that:
1. You already reviewed the commercial service and its trips in P10.
2. You already checked headways, routes, and durations.
3. You no longer need to keep editing the service at this stage.

To confirm the service is ready for scheduling:
1. Open the commercial service you will use as reference.
2. Review its current **status**.
3. If the status is already **Validated**, confirm there is nothing pending before you continue.
4. If the service is still in editing or a prior status, run **Validate**.
5. Confirm the status changes correctly.
6. Verify that:
   1. the service is no longer a draft,
   2. trips are protected against accidental changes,
   3. and the service can now be consumed by Scheduling.
7. If you detect a structural issue, fix it before validating again.

For the reference case, do not proceed unless you can state:
1. Line L1 already has its workday offer reviewed.
2. The service is now in **Validated** status.
3. The system can use it as a scheduling input.

When you finish this section, you should have a service that is truly ready to be read by the engine.

## Checking consistency between structure, service, and eligibility

Now do one final combined review. The goal is not only to have a validated service, but to confirm the validated service lives in the right structure and does not carry organizational inconsistencies that will complicate calculation.

Before you continue, make sure that:
1. You already reviewed depot, operating unit, and groups.
2. You already validated the service (or confirmed it is validated).
3. You know which case you will take to the next step.

To validate end-to-end eligibility before Scheduling:
1. Review the validated service and confirm which line it uses.
2. Confirm that line is still linked to the correct depot.
3. Confirm the operating unit and groups do not contradict the service context.
4. Ask yourself whether the system could take that service as a valid, coherent input for calculation.
5. If the answer is yes, continue with the next quick start.
6. If the answer is no, fix the structure or return the service to editing only if you need to rebuild part of the base before validating again.

For the reference case, make sure that:
1. L1 belongs to the correct organizational context.
2. North Depot truly supports the service.
3. The validated workday service has no contradictions with its structure.

When you finish this section, you should be able to state that the offer is not only created, but also structurally aligned and eligible for Scheduling.

## Additional reading

- [Defining vehicle rules for Scheduling](P12_Defining_vehicle_rules_for_scheduling.md)

