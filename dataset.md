# Dataset Description

## Dataset 1 - Real Time Zonal Demand

**Description** : This dataset contains real-time electricity demand data for various zones in Ontario. Each record includes the date, hour, and interval, along with the total Ontario demand and demand values for individual zones such as NORTHWEST, NORTHEAST, OTTAWA, EAST, TORONTO, ESSA, BRUCE, SOUTHWEST, NIAGARA, and WEST. The dataset also provides the total demand across all zones and the difference (DIFF) between the calculated total and the reported Ontario demand. This data can be used for analyzing regional electricity consumption patterns and supporting smart grid investment decisions.

**Range** : January 1, 2025  - June 13, 2025

## Dataset 2 - Hourly Ontario Zonal Price Report

**Description** : This dataset provides hourly pricing information for electricity in Ontario's zones. Each record includes the date, the day-ahead zonal energy price (in $/MWh) for each hour, the zonal price, the energy loss price, and the energy congestion price. These fields enable detailed analysis of electricity market dynamics, including price fluctuations, congestion impacts, and losses across different zones and time periods. The dataset is valuable for market participants, analysts, and researchers interested in understanding and forecasting electricity prices and grid efficiency.

**Range** : May 14, 2025 - June 14, 2025

## Dataset 3 - Dispatch Deviation Report
**Description** : The data in these files represents monthly summaries of dispatch deviations recorded by the IESO, detailing instances where actual dispatch actions differed from the dispatch algorithm’s recommendations. Each report contains a table with the following features: the type of action taken (such as "One Time Dispatch" or "Blocked Dispatch"), and the rationale for each action, categorized as Non Compliance (NC), Operating Security Limit (OSL), Operating Reserve (OR), Area Control Error (ACE), Data Failure (DF), Planned Outage (PO), Input Error (IE), Energy Limited Resource (ELR), and Other (OTH). For each action and rationale combination, the table lists the number of occurrences in that month, along with row and column totals. These features allow users to analyze the frequency and reasons for significant dispatch deviations, providing insight into system reliability and operational challenges for each month.

### Action Definitions:
- One Time Dispatch:   The IESO issued a one-time-dispatch of resources for system reliability (security and adequacy) purposes - not unit or resource specific.
- Blocked Dispatch:   The IESO blocked a dispatch to a resource(s) for system reliability (security and adequacy) purposes.

### Rationale Definitions:
- Non Compliance(NC):   The action was required to correct for recognized non-compliance of dispatch instructions by a Market Participant(s).
- Operating Security Limit(OSL*):    The action was taken to respect a limit due to differences in the forecast and actual flows, or address a reliability need.
- Operating Reserve(OR*):    The action was taken to respect the forecasted (greater than 5 minutes) OR requirement.
- Area Control Error(ACE*):    The action was taken to correct an over / under generation condition.
- Data Failure(DF):    The action was taken to mitigate the effects of operational data input failures.
- Planned Outage(PO):    The action was taken to facilitate a planned equipment outage.
- Input Error(IE):    The action was taken to mitigate the effects dispatch algorithm input errors.
- Energy Limited Resource(ELR):    The action was taken to preserve resources adequacy for future energy needs, or address equipment limitations
- Other(OTH):    The action was taken for reasons not listed above, or where multiple rationale are applicable.

**Range** : Jan, 2025 - Apr, 2025

## Dataset 4 - Transmission Outages 

**Description** : The PUB_TxOutagesTodayAll.xml file provides a comprehensive, structured report of all transmission outages occurring today within the IESO-controlled grid. Each outage entry, called an OutageRequest, details the planned start and end times, priority, recurrence, and current status of the outage. For each outage, the file lists all affected equipment, including the equipment name, type (such as breaker, line section, disconnect, capacitor, etc.), voltage level, and the type of operational constraint (e.g., Out of Service, Holdoff, Information, etc.). Additional fields specify the recall time for the equipment and the implementation status of the outage. The document header includes metadata such as the report title, creation timestamp, and confidentiality class. This XML format enables automated systems or analysts to track, analyze, and visualize the status and scope of transmission outages across the Ontario power grid for the current day, supporting operational awareness and planning.

**Range** : March 2015 to June 20, 2025

## Dataset 5 - Adequacy Report
**Description** : This script automates the process of downloading and extracting key data from a series of IESO Adequacy Report XML files available online. For each report, it parses the delivery date, hourly total supply, and Ontario demand, then compiles this information into a single, organized Excel spreadsheet. This enables users to efficiently analyze electricity supply and demand trends across multiple days, supporting data-driven insights and reporting for Ontario’s power system. The script is robust, easy to use, and can be extended to include additional fields as needed.

**Range** : 21 June, 2025 to 24 July, 2025

## Dataset 5 - Day Ahead Hourly Ontario Zonal Energy Price Report
**Description** : This script streamlines the collection and analysis of electricity adequacy data from multiple IESO XML reports. By automatically downloading each report, extracting important metrics such as delivery date, hourly total supply, and Ontario demand, and compiling the results into a single Excel file, it provides a convenient and efficient way to monitor and analyze power system trends over time. The resulting spreadsheet enables users to easily visualize and interpret supply and demand patterns, supporting informed decision-making and reporting for Ontario’s electricity grid.

**Range** : 15 June, 2025 to 21 June, 2025

## Dataset 6 - Generator Output and Capability
**Description** : This dataset provides detailed records of generator output and capability across Ontario’s power system. For each generator, it includes hourly or interval-based measurements of actual electricity production, as well as the generator’s available and maximum capability. By capturing both real-time output and operational limits, this dataset enables grid operators, planners, and analysts to assess generation performance, monitor system adequacy, and support informed decision-making for resource planning and reliability management. The data is essential for understanding how Ontario’s generation fleet responds to system needs and for identifying opportunities to optimize grid operations.

**Range** : 23 May, 2025 to 22 June, 2025

## Dataset 7 - Intertie Flows
**Description** : This report provides a comprehensive overview of scheduled and actual power flows across interties within the electric grid. It details the planned (scheduled) energy transfers between interconnected systems and compares them with the real-time (actual) flows, offering valuable insights into grid operations, reliability, and efficiency. The report is essential for system operators, planners, and stakeholders to monitor intertie performance, identify discrepancies, and support informed decision-making for grid management and optimization.

**Range** : 24 May, 2025 to 21 June, 2025

## Dataset 8 - Variable Generation Forecast
**Description** : This XML dataset provides a detailed forecast of variable electricity generation—such as wind and solar—across Ontario’s intertie connections for a specific date and intertie zone. It includes hourly schedules for imports and exports, as well as interval-by-interval measurements of actual power flow. By enabling direct comparison between scheduled and real-time intertie transactions, the report supports grid operators and analysts in monitoring the performance and variability of renewable generation, assessing system flexibility, and making informed decisions to ensure reliable and efficient cross-border electricity exchanges.

**Range** : 23 May, 2025 to 22 June, 2025

## Dataset 9 - Surplus Baseload Generation (SBG) Forecast Report
**Description** : This XML dataset provides a comprehensive forecast of Surplus Baseload Generation (SBG) conditions for a specific date and intertie zone. It includes detailed hourly schedules for imports and exports, as well as interval-by-interval records of actual power flows across intertie connections. By comparing scheduled and real-time flows, the report enables grid operators and analysts to monitor SBG events, assess system flexibility, and make informed decisions to maintain grid reliability and efficiency. This dataset is essential for understanding cross-border electricity exchanges and managing surplus generation within the Ontario power system.

**Range** : 02 June, 2025 to 21 June, 2025








